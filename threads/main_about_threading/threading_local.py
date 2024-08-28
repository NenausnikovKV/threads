"""main_about_threading local"""


import threading
import random


def show_value(data):
    """print value attribute of given data"""
    name_thread = threading.current_thread().name
    try:
        val = data.value
    except AttributeError:
        print(f'{name_thread}: Нет локального значения value')
    else:
        print(f'{name_thread}: value={val}')


def worker(data):
    """
    Worker with local data value.
    Data is main_about_threading.local.
    """
    name_thread = threading.current_thread().name
    show_value(data)
    print(f'Установка значения value для потока {name_thread}.')
    data.value = random.randint(1, 100)
    show_value(data)


if __name__ == '__main__':
    local_data = threading.local()
    show_value(local_data)
    # set value for main thread
    local_data.value = 1000
    show_value(local_data)
    for i in range(2):
        t = threading.Thread(target=worker, args=(local_data,))
        t.start()
