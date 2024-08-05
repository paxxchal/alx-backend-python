import asyncio
from typing import List
import importlib
wait_random = importlib.import_module('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []

    async def spawn_wait_random():
        delay = await wait_random(max_delay)
        delays.append(delay)
        return delay

    await asyncio.gather(*(spawn_wait_random() for _ in range(n)))

    return sorted(delays)
