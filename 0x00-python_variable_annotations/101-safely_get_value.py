#!/usr/bin/env python3
"""Using generic type (typevar)"""
from typing import Mapping
from typing import Any
from typing import Union
from typing import TypeVar
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,  key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """A function that returns a value in a dictionary."""
    if key in dct:
        return dct[key]
    else:
        return default
