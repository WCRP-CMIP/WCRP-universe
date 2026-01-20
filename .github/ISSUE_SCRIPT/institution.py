"""
Institution Issue Handler

Processes institution submissions, fetches ROR data, validates, 
and returns the JSON data to be written.

Returns:
    tuple: (data_dict, output_path) or None if processing fails
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

import update_ror
import json


def similarity(name1, name2):
    """Calculate similarity between two strings as a percentage"""
    from difflib import SequenceMatcher
    matcher = SequenceMatcher(None, name1, name2)
    return matcher.ratio() * 100


def run(issue, packet, dry_run=False):
    """
    Process institution issue and return data to write.
    
    Args:
        issue: Parsed issue content (dict)
        packet: Raw issue data including labels, author, etc.
        dry_run: If True, still process but data won't be written by caller
        
    Returns:
        tuple: (data_dict, None) or None if validation fails
               Output path is set by new_issue.py
    """
    prefix = "[DRY RUN] " if dry_run else ""
    
    print(f"\n{prefix}Processing institution...")
    print(f"{'='*60}")
    
    # Extract fields
    ror_id = issue.get('ror', issue.get('description', '')).strip()
    acronym = issue.get('acronym', issue.get('label', '')).strip()
    full_name = issue.get('full_name_of_the_organisation', issue.get('long_label', '')).strip()
    
    if not acronym:
        print(f"{prefix}❌ Error: No acronym provided")
        return None
    
    data_id = acronym.lower().replace(' ', '-').replace('_', '-')
    
    print(f"{prefix}Acronym: {acronym}")
    print(f"{prefix}ID: {data_id}")
    print(f"{prefix}ROR: {ror_id or 'pending'}")
    print(f"{prefix}Full name: {full_name}")
    
    # Build data based on ROR availability
    if ror_id and ror_id.lower() != 'pending':
        # Fetch ROR data
        print(f"\n{prefix}Fetching ROR data...")
        try:
            data = update_ror.get_institution(ror_id, acronym)
            
            # Check name similarity
            ror_name = data.get('ui_label', '')
            ranking = similarity(full_name, ror_name)
            
            print(f"{prefix}Name similarity: {ranking:.1f}%")
            print(f"  Provided: {full_name}")
            print(f"  From ROR: {ror_name}")
            
            if ranking < 80:
                print(f"\n{prefix}⚠️  Warning: Low similarity ({int(ranking)}%)")
                
        except Exception as e:
            print(f"{prefix}❌ Error fetching ROR data: {e}")
            return None
    else:
        # Create basic data without ROR
        print(f"\n{prefix}Creating entry without ROR data (pending)")
        data = {
            "@context": "_context",
            "@id": data_id,
            "@type": ['wcrp:organisation', 'wcrp:institution'],
        }
        
        if full_name:
            data['ui_label'] = full_name
    
    print(f"\n{prefix}Generated data:")
    print(json.dumps(data, indent=4))
    
    # Return data only - output path is set by new_issue.py
    return (data, None)
