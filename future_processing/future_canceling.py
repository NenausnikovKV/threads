"""future canceling research"""

import concurrent.futures as pool
import time
from concurrent.futures import CancelledError


def method(item):
    """simple arithmetic and sleeping"""
    a, b = item
    time.sleep(0.1)
    return a / b


# функция обратного вызова, принимает
# только один аргумент - объект 'Future'
def done(finished_future):
    """todo"""
    # с помощью атрибута мы
    # передали еще 2 аргумента
    a, b = finished_future.attribute
    action = f'{a} / {b}'
    # теперь методами объекта 'Future'
    # проверяем его состояние и в зависимости, что
    # они возвращают, определяем что дальше делать
    if finished_future.cancelled():
        print(f'DONE: Действие {action} отменено.')
    elif finished_future.done():
        error = finished_future.exception()
        if error:
            print(f'DONE: Действие {action} вызвало ошибку: {error}!')
        else:
            print(f'DONE: Действие {action} = {finished_future.result()}')


def main():
    """main thread"""
    # данные для worker()
    data = [(1, 0), (2, 1), (5, 2), (10, 3)]
    # создаем пул из 2-х потоков
    with pool.ThreadPoolExecutor(max_workers=2) as executor:
        # создаем список объектов 'Future' вызовами `executor.submit()`
        # (вызовы worker() с аргументами из data)
        futures = [executor.submit(method, item) for item in data]
        # проходимся по объектам 'Future',
        # что бы управлять вызовами
        for i, future in enumerate(futures):
            # отменяем вызов с данными (10, 3)
            if data[i][0] == 10:
                future.cancel()
                # В Python, у объектов можно создавать атрибуты на лету
            # в учебных целях создадим на лету атрибуты у всех объекта
            # 'Future', что бы потом использовать их в функции done()
            future.attribute = data[i]
            # добавляем функцию обратного
            # вызова done() к каждому 'Future'
            future.add_done_callback(done)
        # ждем результатов
        for completed_future in pool.as_completed(futures):
            try:
                # если нет исключения или вызов не отменен
                if completed_future.result():
                    # получаем результат
                    result = completed_future.result()
                else:
                    result = "no result"
            except (CancelledError, ZeroDivisionError):
                pass
            else:
                print(f'Полученный результат {result}')


if __name__ == '__main__':
    main()
