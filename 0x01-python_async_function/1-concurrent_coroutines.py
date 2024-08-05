#!/usr/bin/env python3
"""
This module contains an async routine that spawns wait_random n times.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay to be used in wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays


if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
