"""Threads with sleep"""


from time import sleep, perf_counter
from threading import Thread


def task():
    """function having sleep method"""
    print('Начинаем выполнение задачи...')
    sleep(1)
    print('Выполнено')


if __name__ == '__main__':
    start_time = perf_counter()
    # create 2 thread
    t1 = Thread(target=task)
    t2 = Thread(target=task)
    # start threads
    t1.start()
    t2.start()
    # wait threads finish
    t1.join()
    t2.join()
    end_time = perf_counter()
    print(f'Выполнение заняло {end_time- start_time: 0.2f} секунд.')
