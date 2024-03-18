#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay.
    return the list of all the delays (float values)
    list to be in ascending order
    """
    delay_list: List[float] = [await wait_random(max_delay) for i in range(n)]
    listlen: int = len(delay_list)
    for i in range(listlen):
        for j in range(0, listlen-i-1):
            if delay_list[j] > delay_list[j+1]:
                delay_list[j], delay_list[j+1] = delay_list[j+1], delay_list[j]
    return delay_list
