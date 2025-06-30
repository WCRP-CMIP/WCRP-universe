#!/usr/bin/env python3
"""
Script to reprocess all organization files with their original authors.
This script:
1. Gets all organization JSON files from src-data/organisation/
2. Retrieves the latest committer for each file
3. Reprocesses the file using update_ror if it's an institution
4. Recommits the file with the original author

Usage:
    python upgrade_organizations.py [--dry-run]
    
Options:
    --dry-run    Show what would be done without making actual changes
"""

import sys
from pathlib import Path
import json
import os
import glob
import subprocess
import argparse

# Add parent directory to path to import update_ror
sys.path.append(str(Path(__file__).parent))

import update_ror
from cmipld.utils import git
from cmipld.tests.jsonld import organisation
from pydantic import ValidationError

# Path to organization data
repopath = './src-data/organisation/'






def process_organization_file(filepath, dry_run=False):
    """Process a single organization file
    
    Args:
        filepath: Path to the organization file
        dry_run: If True, show what would be done without making changes
        
    Returns:
        True if changes were made/would be made
        False if no changes needed
        None if there was an error
    """
    # Get the last committer using cmipld utility
    author = git.get_last_committer(filepath)
    if not author:
        print(f"⚠️  Could not get author for {filepath}, skipping...")
        return None
        
    print(f"\n📄 Processing {filepath}")
    print(f"👤 Last committer: {author}")
    
    try:
        # Load existing data
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Check if it's an institution or consortium
        if 'type' not in data:
            print(f"⚠️  No type field in {filepath}, skipping...")
            return None
            
        ldtypes = data.get('type', [])
        
        # Process based on type
        if 'wcrp:institution' in ldtypes:
            # Get required fields
            ror = data.get('ror')
            validation_key = data.get('validation-key')
            
            if not ror or ror == 'pending':
                print(f"⚠️  No valid ROR for {filepath}, keeping existing data...")
                # Still recommit with proper author
            else:
                print(f"🔄 {'Would update' if dry_run else 'Updating'} institution data from ROR: {ror}")
                if not dry_run:
                    try:
                        # Get updated data from ROR
                        updated_data = update_ror.get_institution(ror, validation_key)
                        
                        # Validate the data
                        organisation.institution(**updated_data)
                        
                        # Check if the data has actually changed
                        with open(filepath, 'r') as f:
                            current_data = json.load(f)
                        
                        # Compare the data (normalize by dumping both to strings with same formatting)
                        current_json = json.dumps(current_data, sort_keys=True, indent=2)
                        updated_json = json.dumps(updated_data, sort_keys=True, indent=2)
                        
                        if current_json == updated_json:
                            print(f"ℹ️  No changes needed for {validation_key} - data is up to date")
                            return False  # No changes needed
                        
                        # Save the updated data
                        with open(filepath, 'w') as f:
                            json.dump(updated_data, f, indent=2)
                            f.write('\n')  # Add newline at end of file
                            
                        print(f"✅ Updated data for {validation_key}")
                        
                    except ValidationError as e:
                        print(f"❌ Validation error for {filepath}: {e.errors()[0]}")
                        return None
                    except Exception as e:
                        print(f"❌ Error updating {filepath}: {e}")
                        return None
                else:
                    # In dry run mode, still check if changes would be made
                    try:
                        # Get updated data from ROR
                        updated_data = update_ror.get_institution(ror, validation_key)
                        
                        # Check if the data would change
                        with open(filepath, 'r') as f:
                            current_data = json.load(f)
                        
                        current_json = json.dumps(current_data, sort_keys=True, indent=2)
                        updated_json = json.dumps(updated_data, sort_keys=True, indent=2)
                        
                        if current_json == updated_json:
                            print(f"ℹ️  No changes needed for {validation_key} - data is up to date")
                            return False
                        else:
                            print(f"📝 Would update {validation_key} with new ROR data")
                    except Exception as e:
                        print(f"⚠️  Could not check for updates: {e}")
                    
        elif 'wcrp:consortium' in ldtypes:
            print(f"ℹ️  Consortium type - no ROR update needed, will recommit...")
        else:
            print(f"⚠️  Unknown type in {filepath}, skipping...")
            return None
        
        # Recommit the file with the original author
        print(f"💾 {'Would recommit' if dry_run else 'Recommitting'} {filepath} with author: {author}")
        
        if not dry_run:
            # Use git.recommit_file if available, otherwise use commit_one
            if hasattr(git, 'recommit_file'):
                git.recommit_file(
                    filepath, 
                    author,
                    f"Update of {Path(filepath).stem} organization data"
                )
            else:
                # Alternative: stage and commit
                git.commit_one(
                    filepath,
                    author,
                    comment=f"Update of {Path(filepath).stem} organization data"
                )
            
        return True
        
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        return None


def main():
    """Main function to process all organization files"""
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Reprocess organization files with their original authors"
    )
    parser.add_argument(
        "--dry-run", 
        action="store_true",
        help="Show what would be done without making actual changes"
    )
    args = parser.parse_args()
    
    if args.dry_run:
        print("🆗️ DRY RUN MODE - No changes will be made")
        print("="*50)
    
    print("🚀 Starting organization file reprocessing...")
    
    # Get all JSON files (excluding graph files and context)
    files = glob.glob(os.path.join(repopath, '*.json'))
    files = [f for f in files if not any(skip in f for skip in ['graph.', '_context_'])]
    
    print(f"📁 Found {len(files)} organization files to process")
    
    # Track results
    successful = 0
    failed = 0
    unchanged = 0
    
    # Process each file
    for filepath in sorted(files):
        result = process_organization_file(filepath, dry_run=args.dry_run)
        if result is None:
            failed += 1
        elif result:
            successful += 1
        else:
            unchanged += 1
    
    # Summary
    print("\n" + "="*50)
    print(f"✅ Successfully processed: {successful} files")
    print(f"ℹ️  Unchanged: {unchanged} files (already up to date)")
    print(f"❌ Failed to process: {failed} files")
    print(f"📊 Total files: {len(files)}")
    
    # Create a branch and push if we made changes
    if successful > 0 and not args.dry_run:
        branch_name = "reprocess-organizations"
        print(f"\n🌿 Creating branch: {branch_name}")
        
        try:
            # Create and checkout new branch
            subprocess.run(['git', 'checkout', '-b', branch_name], check=True)
            
            # Push the branch
            print(f"🚀 Pushing branch: {branch_name}")
            subprocess.run(['git', 'push', '-u', 'origin', branch_name], check=True)
            
            print(f"\n✅ All changes pushed to branch: {branch_name}")
            print("📝 Please create a pull request to merge these changes.")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error with git operations: {e}")
    elif args.dry_run and successful > 0:
        print(f"\n🆗️ DRY RUN: Would have created branch 'reprocess-organizations' with {successful} files")
    

if __name__ == '__main__':
    main()
