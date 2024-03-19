#!/usr/bin/env python3
"""Measures the time of execution of four asynchronous tasks."""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    A function that measures the execution time of four
    asynchronous tasks.
    Args: no argument
    Return: the time in float
    """
    start_time = time.perf_counter()
    await asyncio.gather(
            async_comprehension(), async_comprehension(),
            async_comprehension(), async_comprehension()
            )
    end_time = time.perf_counter() - start_time
    return end_time
