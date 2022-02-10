import curses
import random
from typing import Tuple

from space_game.settings import CANVAS_BORDER_SIZE


def _get_canvas_size() -> Tuple[int, int]:
    """Get height (max row value) and width
    (max column value) of the current canvas.
    """
    return curses.initscr().getmaxyx()


def get_max_allowed_canvas_coordinates() -> Tuple[int, int]:
    """Get max allowed height (max row value) and width
    (max column value) of the current canvas.
    """
    max_row, max_column = _get_canvas_size()
    return (
        max_row - CANVAS_BORDER_SIZE,
        max_column - CANVAS_BORDER_SIZE,
    )


def get_middle_window_coordinates() -> Tuple[int, int]:
    """Get row and column coordinates of the current canvas midpoint."""
    max_row, max_column = _get_canvas_size()
    return max_row // 2, max_column // 2


def _get_canvas_coordinates() -> Tuple[int, int, int, int]:
    """Get current canvas min and max coordinates and return them
    as a tuple: (min_row, min_column, max_row, max_column).
    Coordinates include canvas border.
    """
    min_row, min_column = 0, 0
    max_row, max_column = _get_canvas_size()
    return min_row, min_column, max_row, max_column


def get_canvas_available_coordinates() -> Tuple[int, int, int, int]:
    """Get current canvas min and max coordinates and return them
    as a tuple: (min_row, min_column, max_row, max_column).
    Coordinates do not include canvas border.
    """
    min_row, min_column, max_row, max_column = _get_canvas_coordinates()
    return (
            min_row + CANVAS_BORDER_SIZE,
            min_column + CANVAS_BORDER_SIZE,
            max_row - CANVAS_BORDER_SIZE,
            max_column - CANVAS_BORDER_SIZE,
        )


def get_random_coordinates() -> Tuple[int, int]:
    """Get random row and column coordinates."""
    max_row, max_column = get_max_allowed_canvas_coordinates()
    return (
            random.randint(CANVAS_BORDER_SIZE, max_row),
            random.randint(CANVAS_BORDER_SIZE, max_column),
        )
