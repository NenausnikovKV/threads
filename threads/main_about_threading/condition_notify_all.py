"""
SuperFastPython.com
example of wait/notify_all with a condition
"""
from time import sleep
from random import random
from threading import Thread
from threading import Condition


def task(condition, number):
    """Processing only after condition notify"""
    # wait to be notified
    print(f'Thread {number} waiting...')
    with condition:
        condition.wait()
    value = random()
    sleep(value)
    print(f'Thread {number} got {value}')


def main():
    """main thread"""
    condition = Condition()
    for i in range(5):
        worker = Thread(target=task, args=(condition, i))
        worker.start()
    sleep(8)
    with condition:
        condition.notify_all()


if __name__ == '__main__':
    main()
