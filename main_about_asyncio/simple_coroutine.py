"""Simple coroutine"""
import asyncio

from main_about_asyncio.util.delay_functions import delay


async def add_one(number: int) -> int:
    """add one to given number"""
    return number + 1


async def hello_world_message() -> str:
    """return message after async sleep"""
    await delay(1)
    return 'Hello World!'


async def main() -> None:
    """first coroutine call and wait inner coroutine"""
    message = await hello_world_message()
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(message)


if __name__ == '__main__':
    asyncio.run(main())
