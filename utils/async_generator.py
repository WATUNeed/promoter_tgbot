import asyncio
from typing import Any


async def async_generator(iterable: list | tuple | frozenset | set, sleep_sec: int | float) -> Any:
    """
    Creates an asynchronous generator and outputs a value with a delay between iterations.
    :param iterable: Collection for iterations
    :param sleep_sec: Delay in seconds between iterations
    :return:
    """
    for item in iterable:
        yield item
        await asyncio.sleep(sleep_sec)
