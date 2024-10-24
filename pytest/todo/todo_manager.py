# todo/todo_manager.py
class ToDoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task:
            raise ValueError("Task cannot be empty.")
        self.tasks.append({"task": task, "completed": False})
        return task

    def remove_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                return task
        raise ValueError("Task not found.")

    def mark_completed(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                return task
        raise ValueError("Task not found.")
    
    def get_tasks(self, completed=None):
        if completed is None:
            return self.tasks
        return [t for t in self.tasks if t["completed"] == completed]
