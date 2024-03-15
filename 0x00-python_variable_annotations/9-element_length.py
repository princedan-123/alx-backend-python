#!/usr/bin/env python3
"""Using duck typing to annotate a function."""
from typing import Sequence
from typing import Iterable
from typing import Tuple
from typing import List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
