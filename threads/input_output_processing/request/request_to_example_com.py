"""multithread request research"""

import time
import threading
import requests


class SiteRequest:
    """single or multithread request to given site"""
    def __init__(self, url='https://www.example.com'):
        self.url = url

    def _read_example(self) -> None:
        """Request to example.com and print response status code"""
        response = requests.get(self.url, timeout=1)
        print(response.status_code)

    def multi_thread_processing(self, thread_num=2):
        """Two thread request to site"""
        threads = []
        for _ in range(thread_num):
            threads.append(threading.Thread(target=self._read_example))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    def single_thread_processing(self, request_count=2):
        """One thread request to site"""
        for _ in range(request_count):
            self._read_example()


if __name__ == '__main__':
    site_request = SiteRequest()
    # single
    single_start = time.time()
    site_request.single_thread_processing()
    single_end = time.time()
    print(f"Однопоточное выполнение заняло {single_end-single_start:.4f} с.")
    # multi
    thread_start = time.time()
    site_request.multi_thread_processing(2)
    thread_end = time.time()
    print(f'Многопоточное выполнение заняло {thread_end - thread_start:.4f} с.')
