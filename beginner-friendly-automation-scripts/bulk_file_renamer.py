#!/usr/bin/env python3
"""
bulk_file_renamer.py

Rename every file in a folder according to a chosen rule: add a prefix,
add a suffix, renumber sequentially, or find-and-replace text in the
filename. Runs as a dry run by default and only renames files once you
pass --apply, so you can preview the result safely first.

Usage:
    # Preview adding a prefix (dry run, nothing is renamed yet)
    python 02_bulk_file_renamer.py photos/ --mode prefix --value "vacation_"

    # Actually apply a sequential rename: photo_001.jpg, photo_002.jpg, ...
    python 02_bulk_file_renamer.py photos/ --mode sequence --value "photo_" --apply

    # Find and replace text in filenames
    python 02_bulk_file_renamer.py exports/ --mode replace --find "draft" --replace "final" --apply
"""

import argparse
from pathlib import Path


def build_new_names(files, mode, value=None, find=None, replace=None, start=1, digits=3):
    """Return a list of (old_path, new_name) pairs without touching the filesystem."""
    new_names = []

    for i, file_path in enumerate(files):
        stem, suffix = file_path.stem, file_path.suffix

        if mode == "prefix":
            new_name = f"{value}{stem}{suffix}"
        elif mode == "suffix":
            new_name = f"{stem}{value}{suffix}"
        elif mode == "sequence":
            number = str(start + i).zfill(digits)
            base = value or "file_"
            new_name = f"{base}{number}{suffix}"
        elif mode == "replace":
            new_name = f"{stem.replace(find, replace)}{suffix}"
        else:
            raise ValueError(f"unknown mode '{mode}'")

        new_names.append((file_path, new_name))

    return new_names


def check_collisions(new_names, folder):
    """Return a list of new filenames that would collide with an existing or another new file."""
    seen = set()
    collisions = []
    existing = {p.name for p in folder.iterdir() if p.is_file()}
    renaming_from = {old.name for old, _ in new_names}

    for old_path, new_name in new_names:
        if new_name in seen:
            collisions.append(new_name)
        seen.add(new_name)
        # Colliding with an existing file that isn't itself being renamed away is a problem
        if new_name in existing and new_name not in renaming_from and new_name != old_path.name:
            collisions.append(new_name)

    return sorted(set(collisions))


def main():
    parser = argparse.ArgumentParser(description="Bulk rename files in a folder.")
    parser.add_argument("folder", help="Folder containing the files to rename")
    parser.add_argument("--mode", required=True, choices=["prefix", "suffix", "sequence", "replace"],
                         help="Renaming mode")
    parser.add_argument("--value", default="",
                         help="Text to add (for prefix/suffix) or base name (for sequence)")
    parser.add_argument("--find", default=None, help="Text to find (mode=replace)")
    parser.add_argument("--replace", default=None, help="Text to replace it with (mode=replace)")
    parser.add_argument("--start", type=int, default=1, help="Starting number for sequence mode")
    parser.add_argument("--digits", type=int, default=3,
                         help="Zero-padding width for sequence numbers (default: 3)")
    parser.add_argument("--extension", default=None,
                         help="Only rename files with this extension, e.g. .jpg")
    parser.add_argument("--apply", action="store_true",
                         help="Actually rename files (default is a dry-run preview only)")
    args = parser.parse_args()

    if args.mode == "replace" and (args.find is None or args.replace is None):
        parser.error("mode=replace requires both --find and --replace")

    folder = Path(args.folder)
    if not folder.is_dir():
        parser.error(f"'{args.folder}' is not a directory")

    files = sorted(p for p in folder.iterdir() if p.is_file())
    if args.extension:
        ext = args.extension if args.extension.startswith(".") else f".{args.extension}"
        files = [p for p in files if p.suffix.lower() == ext.lower()]

    if not files:
        print("No matching files found.")
        return

    new_names = build_new_names(
        files, args.mode, value=args.value, find=args.find, replace=args.replace,
        start=args.start, digits=args.digits
    )

    collisions = check_collisions(new_names, folder)
    if collisions:
        print("ERROR: renaming would create filename collisions:")
        for name in collisions:
            print(f"  {name}")
        print("No files were renamed. Adjust your rule and try again.")
        return

    print(f"{'Renaming' if args.apply else 'Preview (dry run)'} {len(files)} file(s):\n")
    for old_path, new_name in new_names:
        print(f"  {old_path.name}  ->  {new_name}")

    if not args.apply:
        print("\nThis was a preview only. Re-run with --apply to actually rename these files.")
        return

    for old_path, new_name in new_names:
        old_path.rename(old_path.with_name(new_name))

    print(f"\nDone. {len(new_names)} file(s) renamed.")


if __name__ == "__main__":
    main()
  
