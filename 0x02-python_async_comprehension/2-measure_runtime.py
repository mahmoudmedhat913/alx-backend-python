#!/usr/bin/env python3
"""module provide async generator"""
import asyncio
import time
from importlib import import_module as using
async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """async generator function"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
