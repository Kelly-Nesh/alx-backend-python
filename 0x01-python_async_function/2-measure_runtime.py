#!/usr/bin/env python3
"""Measure the runtime"""
wait_n = __import__("1-concurrent_coroutines").wait_n
import asyncio
import time

def measure_time(n: int, max_delay: int) -> float:
    """Measure the runtime of wait_n(n, max_delay)"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return end - start