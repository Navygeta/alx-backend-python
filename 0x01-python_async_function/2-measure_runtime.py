#!/usr/bin/env python3

import asyncio
import time
from typing import List

from 1-concurrent_coroutines import wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns the
    average time per iteration.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The average time per iteration.
    """
    start_time = time.time()

    await wait_n(n, max_delay)

    end_time = time.time()

    total_time = end_time - start_time
    average_time = total_time / n

    return average_time
