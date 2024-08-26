"""Simple multiprocessing"""
import multiprocessing
import time


def task(n=100_000_000):
    """CPU task"""
    while n:
        n -= 1


if __name__ == '__main__':
    start = time.perf_counter()
    task()
    task()
    finish = time.perf_counter()
    print(f'Выполнение одним процессом заняло {finish-start: .2f} секунд.')

    start = time.perf_counter()

    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    finish = time.perf_counter()
    print(f'Выполнение двумя процессами заняло {finish-start: .2f} секунд.')
