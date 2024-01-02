#!/usr/bin/env python3
"""
A coroutine called async_generator that takes no arguments
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Yields a random number between 0 and 10
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
