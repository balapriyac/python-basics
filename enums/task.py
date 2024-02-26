from enum import Enum

class TaskState(Enum):
    TODO = 0
    IN_PROGRESS = 1
    DONE = 2
    ABANDONED = -1


class Task:
    def __init__(self, name, state):
        self.name = name
        self.state = state
    
    def update_state(self, new_state):
        # Define valid state transitions based on the current state
        valid_transitions = {
            TaskState.TODO: [TaskState.IN_PROGRESS, TaskState.ABANDONED],
            TaskState.IN_PROGRESS: [TaskState.DONE, TaskState.ABANDONED],
            TaskState.DONE: [],
            TaskState.ABANDONED: []
        }
        
        # Check if the new state is a valid transition from the current state
        if new_state in valid_transitions[self.state]:
            self.state = new_state
        else:
            raise ValueError(f"Invalid state transition from {self.state.name} to {new_state.name}")


# Create a new task with the initial state "To Do"
task = Task("Write Report", TaskState.TODO)

# Print the task details
print(f"Task Name: {task.name}")
print(f"Current State: {task.state.name}")

# Update the task state to "In Progress"
task.update_state(TaskState.IN_PROGRESS)
print(f"Updated State: {task.state.name}")

# Attempt to update the task state to an invalid state
# task.update_state(TaskState.TODO) # uncomment to see if exception handling works!


# Update the task state to "Completed"
task.update_state(TaskState.DONE)
print(f"Updated State: {task.state.name}")
