# tests/test_todo_manager.py
import pytest
from todo.todo_manager import ToDoManager

@pytest.fixture
def todo_manager():
    return ToDoManager()

def test_add_task(todo_manager):
    todo_manager.add_task("Buy groceries")
    assert todo_manager.tasks == [{"task": "Buy groceries", "completed": False}]

def test_add_empty_task(todo_manager):
    with pytest.raises(ValueError, match="Task cannot be empty."):
        todo_manager.add_task("")

def test_remove_task(todo_manager):
    todo_manager.add_task("Buy groceries")
    todo_manager.remove_task("Buy groceries")
    assert todo_manager.tasks == []

def test_remove_nonexistent_task(todo_manager):
    with pytest.raises(ValueError, match="Task not found."):
        todo_manager.remove_task("Do laundry")

def test_mark_completed(todo_manager):
    todo_manager.add_task("Go for a walk")
    todo_manager.mark_completed("Go for a walk")
    assert todo_manager.tasks == [{"task": "Go for a walk", "completed": True}]

def test_get_tasks(todo_manager):
    todo_manager.add_task("Task 1")
    todo_manager.add_task("Task 2")
    todo_manager.mark_completed("Task 1")
    
    all_tasks = todo_manager.get_tasks()
    completed_tasks = todo_manager.get_tasks(completed=True)
    pending_tasks = todo_manager.get_tasks(completed=False)
    
    assert len(all_tasks) == 2
    assert completed_tasks == [{"task": "Task 1", "completed": True}]
    assert pending_tasks == [{"task": "Task 2", "completed": False}]
