from enum import Enum, auto

class TaskStatus(Enum):
    TODO = auto()
    IN_PROGRESS = auto()
    DONE = auto()
    ABANDONED = auto()


print(list(TaskStatus))

