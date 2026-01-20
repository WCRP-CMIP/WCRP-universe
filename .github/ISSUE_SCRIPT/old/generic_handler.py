"""
Generic Issue Handler for WCRP-universe

This script handles issue submissions by:
1. Parsing the issue body and extracting fields
2. Determining the issue type from labels
3. Loading any custom handler script if it exists
4. Creating/modifying JSON-LD data files
5. Committing with proper author attribution including co-authors
"""

import sys
import json
import os
import re
import glob
import importlib.util
from pathlib import Path

# Add parent directory to path for local imports
sys.path.append(str(Path(__file__).parent))

from cmipld.utils import git
from cmipld.utils.git import coauthors
from cmipld.utils.json import sorted_json
from cmipld import reverse_mapping

# Labels to ignore when determining issue type
IGNORE_LABELS = {'review', 'alpha', 'keep-open', 'delta', 'Review', 'universal', 'universe'}

# Path to custom issue handler scripts
SCRIPT_PATH = '.github/ISSUE_SCRIPT/'

# Base path for data files
DATA_PATH = './src-data/'


def get_repo_prefix():
    """Get the repository prefix from reverse mapping"""
    try:
        rmap = reverse_mapping
        io_url = git.url2io(git.url())
        return rmap.get(io_url, 'universal')
    except Exception as e:
        print(f"Warning: Could not determine repo prefix: {e}")
        return 'universal'


def clean_id(value):
    """
    Clean a value to be used as an @id
    - lowercase
    - no spaces (replace with -)
    - no underscores (replace with -)
    """
    if not value:
        return ''
    return value.lower().strip().replace(' ', '-').replace('_', '-')


def parse_labels(labels_str):
    """
    Parse labels string and return relevant labels (excluding ignored ones)
    """
    if not labels_str:
        return []
    
    # Handle both string and list formats
    if isinstance(labels_str, str):
        # Try to parse as JSON first
        try:
            labels = json.loads(labels_str)
        except json.JSONDecodeError:
            # Split by comma if not JSON
            labels = [l.strip() for l in labels_str.split(',')]
    else:
        labels = labels_str
    
    # Filter out ignored labels
    return [l for l in labels if l.lower() not in {i.lower() for i in IGNORE_LABELS}]


def get_issue_type_from_labels(labels):
    """
    Determine the primary issue type from labels
    Returns the first non-ignored label as the type
    """
    relevant_labels = parse_labels(labels)
    if relevant_labels:
        return relevant_labels[0]
    return None


def find_data_folder(labels):
    """
    Find the appropriate data folder based on labels
    Looks for a folder matching any of the label tags
    """
    relevant_labels = parse_labels(labels)
    
    for label in relevant_labels:
        folder_path = os.path.join(DATA_PATH, label)
        if os.path.isdir(folder_path):
            return folder_path
    
    # If no matching folder found, use the first label as folder name
    if relevant_labels:
        return os.path.join(DATA_PATH, relevant_labels[0])
    
    return DATA_PATH


def load_existing_file(file_path):
    """Load existing JSON file if it exists"""
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return None


def find_existing_file(data_id, labels):
    """
    Find an existing file by ID across possible folders
    """
    relevant_labels = parse_labels(labels)
    
    # Check all possible label folders
    for label in relevant_labels:
        folder_path = os.path.join(DATA_PATH, label)
        file_path = os.path.join(folder_path, f"{data_id}.json")
        if os.path.exists(file_path):
            return file_path
    
    # Also check base data path
    file_path = os.path.join(DATA_PATH, f"{data_id}.json")
    if os.path.exists(file_path):
        return file_path
    
    # Search recursively in src-data
    pattern = os.path.join(DATA_PATH, '**', f"{data_id}.json")
    matches = glob.glob(pattern, recursive=True)
    if matches:
        return matches[0]
    
    return None


def parse_collaborators(collab_string):
    """
    Parse collaborators string into list of GitHub usernames
    Expected format: "user1, user2, user3" or "user1 user2 user3"
    """
    if not collab_string or collab_string.strip() == '':
        return []
    
    # Replace common separators with comma
    normalized = collab_string.replace(';', ',').replace(' ', ',')
    
    # Split and clean
    collaborators = [c.strip().lstrip('@') for c in normalized.split(',') if c.strip()]
    
    # Filter out empty strings and common placeholder text
    collaborators = [c for c in collaborators if c and c.lower() not in {'e.g.', 'e.g', 'eg', 'example'}]
    
    return collaborators


