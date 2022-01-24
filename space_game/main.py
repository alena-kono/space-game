import asyncio
import curses
import time
from typing import Any

from space_game.settings import TIC_TIMEOUT
from space_game.stars.generator import (calculate_optimal_stars_count,
                                        generate_random_stars)
from space_game.window.coordinates import get_middle_window_coordinates


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


def draw(canvas: Any) -> None:
    curses.curs_set(False)
    canvas.border()
    stars_count = calculate_optimal_stars_count()

    space_objects = generate_random_stars(
        stars_count=stars_count,
        canvas=canvas,
    )
    space_objects.append(fire(canvas, *get_middle_window_coordinates()))

    while True:
        exhausted_coroutines = []
        for space_object in space_objects:
            try:
                space_object.send(None)
            except StopIteration:
                exhausted_coroutines.append(space_object)
        canvas.border()
        canvas.refresh()
        time.sleep(TIC_TIMEOUT)

        for coroutine in exhausted_coroutines:
            space_objects.remove(coroutine)


def main() -> None:
    curses.update_lines_cols()
    curses.wrapper(draw)


if __name__ == "__main__":
    main()
