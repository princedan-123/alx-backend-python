#!/usr/bin/env python3
"""An asynchronous couroutine that waits and returns an integer."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """An asychronous function that returns an integer."""
    time: float = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
