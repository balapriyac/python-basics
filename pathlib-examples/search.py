# search.py
from pathlib import Path

# globbing
def search_and_process_text_files(directory):
    path = Path(directory)
    path = path.resolve()
    for text_file in path.glob('*.txt'):
    # process text files as needed
        print(f'Processing {text_file}...')
        print(text_file.read_text())

search_and_process_text_files('new_project')
