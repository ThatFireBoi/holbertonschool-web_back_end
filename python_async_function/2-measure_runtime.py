#!/usr/bin/env python3
"""Module containing measure_runtime coroutine"""


import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_runtime(n: int, max_delay: int) -> float:
    """Return the total runtime"""
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    return (end_time - start_time) / n
