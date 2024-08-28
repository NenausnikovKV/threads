"""tasks with timer decorator"""
import asyncio

from main_about_asyncio.util.async_timer import async_timed
from main_about_asyncio.util.delay_functions import delay


@async_timed()
async def main():
    """timer for tasks"""
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))
    await task_one
    await task_two


if __name__ == '__main__':
    asyncio.run(main())
