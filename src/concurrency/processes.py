import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process


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


def use_processes():
    # Use Processes if you have multiple core machine and you want to do complex calculations
    process = Process(target=complex_calculation)
    process2 = Process(target=complex_calculation)
    start_time = time.time()

    process.start()
    process2.start()

    process.join()
    process2.join()

    end_time = time.time()
    print(f"Two threads total time: {end_time - start_time}")


def use_processes_pool_executor():
    # Use Processes if you have multiple core machine and you want to do complex calculations
    # This is a simpler code to use processes
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_calculation)
        pool.submit(complex_calculation)

    end_time = time.time()
    print(f"Two threads total time: {end_time - start_time}")


def main():
    use_processes()
    print("---------\n")
    use_processes_pool_executor()


if __name__ == '__main__':
    main()
