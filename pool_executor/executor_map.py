"""simple thread executor map example"""

import concurrent.futures as pool
import random
import threading
import time


def thread_processing_method(n):
    """Sleep and return simple math result"""
    # имя конкретного рабочего потока
    th_name = threading.current_thread().name
    print(f'{th_name}: обработка данных => {n}')
    result = n / 10
    sleep_time = random.randint(1, 2)
    time.sleep(sleep_time)
    print(f'{th_name}: обработка закончена => {n}')
    return result


def main():
    """main thread"""
    main_thread_name = threading.current_thread().name
    print(f'{main_thread_name}: запущен...')
    # создаем и запускаем пул из 3 потоков
    with pool.ThreadPoolExecutor(max_workers=3) as thread_executor:
        data = [1, 3, 5, 7, 9]
        results = thread_executor.map(thread_processing_method, data)
    # results variable is iterator
    result_list = list(results)
    print(f'{main_thread_name}: результаты => {result_list}')


if __name__ == '__main__':
    main()
