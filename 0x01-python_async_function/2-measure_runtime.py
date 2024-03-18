#!/usr/bin/env python3
"""A Program that measures the time of an asynchronous operation."""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 0) -> float:
    """ A function that measures the time of execution of a coroutine."""
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    execution_time = time.perf_counter() - start_time
    return execution_time / n
