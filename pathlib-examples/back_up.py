import shutil
from pathlib import Path

def back_up_files(directory, backup_directory):
    path = Path(directory)
    backup_path = Path(backup_directory)
    backup_path.mkdir(parents=True, exist_ok=True)

    for important_file in path.rglob('*.py'):
        shutil.copy(important_file, backup_path / important_file.name)
        print(f'Backed up {important_file} to {backup_path}')

back_up_files('new_project', 'backup')
