import curses
from typing import Tuple

from space_game.settings import CANVAS_BORDER_SIZE


def _get_window_size() -> Tuple[int, int]:
    """Get current window height and width."""
    return curses.initscr().getmaxyx()


def get_max_window_coordinates() -> Tuple[int, int]:
    """Get max allowed height and width of current window."""
    window_height, window_width = _get_window_size()
    return (window_height - 1, window_width - 1)


def get_middle_window_coordinates() -> Tuple[int, int]:
    """Get height and width of the center of current window."""
    window_height, window_width = _get_window_size()
    return (window_height // 2, window_width // 2)


def get_window_coordinates() -> Tuple[int, int, int, int]:
    """Get current window min and max coordinates and return them
    as a tuple: (min_row, min_column, max_row, max_column).
    Coordinates include window border.
    """
    max_height, max_width = _get_window_size()
    return 0, 0, max_height, max_width


def get_window_available_coordinates() -> Tuple[int, int, int, int]:
    """Get current window min and max coordinates and return them
    as a tuple: (min_row, min_column, max_row, max_column).
    Coordinates does not include window border.
    """
    min_row, min_column, max_row, max_column = get_window_coordinates()
    return (
            min_row + CANVAS_BORDER_SIZE,
            min_column + CANVAS_BORDER_SIZE,
            max_row - CANVAS_BORDER_SIZE,
            max_column - CANVAS_BORDER_SIZE,
        )
