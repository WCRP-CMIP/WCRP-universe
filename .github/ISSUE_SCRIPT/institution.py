"""
Institution Issue Handler

Processes institution submissions, fetches ROR data, validates, 
and returns the JSON data to be written.

Works with:
    - new_issue.py: run() builds initial data, update() enriches with ROR
    - update_ror.py: get_institution() fetches full ROR data
    - upgrade_organisations.py: batch updates existing files

Functions:
    run(): Build initial data from issue (called before validation)
    update(): Enrich with ROR data (called after validation)
"""

import sys
import os
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

import update_ror
import json


def similarity(name1, name2):
    """Calculate similarity between two strings as a percentage"""
    from difflib import SequenceMatcher
    if not name1 or not name2:
        return 0
    matcher = SequenceMatcher(None, name1.lower(), name2.lower())
    return matcher.ratio() * 100


def add_label(label):
    """Add a label to the current issue"""
    if 'ISSUE_NUMBER' in os.environ:
        issue_number = os.environ['ISSUE_NUMBER']
        os.popen(f'gh issue edit {issue_number} --add-label "{label}"').read()
        print(f"Added label: {label}")


def post_issue_comment(comment):
    """Post a comment to the current issue"""
    if 'ISSUE_NUMBER' in os.environ:
        issue_number = os.environ['ISSUE_NUMBER']
        # Escape single quotes in comment
        escaped = comment.replace("'", "'\"'\"'")
        os.popen(f"gh issue comment {issue_number} --body '{escaped}'").read()
        print(f"Posted comment to issue #{issue_number}")


def build_summary(acronym, full_name, ror_id, ror_name, ranking, warnings):
    """Build a summary comment for the issue"""
    status = "✅ Passed" if not warnings else "⚠️ Needs Review"
    
    summary = f"""## Institution Validation Summary

| Field | Value |
|-------|-------|
| **Status** | {status} |
| **Acronym** | `{acronym}` |
| **Full Name (provided)** | {full_name or '_not provided_'} |
| **Full Name (from ROR)** | {ror_name or '_not available_'} |
| **ROR ID** | `{ror_id or 'pending'}` |
| **Name Similarity** | {f'{ranking:.1f}%' if ranking is not None else '_n/a_'} |

"""
    
    if warnings:
        summary += "### ⚠️ Warnings\n\n"
        for warning in warnings:
            summary += f"- {warning}\n"
        summary += "\nPlease review and confirm this submission is correct.\n"
    
    return summary


def run(issue, packet, dry_run=False):
    """
    Build initial institution data from issue.
    
    Args:
        issue: Parsed issue content (dict)
        packet: Raw issue data including labels, author, etc.
        dry_run: If True, still process but data won't be written by caller
        
    Returns:
        tuple: (data_dict, None) or None if validation fails
    """
    prefix = "[DRY RUN] " if dry_run else ""
    warnings = []
    ranking = None
    ror_name = None
    
    print(f"\n{prefix}Processing institution...")
    print(f"{'='*60}")
    
    # Extract fields
    acronym = issue.get('acronym', issue.get('label', '')).strip()
    full_name = issue.get('full_name_of_the_organisation', issue.get('long_label', '')).strip()
    ror_id = issue.get('ror', issue.get('description', '')).strip()
    
    if not acronym:
        print(f"{prefix}❌ Error: No acronym provided")
        return None
    
    data_id = acronym.lower().replace(' ', '-').replace('_', '-')
    
    print(f"{prefix}Acronym: {acronym}")
    print(f"{prefix}validation_key: {acronym}")
    print(f"{prefix}@id: {data_id}")
    print(f"{prefix}ROR: {ror_id or 'pending'}")
    print(f"{prefix}Full name: {full_name}")
    
    # If ROR is provided, fetch full data from ROR
    if ror_id and ror_id.lower() not in ['pending', '', 'none']:
        print(f"\n{prefix}Fetching ROR data...")
        try:
            data = update_ror.get_institution(ror_id, acronym)
            
            # Check name similarity
            ror_name = data.get('ui_label', '')
            if full_name and ror_name:
                ranking = similarity(full_name, ror_name)
                print(f"{prefix}Name similarity: {ranking:.1f}%")
                print(f"  Provided: {full_name}")
                print(f"  From ROR: {ror_name}")
                
                if ranking < 80:
                    warning_msg = f"Low name similarity ({ranking:.1f}%): '{full_name}' vs '{ror_name}'"
                    warnings.append(warning_msg)
                    print(f"\n{prefix}⚠️  Warning: {warning_msg}")
            
            # Post summary and add label if needed
            if not dry_run:
                summary = build_summary(acronym, full_name, ror_id, ror_name, ranking, warnings)
                post_issue_comment(summary)
                
                if warnings:
                    add_label("needs-review")
            
            print(f"\n{prefix}Generated data from ROR:")
            print(json.dumps(data, indent=4, ensure_ascii=False))
            
            return (data, None)
            
        except Exception as e:
            warning_msg = f"Could not fetch ROR data: {e}"
            warnings.append(warning_msg)
            print(f"{prefix}⚠️  Warning: {warning_msg}")
            print(f"{prefix}Creating basic entry without ROR data")
    
    # Build basic data without ROR
    data = {
        "@context": "_context",
        "@id": data_id,
        "@type": ['wcrp:organisation', 'wcrp:institution'],
        "validation_key": acronym,  # Same case as provided
    }
    
    if full_name:
        data['ui_label'] = full_name
    
    if ror_id and ror_id.lower() not in ['pending', '', 'none']:
        data['ror'] = ror_id
    
    # Post summary for non-ROR entries
    if not dry_run:
        if not ror_id or ror_id.lower() in ['pending', '', 'none']:
            warnings.append("No ROR ID provided - institution data is incomplete")
        summary = build_summary(acronym, full_name, ror_id, ror_name, ranking, warnings)
        post_issue_comment(summary)
        
        if warnings:
            add_label("needs-review")
    
    print(f"\n{prefix}Generated data (no ROR):")
    print(json.dumps(data, indent=4, ensure_ascii=False))
    
    return (data, None)


