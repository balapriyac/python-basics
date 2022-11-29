import time

def count_down(n):
    for i in range(n,-1,-1):
        if i==0:
            print("Ready to go!")
        else:
             print(i)
             time.sleep(1)

count_down(5)
