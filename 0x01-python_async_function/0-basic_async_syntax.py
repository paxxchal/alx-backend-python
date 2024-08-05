#!/usr/bin/env python3
"""
Basic asynchronous syntax example.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay
    (inclusive) seconds and return the delay.

    Args:
        max_delay (int): Maximum delay in seconds. Default is 10 seconds.

    Returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    max_delay = 10
    delay = asyncio.run(wait_random(max_delay))
    print(f"Waited for {delay} seconds.")
