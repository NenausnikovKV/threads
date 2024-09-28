"""
Simple context manager class example
"""
import time


class Greeting:
    """class for context manager"""
    def __enter__(self):
        print("hello")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("goodbye")


if __name__ == '__main__':
    with Greeting() as timer:
        print("sleep for 2 seconds")
        time.sleep(2)
