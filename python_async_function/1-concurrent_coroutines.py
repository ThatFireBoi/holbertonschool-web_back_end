#!/usr/bin/env python3
"""Import wait_random from 0-basic_async_syntax.
Write an async routine called wait_n that takes in 2 int arguments
(max_delay, n) and returns the list of all the delays (float values)."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return a list of all the delays (float values)"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
