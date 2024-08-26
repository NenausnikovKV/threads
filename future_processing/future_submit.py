"""simple thread executor submit example"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import random
import threading
import time


def thread_method(item_1, item_2):
    """Method for executor submit researching"""
    s = item_1 + item_2 / 10
    time.sleep(random.randint(0, 1))
    thread_name = threading.current_thread().name
    print(f"{thread_name} running")
    return s


if __name__ == '__main__':
    with ThreadPoolExecutor() as executor:
        data = [(1, 1), (2, 2), (3, 3), (4, 4)]
        futures = [executor.submit(thread_method, data_item_2, data_item_1) for data_item_1, data_item_2 in data]
        for complete_future in as_completed(futures):
            result = complete_future.result()
            print(f"result is {result}")
