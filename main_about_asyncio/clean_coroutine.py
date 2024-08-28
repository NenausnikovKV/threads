"""function and coroutine comparison"""
import asyncio


async def coroutine_add_one(number: int) -> int:
    """add one to given number"""
    return number + 1


def add_one(number: int) -> int:
    """add one to given number"""
    return number+1


def simple_call():
    """straight call function and coroutine"""
    function_result = add_one(1)
    print(f'Результат функции равен {function_result}, а его тип равен {type(function_result)}')


def async_call():
    """async circle run and call coroutine"""
    coroutine_result = asyncio.run(coroutine_add_one(1))
    print(f'Результат сопрограммы равен {coroutine_result}, а его тип равен {type(coroutine_result)}')


if __name__ == '__main__':
    simple_call()
    async_call()
