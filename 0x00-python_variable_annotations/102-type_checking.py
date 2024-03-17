#!/usr/bin/env python3
"""A program that will be validated for type annotation using mypy."""
from typing import Sequence
from typing import Union


def zoom_array(
        lst: Sequence[Union[int, float]], factor: int = 2
        ) -> Sequence[Union[int, float]]:
    """A function that takes a list and integer and returns a refined list."""
    zoomed_in: Sequence[Union[int, float]] = [
            item for item in lst
            for i in range(factor)
            ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
