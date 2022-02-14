import asyncio
import curses
from typing import Any

from space_game.canvas.coordinates import Coordinate
from space_game.canvas.frame import draw_frame, get_frame_size
from space_game.settings import EXPLOSION_FRAMES


async def explode(
        canvas: Any,
        center_row: Coordinate,
        center_column: Coordinate
) -> None:
    """Animate explosion."""
    rows, columns = get_frame_size(EXPLOSION_FRAMES[0])
    corner_row = center_row - rows / 2
    corner_column = center_column - columns / 2

    curses.beep()
    for frame in EXPLOSION_FRAMES:
        draw_frame(canvas, corner_row, corner_column, frame)

        await asyncio.sleep(0)
        draw_frame(canvas, corner_row, corner_column, frame, negative=True)
        await asyncio.sleep(0)
