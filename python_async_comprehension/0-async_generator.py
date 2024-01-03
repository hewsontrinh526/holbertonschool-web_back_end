#!/usr/bin/env python3
"""
A coroutine called async_generator that takes no arguments
"""
from random import random
import asyncio
from typing import Generator, AsyncGenerator


async def async_generator() -> Generator[float, None, None]:
    """
    Yields a random number between 0 and 10
    """
    for i in range(10):
        yield random() * 10
        await asyncio.sleep(1)
