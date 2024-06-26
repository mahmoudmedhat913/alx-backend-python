#!/usr/bin/env python3
"""module for function"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function add two number"""
    return [(i, len(i)) for i in lst]
