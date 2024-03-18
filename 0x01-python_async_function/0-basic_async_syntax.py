#!/usr/bin/env python3
"""The basics of async"""
import asyncio
import random
from typing import Union


async def wait_random(max_delay: Union[int, float] = 10) -> float:
    """Takes in an integer argument (max_delay, with a default value of 10)
    waits for a random delay between 0 and
        max_delay (included and float value) seconds
    returns delay time."""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
