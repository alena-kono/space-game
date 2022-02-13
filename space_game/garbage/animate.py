import asyncio
from typing import Any
from space_game.canvas.coordinates import (
        Coordinate,
        get_max_allowed_canvas_coordinates)

from space_game.canvas.frame import draw_frame
from space_game.spaceship.physics import Speed


async def fly_garbage(
    canvas: Any,
    column: Coordinate,
    garbage_frame: str,
    speed: Speed = 0.5,
) -> None:
    """Animate garbage, flying from top to bottom. Сolumn position
    will stay same, as specified on start.
    """
    rows_number, columns_number = get_max_allowed_canvas_coordinates()

    column = max(column, 0)
    column = min(column, columns_number - 1)

    row: float = 0

    while row < rows_number:
        draw_frame(canvas, row, column, garbage_frame)
        await asyncio.sleep(0)
        draw_frame(canvas, row, column, garbage_frame, negative=True)
        row += speed
