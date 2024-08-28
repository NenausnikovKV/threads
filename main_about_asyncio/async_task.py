"""async tasks"""
import asyncio

from main_about_asyncio.util.delay_functions import delay


async def hello_every_second():
    """print messages every second"""
    for _ in range(4):
        await asyncio.sleep(1)
        print("пока я жду, исполняется другой код!")


async def main():
    """create async task and do something else at the same time"""
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))
    await hello_every_second()
    await sleep_for_three
    await sleep_again
    await sleep_once_more
    print("finish main")


if __name__ == '__main__':
    asyncio.run(main())
