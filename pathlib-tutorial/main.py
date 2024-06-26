from pathlib import Path

# import Path from pathlib
from pathlib import Path

# create a base path
# replace user w/ a valid user :)
base_path = Path("/home/user/Documents")

# create new paths from the base path
subdirectory_path = base_path / "projects" / "project1"
file_path = subdirectory_path / "report.txt"

# Print out the paths
print("Base path:", base_path)
print("Subdirectory path:", subdirectory_path)
print("File path:", file_path)


path = Path("/home/user/Downloads")
# check if a path exists
print(path.exists())

# check if a path is a file or a directory
print(path.is_file())
print(path.is_dir())

# iterating over directory contents
for item in path.iterdir():
    print(item)

# rename files
path = Path('old_path')
path.rename('new_path')

# delete files
path.unlink()   

# delete empty directories
path.rmdir()  

# resolve paths
relative_path = Path('new_project/README.md')
absolute_path = relative_path.resolve()
print(absolute_path)

path = Path('/home/user/projectA')

# simple globbing
text_files = list(path.glob('*.txt'))
print(text_files)

# recursive globbing
text_files = list(path.rglob('*.txt'))
print(text_files)

