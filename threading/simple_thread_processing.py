"""Simple thread processing"""


import threading


def print_thread_number(thread_number):
    """Print sentence with thread number"""
    print(f"this function is called by thread num.{thread_number}")


def print_thread_name():
    """print current thread name"""
    print(f"This function is called by {threading.current_thread().name}")


def consistent_thread_processing():
    """Run some simple thread consistently"""
    threads = []
    for thread_num in range(10):
        thread = threading.Thread(target=print_thread_number, args=(thread_num, ))
        threads.append(thread)
        # start thread processing
        thread.start()
        # wait thread processing
        thread.join()


def parallel_thread_processing():
    """Run some simple thread parallel"""
    threads = []
    for thread_num in range(10):
        thread = threading.Thread(target=print_thread_name)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    consistent_thread_processing()
    parallel_thread_processing()
