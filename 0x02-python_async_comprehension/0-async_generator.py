#!usr/bin/env python3
"""Async Generator"""


import asyncio
import random


async def async_generator():
    """
    An asynchronous generator that yields random numbers between 0 and 10
    after a 1 second delay.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
