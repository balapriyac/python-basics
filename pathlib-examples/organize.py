from pathlib import Path

def organize_files_by_extension(path_to_dir):
    path = Path(path_to_dir).expanduser().resolve()
    print(f"Resolved path: {path}")

    if path.exists() and path.is_dir():
        print(f"The directory {path} exists. Proceeding with file organization...")
   	 
    # List all items in the directory
    for item in path.iterdir():
        print(f"Found item: {item}")
        if item.is_file():
            extension = item.suffix.lower()
            target_dir = path / extension[1:]  # Remove the leading dot

            # Ensure the target directory exists
            target_dir.mkdir(exist_ok=True)
            new_path = target_dir / item.name

            # Move the file
            item.rename(new_path)

            # Confirm the file has been moved
            if new_path.exists():
                print(f"Successfully moved {item} to {new_path}")
            else:
                print(f"Failed to move {item} to {new_path}")

	  else:
       print(f"Error: The directory {path} does not exist or is not a directory.")

organize_files_by_extension('new_project')
