#!/usr/bin/env python3
"""module for function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function add two number"""
    return (k, float(v ** 2))
