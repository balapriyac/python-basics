from fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("TaskTracker")

# Simple in-memory task storage
tasks = []
task_id_counter = 1

@mcp.tool()
def add_task(title: str, description: str = "") -> dict:
    """Add a new task to the task list"""
    global task_id_counter
    
    task = {
        "id": task_id_counter,
        "title": title,
        "description": description,
        "status": "pending",
        "created_at": datetime.now().isoformat()
    }
    
    tasks.append(task)
    task_id_counter += 1
    
    return task

@mcp.tool()
def complete_task(task_id: int) -> dict:
    """Mark a task as completed"""
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "completed"
            task["completed_at"] = datetime.now().isoformat()
            return task
    
    return {"error": f"Task {task_id} not found"}

@mcp.tool()
def delete_task(task_id: int) -> dict:
    """Delete a task from the list"""
    global tasks
    
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted_task = tasks.pop(i)
            return {"success": True, "deleted": deleted_task}
    
    return {"success": False, "error": f"Task {task_id} not found"}

@mcp.resource("tasks://all")
def get_all_tasks() -> str:
    """Get all tasks as formatted text"""
    if not tasks:
        return "No tasks found"
    
    result = "Current Tasks:\n\n"
    for task in tasks:
        status_emoji = "✅" if task["status"] == "completed" else "⏳"
        result += f"{status_emoji} [{task['id']}] {task['title']}\n"
        if task["description"]:
            result += f"   Description: {task['description']}\n"
        result += f"   Status: {task['status']}\n"
        result += f"   Created: {task['created_at']}\n\n"
    
    return result

@mcp.resource("tasks://pending")
def get_pending_tasks() -> str:
    """Get only pending tasks"""
    pending = [t for t in tasks if t["status"] == "pending"]
    
    if not pending:
        return "No pending tasks! 🎉"
    
    result = "Pending Tasks:\n\n"
    for task in pending:
        result += f"⏳ [{task['id']}] {task['title']}\n"
        if task["description"]:
            result += f"   {task['description']}\n"
        result += "\n"
    
    return result

@mcp.prompt()
def task_summary_prompt() -> str:
    """Generate a prompt for summarizing tasks"""
    return """Please analyze the current task list and provide:

1. Total number of tasks (completed vs pending)
2. Any overdue or high-priority items
3. Suggested next actions
4. Overall progress assessment

Use the tasks://all resource to access the complete task list."""

if __name__ == "__main__":
    mcp.run()

