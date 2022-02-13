import asyncio
import curses
import itertools
from typing import Any

from space_game.global_objects import spaceship
from space_game.settings import SPACESHIP_FRAMES_DIR
from space_game.spaceship.physics import Speed, update_speed
from space_game.utilities.async_tools import sleep_for
from space_game.canvas.controls import read_controls
from space_game.canvas.coordinates import get_middle_window_coordinates
from space_game.canvas.frame import (
        draw_frame,
        calculate_frame_coordinates,
        get_frames_from_dir)


async def run_spaceship(canvas: Any) -> None:
    """Run spaceship."""
    row, column = get_middle_window_coordinates()
    row_speed: Speed = 0
    column_speed: Speed = 0
    while True:
        tmp_spaceship = spaceship
        # Read only arrow keys controls.
        row_direction, column_direction = read_controls(canvas)[:2]
        row_speed, column_speed = update_speed(
                row_speed,
                column_speed,
                row_direction,
                column_direction,
                )
        row, column = row + row_speed, column + column_speed
        row, column = calculate_frame_coordinates(
                tmp_spaceship,
                row,
                column,
                )
        print(row, column)
        draw_frame(canvas, row, column, tmp_spaceship)
        await sleep_for(1)
        draw_frame(canvas, row, column, tmp_spaceship, negative=True)


async def animate_spaceship() -> None:
    """Display animation of flying spaceship."""
    animation_states = get_frames_from_dir(SPACESHIP_FRAMES_DIR)
    global spaceship
    for state in itertools.cycle(animation_states):
        spaceship = state
        await sleep_for(2)


async def fire(
    canvas: Any,
    start_row: int,
    start_column: int,
    rows_speed: float = -0.3,
    columns_speed: float = 0,
) -> None:
    """Display animation of gun shot, direction and speed can be specified."""
    row, column = float(start_row), float(start_column)

    canvas.addstr(round(row), round(column), "*")
    await asyncio.sleep(0)

    canvas.addstr(round(row), round(column), "O")
    await asyncio.sleep(0)
    canvas.addstr(round(row), round(column), " ")

    row += rows_speed
    column += columns_speed

    symbol = "-" if columns_speed else "|"

    rows, columns = canvas.getmaxyx()
    max_row, max_column = rows - 1, columns - 1

    curses.beep()

    while 0 < row < max_row and 0 < column < max_column:
        canvas.addstr(round(row), round(column), symbol)
        await asyncio.sleep(0)
        canvas.addstr(round(row), round(column), " ")
        row += rows_speed
        column += columns_speed
