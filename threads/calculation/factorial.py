"""Check threat for"""
import time
import threading


class Factorial:
    """Calculate factorial using one or two threads"""

    def __init__(self, fact_num):
        self.fact_num = fact_num

    def one_thread_factorial(self):
        """Get factorial using one thread"""
        thread = threading.Thread(target=self._factorial)
        thread.start()
        thread.join()

    def two_factorials_by_two_threads(self):
        """Get 2 factorials using two threads"""
        thread_1 = threading.Thread(target=self._factorial)
        thread_2 = threading.Thread(target=self._factorial)
        thread_1.start()
        thread_2.start()
        thread_1.join()
        thread_2.join()

    def _factorial(self, start_num=None):
        """Calculate factorial"""
        if start_num is None:
            start_num = 1
        fact = 1
        for n in range(start_num, self.fact_num+1):
            fact *= n
        return fact


if __name__ == '__main__':
    factorial = Factorial(fact_num=100000)
    # One thread processing
    start_time = time.perf_counter()
    factorial.one_thread_factorial()
    end_time = time.perf_counter()
    print(f"One thread processing time is {end_time - start_time:0.2f} seconds")
    # Two thread and two factorials processing
    start_time = time.perf_counter()
    factorial.two_factorials_by_two_threads()
    end_time = time.perf_counter()
    print(f"Two thread processing time is {end_time - start_time:0.2f} seconds")
