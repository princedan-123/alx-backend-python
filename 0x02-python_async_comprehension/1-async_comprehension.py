#!/usr/bin/env python3
"""A programs that implements asynchronous comprehension."""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A function that uses asynchronous comprehension to create
    a list of floats.
    Args: no arguments.
    Return: A list of floats
    """
    numbers = [number async for number in async_generator()]
    return numbers
