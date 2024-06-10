#!/usr/bin/env python3
"""module for async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait for random amount of time"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
