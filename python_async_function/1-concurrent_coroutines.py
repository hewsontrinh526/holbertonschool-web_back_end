#!/usr/bin/env python3
"""
An async routine called wait_n that takes in 2 int arguments (in this order):
n and max_delay. You will spawn wait_random n times with the specified
max_delay. wait_n should return the list of all the delays (float values). The
list if the delay should be ascending order without using sort() because of
concurrency
"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns the list of all the delays (float values)
    """
    delays: List[float] = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
