""" debug mode """
import asyncio

from main_about_asyncio.util.async_timer import async_timed


@async_timed()
async def cpu_bound_work() -> int:
    """cpu hungry"""
    counter = 0
    for _ in range(100000000):
        counter = counter + 1
    return counter


async def main() -> None:
    """create task"""
    task_one = asyncio.create_task(cpu_bound_work())
    await task_one


if __name__ == '__main__':
    asyncio.run(main(), debug=True)
