"""
SuperFastPython.com
example of wait_for with a condition
"""
from time import sleep
from random import random
from threading import Thread
from threading import Condition


def task(condition, work_list):
    """finish after condition wait is realized"""
    with condition:
        value = random()
        sleep(value)
        work_list.append(value)
        print(f'Thread added {value}')
        condition.notify()


def main():
    """Main function"""
    condition = Condition()
    work_list = []
    for _ in range(5):
        worker = Thread(target=task, args=(condition, work_list))
        worker.start()
    with condition:
        condition.wait_for(lambda: len(work_list) == 5)
        # example of waiting without condition
        # condition.wait() or condition.wait(timeout=2)
        print(f'Done, got: {work_list}')


if __name__ == '__main__':
    main()
