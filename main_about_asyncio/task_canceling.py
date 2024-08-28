"""Cancel task"""
import asyncio

from main_about_asyncio.util.delay_functions import delay


async def create_and_cancel_task():
    """create and cancel task"""
    long_task = asyncio.create_task(delay(10))
    seconds_elapsed = 0
    while not long_task.done():
        print('Задача не закончилась, следующая проверка через секунду.')
        await asyncio.sleep(1)
        seconds_elapsed = seconds_elapsed + 1
        if seconds_elapsed == 5:
            print('Снимаем долгую задачу')
            long_task.cancel()
    try:
        await long_task
    except asyncio.CancelledError:
        print('Наша задача была снята')


async def create_task_with_timeout():
    """create task with timeout"""
    delay_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Тайм-аут!')
        print(f'Задача была снята? {delay_task.cancelled()}')


async def task_with_timeout_and_shield():
    """
    task with timeout and shield
    create task and wait timeout for task with shield
    raise exception do not interrupt task
    """
    task = asyncio.create_task(delay(5))
    try:
        # add shield to task
        result = await asyncio.wait_for(asyncio.shield(task), 2)
        print(result)
    except TimeoutError:
        print("Задача заняла более 2 с, скоро она закончится!")
        result = await task
        print(f"Задача завершена с результатом {result}")


if __name__ == '__main__':
    asyncio.run(create_and_cancel_task())
    print()
    asyncio.run(create_task_with_timeout())
    print()
    asyncio.run(task_with_timeout_and_shield())
