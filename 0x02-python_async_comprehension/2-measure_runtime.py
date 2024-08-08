#!/usr/bin/env python3
"""
Module for measuring the runtime of async_comprehension executed in parallel.
"""

import asyncio
import time
import importlib.util
from typing import List

# Dynamically import the module
spec = importlib.util.spec_from_file_location(
    "async_comprehension", "./1-async_comprehension.py"
    )
async_comprehension_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(async_comprehension_module)
async_comprehension = async_comprehension_module.async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing async_comprehension
    four times in parallel using asyncio.gather.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time

if __name__ == "__main__":
    async def main():
        total_runtime = await measure_runtime()
        print(f"Total runtime: {total_runtime:.2f} seconds")

    asyncio.run(main())
