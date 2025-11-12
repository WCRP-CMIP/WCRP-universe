#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to remove duplicate variable files where the only difference is capitalization.
Keeps the lowercase version and ensures the 'id' field inside is also lowercase.
"""

import json
import os
from pathlib import Path
from collections import defaultdict


def find_duplicate_files(variable_dir: Path) -> dict[str, list[Path]]:
    """
    Find JSON files that are duplicates (differing only by case).

    Returns:
        Dictionary mapping lowercase filename to list of actual file paths
    """
    files_by_lowercase = defaultdict(list)

    for file_path in variable_dir.glob("*.json"):
        if file_path.name == "000_context.jsonld":
            continue
        lowercase_name = file_path.name.lower()
        files_by_lowercase[lowercase_name].append(file_path)

    # Only return groups with duplicates
    return {k: v for k, v in files_by_lowercase.items() if len(v) > 1}


def correct_id_in_file(file_path: Path) -> bool:
    """
    Ensure the 'id' field in the JSON file is lowercase.

    Returns:
        True if file was modified, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if 'id' not in data:
            print(f"  Warning: No 'id' field found in {file_path.name}")
            return False

        original_id = data['id']
        lowercase_id = original_id.lower()

        if original_id != lowercase_id:
            data['id'] = lowercase_id
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
                f.write('\n')  # Add newline at end of file
            print(f"  [OK] Corrected id in {file_path.name}: '{original_id}' -> '{lowercase_id}'")
            return True

        return False
    except Exception as e:
        print(f"  Error processing {file_path.name}: {e}")
        return False


def remove_duplicates(variable_dir: Path, dry_run: bool = True):
    """
    Remove duplicate files keeping only lowercase versions.

    Args:
        variable_dir: Path to the variable directory
        dry_run: If True, only show what would be done without making changes
    """
    duplicates = find_duplicate_files(variable_dir)

    if not duplicates:
        print("No duplicate files found!")
        return

    print(f"Found {len(duplicates)} groups of duplicate files:\n")

    files_to_remove = []
    files_to_keep = []

    for lowercase_name, file_paths in sorted(duplicates.items()):
        print(f"Duplicate group: {lowercase_name}")

        # Find the file with all lowercase name
        lowercase_file = None
        other_files = []

        for file_path in file_paths:
            if file_path.name == lowercase_name:
                lowercase_file = file_path
            else:
                other_files.append(file_path)

        if lowercase_file:
            print(f"  KEEP: {lowercase_file.name}")
            files_to_keep.append(lowercase_file)
        else:
            # If no fully lowercase version exists, keep the first one and rename it
            print(f"  WARNING: No lowercase version exists, will keep: {file_paths[0].name}")
            files_to_keep.append(file_paths[0])
            other_files = file_paths[1:]

        for file_path in other_files:
            print(f"  REMOVE: {file_path.name}")
            files_to_remove.append(file_path)

        print()

    # Summary
    print("=" * 60)
    print(f"Summary:")
    print(f"  Files to keep: {len(files_to_keep)}")
    print(f"  Files to remove: {len(files_to_remove)}")
    print("=" * 60)
    print()

    if dry_run:
        print("DRY RUN MODE - No files will be modified or deleted.")
        print("Run with --execute to apply changes.")
    else:
        print("Removing duplicate files...")
        for file_path in files_to_remove:
            try:
                file_path.unlink()
                print(f"  [OK] Removed: {file_path.name}")
            except Exception as e:
                print(f"  [ERROR] Error removing {file_path.name}: {e}")

        print("\nCorrecting 'id' fields in kept files...")
        for file_path in files_to_keep:
            correct_id_in_file(file_path)

        print("\n[OK] Done!")


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Remove duplicate variable files with capitalization differences"
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually remove files (default is dry-run mode)"
    )
    parser.add_argument(
        "--variable-dir",
        type=Path,
        default=Path(__file__).parent.parent.parent.parent.parent / "variable",
        help="Path to variable directory (default: relative to script location)"
    )

    args = parser.parse_args()

    variable_dir = args.variable_dir.resolve()

    if not variable_dir.exists():
        print(f"Error: Variable directory not found: {variable_dir}")
        return 1

    print(f"Variable directory: {variable_dir}")
    print(f"Mode: {'EXECUTE' if args.execute else 'DRY RUN'}")
    print("=" * 60)
    print()

    remove_duplicates(variable_dir, dry_run=not args.execute)

    return 0


if __name__ == "__main__":
    exit(main())
