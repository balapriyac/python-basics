# Beginner-Friendly Python Automation Scripts

Five short, self-contained scripts that automate everyday tasks — spanning image processing, file handling, text analysis, and the command line. 

## Requirements

- Python 3.11+
- Script 1 requires **Pillow**: `pip install Pillow`
- Scripts 2–5 use only the Python standard library 

## Scripts

| # | Script | Category | What it does |
|---|--------|----------|---------------|
| 1 | `image_resizer_watermarker.py` | Image | Batch-resizes images to a max size and stamps a text watermark on each one. |
| 2 | `bulk_file_renamer.py` | File | Renames a batch of files by prefix, suffix, sequence, or find/replace. Dry-run by default. |
| 3 | `text_word_frequency_analyzer.py` | Text | Reports word/sentence counts, top words, and estimated reading time for a text file. |
| 4 | `todo_cli.py` | Command-line | A persistent to-do list you manage entirely from the terminal. |
| 5 | `log_file_analyzer.py` | Text / CLI | Filters a log file by level, keyword, or date and summarizes the matches. |


## Quick Start

```bash
# 1. Resize and watermark a folder of images
pip install Pillow
python scripts/01_image_resizer_watermarker.py photos/ photos_out/ \
    --max-size 1200 --watermark "(c) My Studio" --position bottom-right

# 2. Preview a bulk rename, then apply it
python scripts/02_bulk_file_renamer.py photos/ --mode sequence --value "photo_"
python scripts/02_bulk_file_renamer.py photos/ --mode sequence --value "photo_" --apply

# 3. Analyze a text file
python scripts/03_text_word_frequency_analyzer.py essay.txt --top 15

# 4. Manage a to-do list from the terminal
python scripts/04_todo_cli.py add "Write the quarterly report"
python scripts/04_todo_cli.py list
python scripts/04_todo_cli.py done 1

# 5. Filter and summarize a log file
python scripts/05_log_file_analyzer.py app.log --level ERROR --since 2026-09-20
```

Each script also supports `-h` / `--help` for the full list of options.

## Notes

- **Script 1** skips files it can't open (e.g. corrupted images or unsupported formats) rather than stopping the whole batch, and never modifies your original files — output always goes to a separate folder.
- **Script 2** always shows a dry-run preview first; nothing is renamed until you pass `--apply`. It also refuses to proceed if the rename would create filename collisions.
- **Script 3** expects a plain `.txt` file. It uses a small built-in stop-word list to keep the "top words" list meaningful rather than dominated by "the", "and", etc.
- **Script 4** stores tasks as plain JSON at `~/.todo_cli.json` by default (override with `--store`), so the file is easy to inspect, back up, or sync yourself.
- **Script 5** expects log lines in the form `YYYY-MM-DD HH:MM:SS LEVEL message...`. Lines that don't match this format are skipped and counted separately rather than causing an error — adjust the regular expression at the top of the script if your logs use a different format.

