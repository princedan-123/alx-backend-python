#!/usr/bin/env python3
"""A program that creates an asynchronous generator."""
import random
from typing import AsyncGenerator
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """
        A function that yields random floats.
        Args: no arguments
        Return: it returns a generator object
    """
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
