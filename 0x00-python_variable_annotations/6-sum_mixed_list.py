#!/usr/bin/env python3
"""A program that uses an annotated function to sum of a list."""
from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """A function that sums up a list of integers and floats.
        ARGS: mxd_lst - the list to be summed
        RETURN: The result of the sum (a float) is returned
    """
    return sum(mxd_lst)
