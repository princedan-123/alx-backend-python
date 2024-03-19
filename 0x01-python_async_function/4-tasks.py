#!/usr/bin/env python3
"""Alters another coroutine to use the instance of Task class."""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 0) -> List[float]:
    """An asycn function that implements another async function
    Args: n (int) a number that indicates the number of times
    to implement wait_random function
    max_delay (int) the duration for the wait_random funcion
    to slep
    Return: a list is returned
    """
    calls = [task_wait_random(max_delay) for i in range(0, n)]
    result = await asyncio.gather(*calls)
    return sorted(result)
