import random
import time
from threading import Thread

counter = 0


def increment_counter():
    global counter
    time.sleep(random.randint(0, 2))
    counter += 1
    time.sleep(random.randint(0, 2))
    print(f'New counter value: {counter}')
    time.sleep(random.randint(0, 2))
    print('--------')


def main():
    # This exercise will show the issue with the threads, some of them will increment the counter with old value
    # New counter value: 1
    # --------
    # New counter value: 4
    # --------
    # New counter value: 4
    # New counter value: 4
    # --------
    # --------
    # New counter value: 6
    # To fix that issue, check the code in queued_thread.py file
    for x in range(10):
        t = Thread(target=increment_counter)
        time.sleep(random.randint(0, 2))
        t.start()


if __name__ == '__main__':
    main()
