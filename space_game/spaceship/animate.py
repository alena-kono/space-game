import asyncio
import curses
import itertools
from typing import Any, Tuple

from space_game.settings import DEBUG, SPEED, SPEED_DEBUG
from space_game.spaceship.get_frames import get_spaceship_frames
from space_game.utilities.async_tools import sleep_for
from space_game.window.controls import read_controls
from space_game.window.coordinates import get_middle_window_coordinates
from space_game.window.frame import draw_frame, calculate_frame_coordinates

# Globals
spaceship = ""


async def run_spaceship(canvas: Any) -> None:
    """Run spaceship."""
    row, column = get_middle_window_coordinates()
    while True:
        tmp_spaceship = spaceship
        # Read only arrow keys controls.
        row_change, column_change = read_controls(canvas)[:2]
        if DEBUG:
            speed = SPEED_DEBUG
        else:
            speed = SPEED
        row_change, column_change = change_speed(
            increment=speed,
            row=row_change,
            column=column_change,
        )

        row, column = calculate_frame_coordinates(
                tmp_spaceship,
                row,
                column,
                row_change,
                column_change,
            )
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


def change_speed(increment: int, row: int, column: int) -> Tuple[int, int]:
    """Change speed by increment and return updated row and column."""
    return row * increment, column * increment


async def fire(
    canvas: Any,
    start_row: int,
    start_column: int,
    rows_speed: float = -0.3,
    columns_speed: float = 0,
) -> None:
    """Display animation of gun shot, direction and speed can be specified."""
    row, column = float(start_row), float(start_column)

    canvas.addstr(round(row), round(column), '*')
    await asyncio.sleep(0)

    canvas.addstr(round(row), round(column), 'O')
    await asyncio.sleep(0)
    canvas.addstr(round(row), round(column), ' ')

    row += rows_speed
    column += columns_speed

    symbol = '-' if columns_speed else '|'

    rows, columns = canvas.getmaxyx()
    max_row, max_column = rows - 1, columns - 1

    curses.beep()

    while 0 < row < max_row and 0 < column < max_column:
        canvas.addstr(round(row), round(column), symbol)
        await asyncio.sleep(0)
        canvas.addstr(round(row), round(column), ' ')
        row += rows_speed
        column += columns_speed
