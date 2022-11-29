import threading
import time

def func1():
    for i in range(5):
        print(f"Running t1, print {i}.")
        time.sleep(2)

def func2():
    for i  in range(5):
         print(f"Running t2, print {i}.")
         time.sleep(1)


def func3():
    for i in range(4):
         print(f"Running t3, print {i}.")
         time.sleep(0.5)


t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)
t3 = threading.Thread(target=func3)

t1.start()
t2.start()
t3.start()
