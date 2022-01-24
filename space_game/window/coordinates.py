import curses
from typing import Tuple


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
