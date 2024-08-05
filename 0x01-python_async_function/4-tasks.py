#!/usr/bin/env python3
"""
Concurrent coroutines with tasks example.
"""

import asyncio
from typing import List
import importlib.util

# Dynamically import task_wait_random from 3-tasks.py
spec = importlib.util.spec_from_file_location(
    "task_wait_random", "./3-tasks.py"
    )
tasks_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tasks_module)
task_wait_random = tasks_module.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified
    max_delay and return the list of delays in ascending order.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay value to pass to task_wait_random.

    Returns:
        List[float]: The list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays


if __name__ == "__main__":
    n = 5
    max_delay = 10
    delays = asyncio.run(task_wait_n(n, max_delay))
    print(f"Delays: {delays}")
