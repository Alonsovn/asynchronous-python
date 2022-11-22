import time
from concurrent.futures import ThreadPoolExecutor


def ask_user():
    start = time.time()

    user_input = input("Enter your name: ")
    greet = f"Hello, {user_input}"
    print(greet)

    end = time.time()
    print(f"ask_user, {end - start}")


def complex_calculation():
    start = time.time()
    print("Start calculating....")

    [x ** 2 for x in range(20000000)]

    end = time.time()
    print(f"complex_calculation, {end - start}")


def main():
    start_time = time.time()

# Create a pool of threads and them we can submit a task to run it
# You can have a bunch of threads waiting to execute tasks and get the result
# In this case will be 2 threads
    with ThreadPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_calculation)
        pool.submit(ask_user)

    end_time = time.time()
    print(f"Two threads total time: {end_time - start_time}")


if __name__ == '__main__':
    main()
