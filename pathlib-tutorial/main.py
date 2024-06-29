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


