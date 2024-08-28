"""async delay function"""

import asyncio


async def delay(delay_seconds: int) -> int:
    """
    Async delay function.
    Print given time and sleep for that seconds.
    Return given time.
    """
    print(f"sleep for {delay_seconds} seconds")
    await asyncio.sleep(delay_seconds)
    print(f"dream during {delay_seconds} has finished")
    return delay_seconds
