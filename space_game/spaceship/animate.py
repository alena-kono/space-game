import itertools
from typing import Any, List

from space_game.settings import (SPACESHIP_FRAME_0_FILENAME,
                                 SPACESHIP_FRAME_1_FILENAME, TIC_TIMEOUT)
from space_game.utilities.async_tools import sleep_for
from space_game.utilities.read_file import read_file
from space_game.window.frame import draw_frame


async def animate_spaceship(canvas: Any, row: int, column: int) -> None:
    """Display animation of flying spaceship.

    Coordinates of the highest point of a spaceship can be specified.
    """
    animation_states = get_spaceship_animation_states()
    for state in itertools.cycle(animation_states):
        draw_frame(canvas, row, column, state)
        await sleep_for(int(TIC_TIMEOUT * 1000))
        draw_frame(canvas, row, column, state, negative=True)


def get_spaceship_animation_states() -> List[str]:
    """Read animation states of flying spaceship from files."""
    return [
        read_file(SPACESHIP_FRAME_0_FILENAME),
        read_file(SPACESHIP_FRAME_1_FILENAME),
    ]
