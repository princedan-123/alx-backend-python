#!/usr/bin/env python3
"""A program that creates a Task Class."""
from typing import Any
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """A function that creates a Task class for wait_random coroutine."""
    return asyncio.create_task(wait_random(max_delay))
