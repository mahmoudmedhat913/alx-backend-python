#!/usr/bin/env python3
"""module for function"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """function add two number"""
    if lst:
        return lst[0]
    else:
        return None
