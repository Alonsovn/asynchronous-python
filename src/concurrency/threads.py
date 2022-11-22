import time
from threading import Thread


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


def run_in_main_thread():
    start_time = time.time()

    ask_user()
    complex_calculation()

    end_time = time.time()
    print(f"Single thread total time: {end_time - start_time}")


def run_with_threads():
    # Note: Use threads to reduce waiting time. when you have user inputs, when you have a blocking operation
    # Not use thread when you need CPU, not complex operations
    start_time = time.time()
    thread1 = Thread(target=complex_calculation)
    thread2 = Thread(target=ask_user)

    # Trigger threads executions
    thread1.start()
    thread2.start()

    # Wait for threads executions completions
    thread1.join()
    thread2.join()

    end_time = time.time()
    print(f"Two threads total time: {end_time - start_time}")


def run_complex_operations_with_threads():
    # This approach will increase the processing time, because the threads are fighting for CPU time,
    # probably double the time, the OS has to switch CPU time for each thread
    start_time = time.time()
    thread1 = Thread(target=complex_calculation)
    thread2 = Thread(target=complex_calculation)

    # Trigger threads executions
    thread1.start()
    thread2.start()

    # Wait for threads executions completions
    thread1.join()
    thread2.join()

    end_time = time.time()
    print(f"Two threads total time: {end_time - start_time}")


def run_complex_operations_in_main_thread():
    start_time = time.time()
    complex_calculation()
    complex_calculation()

    end_time = time.time()
    print(f"Two threads total time: {end_time - start_time}")


def user_menu():
    menu = """\nSelect you option:
    1: Run in main thread
    2: Run with two threads
    3: Run complex operation with threads
    4: Run complex operations in main thread
    5: Exit
    \n
    """
    user_option = int(input(menu))

    return user_option


def main():
    user_option = user_menu()

    while user_option != 5:
        if user_option == 1:
            run_in_main_thread()
        elif user_option == 2:
            run_with_threads()
        elif user_option == 3:
            run_complex_operations_with_threads()
        elif user_option == 4:
            run_complex_operations_in_main_thread()
        elif user_option == 5:
            break
        else:
            print("Your option is not valid, try again!")

        user_option = user_menu()


if __name__ == '__main__':
    main()
