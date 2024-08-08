#!/usr/bin/env python3
"""
This module contains the `async_comprehension` coroutine.
"""

import asyncio
from typing import List


async def async_comprehension() -> List[int]:
    """
    Collects 10 random numbers using async
    comprehension over `async_generator`.

    Returns:
        List[int]: A list of 10 random numbers.
    """
    async_generator = __import__('0-async_generator').async_generator
    return [num async for num in async_generator()]
