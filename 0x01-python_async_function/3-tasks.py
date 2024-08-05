#!/usr/bin/env python3
"""
Task example.
"""

import asyncio
import importlib.util

# Dynamically import wait_random from 0-basic_async_syntax.py
spec = importlib.util.spec_from_file_location(
    "wait_random", "./0-basic_async_syntax.py"
    )
async_syntax = importlib.util.module_from_spec(spec)
spec.loader.exec_module(async_syntax)
wait_random = async_syntax.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for wait_random with the given max_delay.

    Args:
        max_delay (int): The maximum delay value to pass to wait_random.

    Returns:
        asyncio.Task: The created asyncio.Task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    max_delay = 10
    task = task_wait_random(max_delay)
    print(f"Created task: {task}")
