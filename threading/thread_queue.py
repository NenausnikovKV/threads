"""thread safe queue"""

import time
from queue import Empty, Queue
from threading import Thread


def produce_queue(queue):
    """Добавляем элементы в потокобезопасную очередь"""
    for i in range(1, 6):
        print(f'Вставляем элемент {i} в очередь')
        time.sleep(1)
        queue.put(i)


def get_from_queue(queue):
    """Извлекаем элементы из потокобезопасной очереди"""
    while True:
        try:
            item = queue.get()
        except Empty:
            continue
        else:
            print(f'Обрабатываем элемент {item}')
            time.sleep(2)
            queue.task_done()


def queue_process():
    """Создаем очередь и извлекаем элементы из очереди в двух потоках"""
    queue = Queue()
    # создаем поток-производитель и запускаем его
    producer_thread = Thread(
        target=produce_queue,
        args=(queue,)
    )
    producer_thread.start()
    # создаем поток-потребитель и запускаем его
    consumer_thread = Thread(
        target=get_from_queue,
        args=(queue,),
        daemon=True
    )
    consumer_thread.start()
    # дожидаемся, пока все задачи добавятся в очередь
    producer_thread.join()
    # дожидаемся, пока все задачи в очереди будут завершены
    queue.join()


if __name__ == '__main__':
    queue_process()
