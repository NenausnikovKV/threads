"""
Sum of unit over one or two threads.
"""
import threading
import time


class OneSum:
    """Sum of unit over one or two threads """
    def __init__(self, num):
        self.number = num

    def one_thread_sum(self):
        """Get sum number using main thread"""
        self._sum_one(0, self.number)

    def two_thread_sum(self):
        """Get sum number using two threads"""
        first_part_num = self.number
        second_part_num = self.number
        thread_1 = threading.Thread(target=self._sum_one, args=(0, first_part_num))
        thread_2 = threading.Thread(target=self._sum_one, args=(first_part_num, second_part_num))
        thread_1.start()
        thread_2.start()
        thread_1.join()
        thread_2.join()

    @staticmethod
    def _sum_one(start, stop):
        sum_num = 0
        for _ in range(start, stop):
            sum_num += 1


if __name__ == '__main__':
    one_sum = OneSum(100000000)
    start_time = time.perf_counter()
    one_sum.one_thread_sum()
    end_time = time.perf_counter()
    print(f"One thread processing time is {end_time - start_time:0.2f} seconds")
    start_time = time.perf_counter()
    one_sum.two_thread_sum()
    end_time = time.perf_counter()
    print(f"two threads processing time is {end_time - start_time:0.2f} seconds")
