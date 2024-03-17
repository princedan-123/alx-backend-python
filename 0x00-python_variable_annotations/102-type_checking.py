#!/usr/bin/env python3
"""A program that will be validated for type annotation using mypy."""
from typing import List
from typing import Tuple


def zoom_array(
        lst: Tuple, factor: int = 2
        ) -> List[int]:
    """A function that takes a list and integer and returns a refined list."""
    zoomed_in: List[int] = [
            item for item in lst
            for i in range(factor)
            ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
