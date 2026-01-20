"""
Generic Issue Handler for WCRP-universe

Processes generic issue submissions and returns JSON data to be written.
Used as fallback when no specific handler exists for an issue type.

Returns:
    tuple: (data_dict, output_path) or None if processing fails
"""

import sys
import json
import os
import glob
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from cmipld import reverse_mapping
from cmipld.utils import git

# Labels to ignore when determining issue type
IGNORE_LABELS = {'review', 'alpha', 'keep-open', 'delta', 'Review', 'universal', 'universe'}

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
    """Clean a value to be used as an @id"""
    if not value:
        return ''
    return value.lower().strip().replace(' ', '-').replace('_', '-')


def parse_labels(labels_str):
    """Parse labels string and return relevant labels (excluding ignored ones)"""
    if not labels_str:
        return []
    
    if isinstance(labels_str, str):
        try:
            labels = json.loads(labels_str)
        except json.JSONDecodeError:
            labels = [l.strip() for l in labels_str.split(',')]
    else:
        labels = labels_str
    
    return [l for l in labels if l.lower() not in {i.lower() for i in IGNORE_LABELS}]


def find_data_folder(labels):
    """Find the appropriate data folder based on labels"""
    relevant_labels = parse_labels(labels)
    
    for label in relevant_labels:
        folder_path = os.path.join(DATA_PATH, label)
        if os.path.isdir(folder_path):
            return folder_path
    
    if relevant_labels:
        return os.path.join(DATA_PATH, relevant_labels[0])
    
    return DATA_PATH


def find_existing_file(data_id, labels):
    """Find an existing file by ID across possible folders"""
    relevant_labels = parse_labels(labels)
    
    for label in relevant_labels:
        folder_path = os.path.join(DATA_PATH, label)
        file_path = os.path.join(folder_path, f"{data_id}.json")
        if os.path.exists(file_path):
            return file_path
    
    file_path = os.path.join(DATA_PATH, f"{data_id}.json")
    if os.path.exists(file_path):
        return file_path
    
    pattern = os.path.join(DATA_PATH, '**', f"{data_id}.json")
    matches = glob.glob(pattern, recursive=True)
    if matches:
        return matches[0]
    
    return None


def load_existing_file(file_path):
    """Load existing JSON file if it exists"""
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return None


def build_type_array(labels, prefix):
    """Build the @type array from labels and prefix"""
    relevant_labels = parse_labels(labels)
    types = [f'wcrp:{label}' for label in relevant_labels]
    
    if prefix and prefix not in types:
        types.append(prefix)
    
    return types


def run(parsed_issue, packet, dry_run=False):
    """
    Process generic issue and return data to write.
    
    Args:
        parsed_issue: Parsed issue content (dict)
        packet: Raw issue data including labels, author, etc.
        dry_run: If True, still process but data won't be written by caller
        
    Returns:
        tuple: (data_dict, output_path) or None if processing fails
    """
    prefix = "[DRY RUN] " if dry_run else ""
    
    print(f"\n{prefix}Processing with generic handler...")
    print(f"{'='*60}")
    
    # Get repo prefix
    repo_prefix = get_repo_prefix()
    print(f"{prefix}Repository prefix: {repo_prefix}")
    
    # Get labels
    labels = packet.get('labels_full') or os.environ.get('ISSUE_LABELS', '')
    relevant_labels = parse_labels(labels)
    print(f"{prefix}Relevant labels: {relevant_labels}")
    
    # Determine issue kind (new/modify)
    issue_kind = parsed_issue.get('issue_kind', 'New').lower()
    is_modify = issue_kind == 'modify'
    print(f"{prefix}Issue kind: {'Modify' if is_modify else 'New'}")
    
    # Get validation key / ID
    validation_key = (parsed_issue.get('validation_key') or 
                      parsed_issue.get('consortium_name') or
                      parsed_issue.get('acronym') or '')
    
    data_id = clean_id(validation_key)
    
    if not data_id:
        print(f"{prefix}❌ Error: No validation key / identifier provided")
        return None
    
    print(f"{prefix}Validation key: {validation_key}")
    print(f"{prefix}Data ID: {data_id}")
    
    # Determine output path
    data_folder = find_data_folder(labels)
    output_path = os.path.join(data_folder, f"{data_id}.json")
    
    # Handle modify vs new
    existing_data = None
    if is_modify:
        existing_path = find_existing_file(data_id, labels)
        if existing_path:
            print(f"{prefix}Found existing file: {existing_path}")
            output_path = existing_path
            existing_data = load_existing_file(existing_path)
        else:
            print(f"{prefix}⚠️ Warning: No existing file found for '{data_id}', creating new")
    else:
        # For new issues, check if file exists and refuse to overwrite
        if os.path.exists(output_path):
            print(f"{prefix}❌ Error: File already exists at {output_path}")
            print(f"{prefix}Cannot overwrite existing file with 'New' issue.")
            print(f"{prefix}Use issue_kind: 'Modify' to update an existing entry.")
            return None
    
    # Build data object
    data = existing_data.copy() if existing_data else {}
    
    # Set core fields
    data['id'] = data_id
    data['type'] = build_type_array(labels, repo_prefix)
    data['validation_key'] = validation_key
    
    # Map common fields
    field_mapping = {
        'ui_label': ['ui_label', 'full_name', 'full_name_of_the_organisation'],
        'description': ['description'],
        'url': ['url', 'activity_webpage_/_citation', 'webpage', 'website'],
    }
    
    for data_field, issue_fields in field_mapping.items():
        for issue_field in issue_fields:
            value = parsed_issue.get(issue_field, '')
            if isinstance(value, str):
                value = value.strip()
            if value and str(value).lower() not in {'_no response_', 'none', ''}:
                data[data_field] = value
                break
    
    # Copy additional fields (excluding known control fields)
    ignore_fields = {'issue_type', 'issue_kind', 'validation_key',
                     'additional_collaborators', 'collaborators', 'consortium_name', 'acronym'}
    
    for key, value in parsed_issue.items():
        if key.lower() not in ignore_fields and key not in data:
            if isinstance(value, str):
                value = value.strip()
                if value and value.lower() not in {'_no response_', 'none', ''}:
                    data[key] = value
    
    # Sort keys for consistent output
    data = dict(sorted(data.items()))
    
    print(f"\n{prefix}Output path: {output_path}")
    print(f"\n{prefix}Generated data:")
    print(json.dumps(data, indent=4))
    
    return (data, output_path)
