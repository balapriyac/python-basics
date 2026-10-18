#!/usr/bin/env python3
"""
todo_cli.py

A small command-line to-do list manager. Tasks persist between runs in a
local JSON file, so your list is right where you left it. Built with
argparse subcommands as a beginner-friendly example of a CLI tool.

Usage:
    python 04_todo_cli.py add "Write the quarterly report"
    python 04_todo_cli.py list
    python 04_todo_cli.py list --all
    python 04_todo_cli.py done 2
    python 04_todo_cli.py remove 2
"""

import argparse
import json
from datetime import datetime
from pathlib import Path

DEFAULT_STORE = Path.home() / ".todo_cli.json"


def load_tasks(store_path):
    if not store_path.exists():
        return []
    with open(store_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks, store_path):
    with open(store_path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def cmd_add(args, store_path):
    tasks = load_tasks(store_path)
    task = {
        "id": (max((t["id"] for t in tasks), default=0) + 1),
        "description": args.description,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    tasks.append(task)
    save_tasks(tasks, store_path)
    print(f"Added task #{task['id']}: {task['description']}")


def cmd_list(args, store_path):
    tasks = load_tasks(store_path)
    if not args.all:
        tasks = [t for t in tasks if not t["done"]]

    if not tasks:
        print("No tasks to show." if not args.all else "No tasks yet.")
        return

    for task in tasks:
        mark = "x" if task["done"] else " "
        print(f"[{mark}] #{task['id']}  {task['description']}  (added {task['created']})")


def cmd_done(args, store_path):
    tasks = load_tasks(store_path)
    for task in tasks:
        if task["id"] == args.task_id:
            task["done"] = True
            save_tasks(tasks, store_path)
            print(f"Marked task #{args.task_id} as done.")
            return
    print(f"No task found with id {args.task_id}")


def cmd_remove(args, store_path):
    tasks = load_tasks(store_path)
    remaining = [t for t in tasks if t["id"] != args.task_id]
    if len(remaining) == len(tasks):
        print(f"No task found with id {args.task_id}")
        return
    save_tasks(remaining, store_path)
    print(f"Removed task #{args.task_id}")


def main():
    parser = argparse.ArgumentParser(description="A simple command-line to-do list.")
    parser.add_argument("--store", default=str(DEFAULT_STORE),
                         help=f"Path to the JSON file used to store tasks (default: {DEFAULT_STORE})")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Description of the task")
    add_parser.set_defaults(func=cmd_add)

    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("--all", action="store_true", help="Include completed tasks")
    list_parser.set_defaults(func=cmd_list)

    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("task_id", type=int, help="ID of the task to mark done")
    done_parser.set_defaults(func=cmd_done)

    remove_parser = subparsers.add_parser("remove", help="Remove a task")
    remove_parser.add_argument("task_id", type=int, help="ID of the task to remove")
    remove_parser.set_defaults(func=cmd_remove)

    args = parser.parse_args()
    store_path = Path(args.store)
    args.func(args, store_path)


if __name__ == "__main__":
    main()


