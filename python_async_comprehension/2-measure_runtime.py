#!/usr/bin/env python3
"""
A measure_runtime coroutine that will execute async_comprehension four times
in parallel using asyncio.gather
"""
import asyncio
import random
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Returns the total runtime for executing async_comprehension four times
    in parallel using asyncio.gather
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
