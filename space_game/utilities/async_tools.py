import asyncio


async def sleep_for(n_times: int) -> None:
    for _ in range(n_times):
        await asyncio.sleep(0)
