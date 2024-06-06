#!/usr/bin/env python3
"""module for function"""
from typing import Union, Any, Mapping, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """function add two number"""
    if key in dct:
        return dct[key]
    else:
        return default
