#!/usr/bin/env python3
"""A program that creates a tuple using an annotated function."""
from typing import Union
from typing import Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a tuple from the parameters.
        ARGS: k - string
              v - integer or float
        RETURN - A tuple of the parameters
    """
    square = v * v
    return (k, square)
