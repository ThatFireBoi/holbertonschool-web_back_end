#!/usr/bin/env python3
"""Module containing measure_runtime coroutine"""


import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Return the average time for wait_n to execute n times with the
    specified max_delay"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
