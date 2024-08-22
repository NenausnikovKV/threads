"""Контроль ресурса за счет блокировки"""

import threading
import time


class Counter:
    """Счетчик блокировок"""
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        """
        Увеличить счетчик блокировок.
        При изменении значения блокировать доступ к ресурсу.
        """
        th_name = threading.current_thread().name
        print(f'Th: {th_name} - ждет блокировку')
        # pylint: disable-next=consider-using-with
        self.lock.acquire()
        try:
            print(f'Th: {th_name} - получил блокировку')
            self.value = self.value + 1
        finally:
            print(f'Th: {th_name} - отпускает блокировку')
            self.lock.release()


def increment_counter(counter):
    """Pause and increment counter"""
    current_thread_name = threading.current_thread().name
    for _ in range(2):
        pause = 0.5
        print(f'Th: {current_thread_name} - заснул на {pause:0.02f}')
        time.sleep(pause)
        counter.increment()
    print(f'Th: {current_thread_name} - сделано.')


if __name__ == '__main__':
    lock_counter = Counter()
    for i in range(2):
        t = threading.Thread(target=increment_counter, args=(lock_counter,))
        t.start()
    for t in threading.enumerate():
        if t is not threading.main_thread():
            t.join()
    print(f'Счетчик: {lock_counter.value}')
