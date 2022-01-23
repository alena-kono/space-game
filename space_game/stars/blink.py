import asyncio

from space_game.stars.generator import generate_animation_states
from space_game.utilities.async_tools import sleep_for


async def blink(canvas, row, column, offset_tick_amount, symbol="*"):
    animation_states = generate_animation_states()

    state, timeout = animation_states[0]
    canvas.addstr(row, column, symbol, state)
    await asyncio.sleep(0)

    await sleep_for(offset_tick_amount)
    while True:
        for state, timeout in animation_states:
            canvas.addstr(row, column, symbol, state)
            await sleep_for(timeout)
