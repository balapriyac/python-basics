from enum import Enum
 	 
class TaskStatus(Enum):
    TODO = 0
    IN_PROGRESS = 1
    DONE = 2
    ABANDONED = -1


print(list(TaskStatus))

for status in TaskStatus:
    print(status.name, status.value)
