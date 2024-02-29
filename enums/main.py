from enum import Enum
 	 
class TaskStatus(Enum):
    TODO = 0
    IN_PROGRESS = 1
    DONE = 2
    ABANDONED = -1

print(isinstance(TaskStatus.TODO,Enum))

print(list(TaskStatus))

num_statuses = len(TaskStatus)
print(num_statuses) 

for status in TaskStatus:
    print(status.name, status.value)
