import queue
import random
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Thread

counter = 0
job_queue = queue.Queue()


def increment_manager():
    global counter

    while True:
        increment = job_queue.get()  # This waits until an item is available adn locks the queue
        time.sleep(random.random())
        old_counter = counter
        counter = old_counter + increment
        time.sleep(random.random())
        print(f"New counter value {counter}")
        time.sleep(random.random())
        job_queue.task_done()  # this unlock the queue


# printer_manager and increment_manager run continuously because of the `daemon` flag
Thread(target=increment_manager, daemon=True).start()


def increment_counter():
    job_queue.put(1)
    time.sleep(random.random())


executor = ThreadPoolExecutor(max_workers=25)
for x in range(10):
    _ = executor.submit(increment_counter)


job_queue.join()  # wait for counter_queue to be empty
