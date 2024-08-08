#!/usr/bin/env python3
"""
Module for measure_runtime coroutine.
"""

import asyncio
import time
import importlib

# Import the async_comprehension function from 1-async_comprehension module
async_comprehension_module = importlib.import_module("1-async_comprehension")
async_comprehension = async_comprehension_module.async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather, and measures the total runtime.

    Returns:
        The total runtime as a float.
    """
    start_time = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.perf_counter()

    return end_time - start_time
