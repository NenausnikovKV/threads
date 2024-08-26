"""exception processing"""
import concurrent.futures as pool
import time


def worker():
    """thread method"""
    time.sleep(1)
    raise ValueError('WORKER: Подняли ValueError!')


if __name__ == '__main__':
    with pool.ThreadPoolExecutor(max_workers=2) as executor:
        print('Старт потоков')
        future = executor.submit(worker)
        error = future.exception()
        print(error)
    # обрабатываем исключение
    try:
        result = future.result()
    except ValueError as exc:
        print(f'Поймали ошибку "{exc}" при получении результата')
