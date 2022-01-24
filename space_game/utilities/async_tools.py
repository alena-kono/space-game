import asyncio


async def sleep_for(n_times: int) -> None:
    """Create coroutines that will be completed after :n_times:."""
    for _ in range(n_times):
        await asyncio.sleep(0)
