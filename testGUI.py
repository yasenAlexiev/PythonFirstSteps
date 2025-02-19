import threading
from time import sleep

def func1():
    while True:
        sleep(1)
        print("Working1")

def func2():
    while True:
        sleep(1)
        print("Working2")

thread1 = threading.Thread(target=func1, daemon=True)
thread2 = threading.Thread(target=func2, daemon=True)

print("Starting threads...")
thread1.start()
thread2.start()
print("Threads started.")
thread1.join()
thread2.join()
print("Threads finished.")