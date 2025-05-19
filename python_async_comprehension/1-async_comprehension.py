#!/usr/bin/env python3
"""
Asynchronously generates 10 random floating-point numbers between 0 and 10.

Yields:
    float: A random number between 0 and 10, generated after a 1 second delay.

Usage:
    This function is an asynchronous generator that yields a new random float
    every second, for a total of 10 values. It can be used in an async for loop.

Example:
    async for number in async_generator():
        print(number)
"""


import asyncio
import random
from typing import AsyncGenerator, List


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield a random number between 0 and 10, 10 times, waiting 1 second each time."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers from async_generator and returns them as a list."""
    return [num async for num in async_generator()]
