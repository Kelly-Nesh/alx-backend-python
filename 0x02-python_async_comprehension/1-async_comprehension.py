#!/usr/bin/env python3
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    """
    Collects 10 random numbers using an async comprehension
    and returns them as a list.
    """
    return [await num for num in async_generator()]
