#!/usr/bin/env python3
"""
Module for async_comprehension coroutine.
"""

from typing import List
import importlib

# Import the async_generator from 0-async_generator module
async_generator = importlib.import_module("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    """
    return [number async for number in async_generator()]
