#!/usr/bin/env python3
"""An asychronous coroutine that generates a list of numbers."""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 0) -> List[float]:
    """An asycn function that implements another async function
        Args: n (int) a number that indicates the number of times
              to implement wait_random function
              max_delay (int) the duration for the wait_random funcion
              to sleep.
        Return: a list is returned
    """
    calls = [wait_random(max_delay) for i in range(0, n)]
    result = await asyncio.gather(*calls)
    return sorted(result)
