#!/usr/bin/python3 env
"""A program that creates a tuple using an annotated function."""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, Union[int, float]]:
    """Creates a tuple from the parameters.
        ARGS: k - string
              v - integer or float
        RETURN - A tuple of the parameters
    """
    return (k, v)
