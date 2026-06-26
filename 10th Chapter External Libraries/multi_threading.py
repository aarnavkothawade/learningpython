import threading
import time

def worker(num, x):
    print(f"Thread {num} : Starting\n")
    time.sleep(x+0.5) 
    print(f"Thread {num} : Finishing\n")

threads = []

for i in range(3):
    thread = threading.Thread(target = worker, args = (i, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All Threads Completed!")