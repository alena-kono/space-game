import itertools
from typing import Any

from space_game.spaceship.get_frames import get_spaceship_frames
from space_game.utilities.async_tools import sleep_for
from space_game.window.controls import read_controls
from space_game.window.coordinates import get_middle_window_coordinates
from space_game.window.frame import draw_frame

# Globals
spaceship = ""


async def run_spaceship(canvas: Any) -> None:
    """Run spaceship."""
    row, column = get_middle_window_coordinates()
    while True:
        tmp_spaceship = spaceship
        row_change, column_change = read_controls(canvas)[:2]
        row += row_change
        column += column_change
        draw_frame(canvas, row, column, tmp_spaceship)
        await sleep_for(1)
        draw_frame(canvas, row, column, tmp_spaceship, negative=True)


async def animate_spaceship() -> None:
    """Display animation of flying spaceship."""
    animation_states = get_spaceship_frames()
    global spaceship
    for state in itertools.cycle(animation_states):
        spaceship = state
        await sleep_for(2)
