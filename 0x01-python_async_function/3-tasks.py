#!/usr/bin/env python3
"""module for async"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """wait  for random amount of time"""
    return asyncio.create_task(wait_random(max_delay))
