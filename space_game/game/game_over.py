import asyncio
from typing import Any

from space_game.canvas.coordinates import get_middle_window_coordinates
from space_game.canvas.frame import (draw_frame,
                                     get_coordinates_for_centered_frame)
from space_game.game.globals import game_over
from space_game.game.settings import GAMEOVER_FRAME_FILENAME
from space_game.utilities.read_file import read_file


async def show_gameover(canvas: Any) -> None:
    """Show game over screen."""
    row, column = get_middle_window_coordinates()
    gameover_frame = read_file(GAMEOVER_FRAME_FILENAME)
    row, column = get_coordinates_for_centered_frame(gameover_frame)
    while True:
        draw_frame(canvas, row, column, gameover_frame)
        await asyncio.sleep(0)


def activate_game_over() -> None:
    """Activate game over status globally."""
    global game_over
    game_over = True


def is_game_over() -> bool:
    """Return True if game is over, otherwise - False."""
    return bool(game_over)
