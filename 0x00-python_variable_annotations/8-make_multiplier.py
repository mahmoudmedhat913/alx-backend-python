#!/usr/bin/env python3
"""module for function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function add two number"""
    def multiply(n: float) -> float:
        """function to multiply float"""
        return n * multiplier
    return multiply