def build_type_array(labels, prefix):
    """
    Build the @type array from labels and prefix
    Format: ['wcrp:label1', 'wcrp:label2', 'prefix']
    """
    relevant_labels = parse_labels(labels)
    types = [f'wcrp:{label}' for label in relevant_labels]
    
    # Add the repo prefix
    if prefix and prefix not in types:
        types.append(prefix)
    
    return types


def create_commit_message(action, item_id, issue_type, coauthor_list=None):
    """
    Create a commit message with optional co-authors
    """
    if action == 'modify':
        message = f"Modified {issue_type}: {item_id}"
    else:
        message = f"New {issue_type}: {item_id}"
    
    # Add co-author lines if present
    if coauthor_list:
        coauthor_lines = []
        for author in coauthor_list:
            if isinstance(author, dict):
                name = author.get('name', author.get('login', 'Unknown'))
                email = author.get('email', f"{author.get('login', 'unknown')}@users.noreply.github.com")
            else:
                name = author
                email = f"{author}@users.noreply.github.com"
            coauthor_lines.append(f"Co-authored-by: {name} <{email}>")
        
        if coauthor_lines:
            message += "\n\n" + "\n".join(coauthor_lines)
    
    return message


def run_custom_handler(issue_type, parsed_issue, packet):
    """
    Check for and run a custom handler script for the issue type
    Returns True if custom handler was found and executed
    """
    script_path = os.path.join(SCRIPT_PATH, f"{issue_type}.py")
    
    if os.path.exists(script_path):
        print(f"Found custom handler: {script_path}")
        
        try:
            spec = importlib.util.spec_from_file_location(issue_type, script_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            if hasattr(module, 'run'):
                print(f"Running custom handler for {issue_type}")
                module.run(parsed_issue, packet)
                return True
            else:
                print(f"Custom handler has no run() function, using generic handler")
        except Exception as e:
            print(f"Error loading custom handler: {e}")
    
    return False


def process_issue(parsed_issue, packet):
    """
    Main processing function for generic issues
    """
    # Get repo prefix for type construction
    prefix = get_repo_prefix()
    print(f"Repository prefix: {prefix}")
    
    # Get labels from packet or environment
    labels = packet.get('labels_full') or os.environ.get('ISSUE_LABELS', '')
    
    # Determine issue type from labels
    issue_type = get_issue_type_from_labels(labels)
    
    if not issue_type:
        print("Warning: Could not determine issue type from labels")
        # Try to get from parsed issue
        issue_type = parsed_issue.get('issue-type', 'unknown')
    
    print(f"Issue type: {issue_type}")
    
    # Check if this is a new or modify action
    issue_kind = parsed_issue.get('issue-kind', parsed_issue.get('issue_kind', 'New')).lower()
    is_modify = issue_kind == 'modify'
    
    print(f"Issue kind: {'Modify' if is_modify else 'New'}")
    
    # Get the validation key / ID
    validation_key = parsed_issue.get('validation-key', 
                     parsed_issue.get('validation_key',
                     parsed_issue.get('consortium-name',
                     parsed_issue.get('acronym', ''))))
    
    data_id = clean_id(validation_key)
    
    if not data_id:
        git.update_issue("❌ Error: No validation key / identifier provided")
        sys.exit("No validation key provided")
    
    print(f"Data ID: {data_id}")
    
    # Update issue summary
    git.update_summary(f"### Issue Content\n```json\n{json.dumps(parsed_issue, indent=4)}\n```")
    
    # Find data folder and file path
    data_folder = find_data_folder(labels)
    os.makedirs(data_folder, exist_ok=True)
    
    file_path = os.path.join(data_folder, f"{data_id}.json")
    
    # Handle modify vs new
    if is_modify:
        # Try to find existing file
        existing_path = find_existing_file(data_id, labels)
        
        if existing_path:
            print(f"Found existing file: {existing_path}")
            file_path = existing_path
            existing_data = load_existing_file(existing_path)
        else:
            git.update_issue(f"⚠️ Warning: Could not find existing file for ID '{data_id}'. Creating new file.")
            existing_data = None
    else:
        existing_data = None
        
        # Check if file already exists for new submissions
        if os.path.exists(file_path):
            git.update_issue(f"⚠️ Warning: File already exists at {file_path}. Will update.")
            existing_data = load_existing_file(file_path)
    
    # Build the data object
    data = existing_data.copy() if existing_data else {}
    
    # Set core fields
    data['id'] = data_id
    data['type'] = build_type_array(labels, prefix)
    data['validation-key'] = validation_key
    
    # Map common fields from issue to data
    field_mapping = {
        'ui-label': ['ui-label', 'ui_label', 'full-name', 'full-name-of-the-organisation'],
        'description': ['description'],
        'url': ['url', 'activity-webpage-/-citation', 'webpage', 'website'],
    }
    
    for data_field, issue_fields in field_mapping.items():
        for issue_field in issue_fields:
            value = parsed_issue.get(issue_field, '').strip()
            if value and value.lower() not in {'_no response_', 'none', ''}:
                data[data_field] = value
                break
    
    # Copy any additional fields that aren't in the ignore list
    ignore_fields = {'issue-type', 'issue-kind', 'issue_kind', 'validation-key', 'validation_key',
                     'additional-collaborators', 'collaborators', 'consortium-name', 'acronym'}
    
    for key, value in parsed_issue.items():
        if key.lower() not in ignore_fields:
            # Convert key format from issue (with-dashes) to data format
            if isinstance(value, str):
                value = value.strip()
                if value and value.lower() not in {'_no response_', 'none', ''}:
                    # Only add if not already set by field mapping
                    if key not in data:
                        data[key] = value
    
    # Sort the data for consistent output
    data = sorted_json(data)
    
    git.update_summary(f"### Data Content\n```json\n{json.dumps(data, indent=4)}\n```")
    
    # Create branch for the changes
    # Format: "{Issue_kind} {issue_types joined by |} : {validation-key}"
    relevant_labels = parse_labels(labels)
    issue_kind_cap = 'Modify' if is_modify else 'New'
    types_joined = ' | '.join([t.capitalize() for t in relevant_labels]) if relevant_labels else issue_type.capitalize()
    title = f"{issue_kind_cap} {types_joined} : {validation_key}"
    
    branch_name = f"{issue_kind_cap.lower()}_{data_id}".replace(' ', '_').lower()
    
    git.update_issue_title(title)
    git.newbranch(branch_name)
    
    # Write the data file
    print(f"Writing to: {file_path}")
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    
    git.update_summary(f"### File written to: `{file_path}`")
    
    # Get author information
    author = packet.get('author') or os.environ.get('ISSUE_SUBMITTER', 'unknown')
    if isinstance(author, str):
        author = {'login': author, 'name': author}
    
    # Parse collaborators
    collab_string = parsed_issue.get('additional-collaborators', 
                    parsed_issue.get('collaborators', ''))
    collaborators = parse_collaborators(collab_string)
    
    # Build co-author list
    coauthor_list = []
    for collab in collaborators:
        coauthor_list.append({
            'login': collab,
            'name': collab,
            'email': f"{collab}@users.noreply.github.com"
        })
    
    # If modifying, also include previous file authors as co-authors
    if is_modify and existing_data:
        try:
            existing_authors = coauthors.get_file_authors(file_path)
            for auth_str in existing_authors:
                # Parse "Name <email>" format
                if '<' in auth_str and '>' in auth_str:
                    name = auth_str.split('<')[0].strip()
                    email = auth_str.split('<')[1].split('>')[0].strip()
                    login = email.split('@')[0]
                    if '+' in login:
                        login = login.split('+')[1]
                    
                    # Don't add if it's the current author
                    if login != author.get('login', ''):
                        coauthor_list.append({
                            'login': login,
                            'name': name,
                            'email': email
                        })
        except Exception as e:
            print(f"Warning: Could not get existing authors: {e}")
    
    # Create commit message
    commit_msg = create_commit_message(
        'modify' if is_modify else 'new',
        data_id,
        issue_type,
        coauthor_list
    )
    
    print(f"Commit message:\n{commit_msg}")
    
    # Commit the file
    git.commit_one(file_path, author, comment=commit_msg, branch=branch_name)
    
    # Create pull request
    issue_number = os.environ.get('ISSUE_NUMBER', '')
    git.newpull(
        branch_name,
        author,
        json.dumps(data, indent=4),
        title,
        issue_number
    )
    
    print(f"✅ Successfully processed issue: {title}")


def main():
    """Main entry point"""
    from cmipld.generate.new_issue import get_issue, parse_issue_body
    
    # Get issue data
    issue = get_issue()
    parsed_issue = parse_issue_body(issue['body'])
    
    print(f"Parsed issue:\n{json.dumps(parsed_issue, indent=2)}")
    
    # Get issue type to check for custom handler
    labels = issue.get('labels_full') or os.environ.get('ISSUE_LABELS', '')
    issue_type = get_issue_type_from_labels(labels)
    
    # Also check the issue-type field in parsed content
    if not issue_type:
        issue_type = parsed_issue.get('issue-type', '')
    
    # Try to run custom handler first
    if issue_type and run_custom_handler(issue_type, parsed_issue, issue):
        print(f"Custom handler completed for {issue_type}")
        return
    
    # Fall back to generic processing
    print("Using generic issue handler")
    process_issue(parsed_issue, issue)


if __name__ == '__main__':
    main()
