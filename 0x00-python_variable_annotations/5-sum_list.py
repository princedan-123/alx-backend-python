#!/usr/bin/env python3
"""A programs that defines an annotated function
   which sums up a list of floats.
"""


def sum_list(input_list: list[float]) -> float:
    """A function that sums up a list of float
        ARGS: input_list - A list of float to be summed up
        RETURN: The result of the sum is returned
    """
    return sum(input_list)
