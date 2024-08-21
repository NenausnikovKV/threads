"""Class inherited Thread """
import os
import threading
import time
from random import randint


class SimpleThread(threading.Thread):
    """Simple personal thread"""
    def __init__(self, name, duration):
        super().__init__(name=name)
        self.duration = duration

    def run(self):
        """Override class payload"""
        print(f"{self.name} running and belonging to process ID {os.getpid()}")
        time.sleep(self.duration)
        print("\n")
        print(f"{self.name} is complete and lasted {self.duration} seconds")


if __name__ == '__main__':
    start_time = time.time()
    threads = []
    for thread_num in range(1, 11):
        thread = SimpleThread(name=f"thread_{thread_num}", duration=randint(1, 10))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    processing_time = time.time() - start_time
    print(f"main thread was done in {processing_time} seconds")
