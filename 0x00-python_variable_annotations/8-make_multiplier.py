#!/usr/bin/env python3
"""A program that creates a function to return a multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A function that returns another function that multipliers a
      float when called
      ARGS: multiplier - float
      RETURN: A callable
    """
    return lambda x: x * multiplier
