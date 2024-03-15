#!/usr/bin/env python3
"""An annotated function without a type."""
from typing import Any
from typing import Union
from typing import Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """A function that has been duck typed."""
    if lst:
        return lst[0]
    else:
        return None