def update(data, parsed_issue, issue, dry_run=False):
    """
    Update validated data with ROR information.
    
    Called after JSONValidator has processed the file.
    This is a secondary update in case run() didn't fetch ROR data
    or if additional enrichment is needed.
    
    Args:
        data: Validated data from JSONValidator
        parsed_issue: Parsed issue content (dict)
        issue: Raw issue data including labels, author, etc.
        dry_run: If True, still process but data won't be written
        
    Returns:
        dict: Updated data with ROR information merged in
    """
    prefix = "[DRY RUN] " if dry_run else ""
    
    # Check if data already has ROR info (from run())
    if data.get('ror') and data.get('location'):
        print(f"{prefix}Data already enriched with ROR, skipping update")
        return data
    
    # Extract ROR from issue
    ror_id = parsed_issue.get('ror', parsed_issue.get('description', '')).strip()
    acronym = data.get('validation_key', data.get('@id', '').replace('-', '_'))
    full_name = parsed_issue.get('full_name_of_the_organisation', 
                                  parsed_issue.get('long_label', '')).strip()
    
    if not ror_id or ror_id.lower() in ['pending', '', 'none']:
        print(f"{prefix}No ROR ID provided, skipping ROR enrichment")
        return data
    
    print(f"\n{prefix}Enriching with ROR data: {ror_id}")
    
    try:
        # Fetch ROR data using update_ror (shared with upgrade_organisations.py)
        ror_data = update_ror.get_institution(ror_id, acronym)
        
        # Check name similarity
        ror_name = ror_data.get('ui_label', '')
        if full_name and ror_name:
            ranking = similarity(full_name, ror_name)
            print(f"{prefix}Name similarity: {ranking:.1f}%")
            print(f"  Provided: {full_name}")
            print(f"  From ROR: {ror_name}")
            
            if ranking < 80:
                print(f"\n{prefix}⚠️  Warning: Low similarity ({int(ranking)}%)")
                if not dry_run:
                    add_label("needs-review")
        
        # Merge ROR data into validated data
        # Preserve @context, @id from validated data
        # @type gets merged (keeping both validated and ROR types)
        preserved_keys = ['@context', '@id']
        
        for key, value in ror_data.items():
            if key in preserved_keys:
                continue
            if key == '@type':
                # Merge types, keeping unique values
                existing_types = data.get('@type', [])
                if not isinstance(existing_types, list):
                    existing_types = [existing_types] if existing_types else []
                new_types = value if isinstance(value, list) else [value]
                merged_types = list(dict.fromkeys(existing_types + new_types))
                data['@type'] = merged_types
            elif value is not None:
                data[key] = value
        
        print(f"{prefix}ROR data merged successfully")
        
    except Exception as e:
        print(f"{prefix}⚠️  Warning: Could not fetch ROR data: {e}")
    
    return data
