import asyncio
import curses
from typing import Any, List, Tuple

from space_game.settings import TIC_TIMEOUT
from space_game.utilities.async_tools import sleep_for


async def blink(
    canvas: Any,
    row: int,
    column: int,
    offset_tick_amount: int,
    symbol: str = "*"
) -> None:
    """Display animation of blinking star.

    Coordinates, timeout of blinking and symbol of star
    can be specified.
    """
    animation_states = generate_animation_states()

    state, timeout = animation_states[0]
    canvas.addstr(row, column, symbol, state)
    await asyncio.sleep(0)

    await sleep_for(offset_tick_amount)
    while True:
        for state, timeout in animation_states:
            canvas.addstr(row, column, symbol, state)
            await sleep_for(timeout)


def generate_animation_states() -> List[Tuple[int, int]]:
    """Generate brightness and offset timeout of star animation."""
    return [
      (curses.A_DIM, int(2 / TIC_TIMEOUT)),
      (curses.A_NORMAL, int(0.3 / TIC_TIMEOUT)),
      (curses.A_BOLD, int(0.5 / TIC_TIMEOUT)),
      (curses.A_NORMAL, int(0.3 / TIC_TIMEOUT)),
    ]
