import asyncio
import curses
from typing import Any

from space_game.canvas.coordinates import Coordinate
from space_game.global_objects import obstacles, obstacles_in_last_collisions
from space_game.spaceship.physics import Speed


async def fire(
    canvas: Any,
    start_row: Coordinate,
    start_column: Coordinate,
    rows_speed: Speed = -0.3,
    columns_speed: Speed = 0,
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

        for obstacle in obstacles:
            if obstacle.has_collision(row, column):
                obstacles_in_last_collisions.append(obstacle)
                obstacles.remove(obstacle)
                return None

        canvas.addstr(round(row), round(column), symbol)
        await asyncio.sleep(0)
        canvas.addstr(round(row), round(column), " ")
        row += rows_speed
        column += columns_speed
