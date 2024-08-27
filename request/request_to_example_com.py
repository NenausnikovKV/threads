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

    def multi_thread_processing(self):
        """Two thread request to site"""
        thread_1 = threading.Thread(target=self._read_example)
        thread_2 = threading.Thread(target=self._read_example)
        thread_1.start()
        thread_2.start()
        thread_1.join()
        thread_2.join()

    def single_thread_processing(self):
        """One thread request to site"""
        self._read_example()
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
    site_request.multi_thread_processing()
    thread_end = time.time()
    print(f'Многопоточное выполнение заняло {thread_end - thread_start:.4f} с.')
