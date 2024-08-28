"""wait processing"""
import concurrent.futures as pool
import time


def worker(a, b):
    """thread method"""
    time.sleep(0.5)
    return a / b


# данные для worker()
data = [(1, 0.3), (2, 0.7), (3, 9), (4, 3)]

# создаем пул из 3-х потоков
with pool.ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(worker, a, b) for a, b in data]
    ok = pool.wait(futures)
    for future in ok.done:
        result = future.result()
        print(f'Результат {result}')
