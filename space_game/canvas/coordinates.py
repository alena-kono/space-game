import curses
import random
from typing import Any, Optional, Tuple, Union

from space_game.game.settings import CANVAS_BORDER_SIZE

Coordinate = Union[int, float]
Coordinates = Tuple[Coordinate, Coordinate]
RectangleCoordinates = Tuple[Coordinate, Coordinate, Coordinate, Coordinate]


def get_max_allowed_canvas_coordinates(
        canvas: Optional[Any] = None
) -> Coordinates:
    """Get max allowed height (max row value) and width
    (max column value) of the current canvas.
    """
    max_row, max_column = _get_canvas_size(canvas)
    return (
        max_row - CANVAS_BORDER_SIZE,
        max_column - CANVAS_BORDER_SIZE,
    )


def get_middle_window_coordinates(
        canvas: Optional[Any] = None
) -> Coordinates:
    """Get row and column coordinates of the current canvas midpoint."""
    max_row, max_column = _get_canvas_size(canvas)
    return max_row // 2, max_column // 2


def get_canvas_available_coordinates(
        canvas: Optional[Any] = None
) -> RectangleCoordinates:
    """Get current canvas min and max coordinates and return them
    as a tuple: (min_row, min_column, max_row, max_column).
    Coordinates do not include canvas border.
    """
    min_row, min_column, max_row, max_column = _get_canvas_coordinates(
            canvas
    )
    return (
            min_row + CANVAS_BORDER_SIZE,
            min_column + CANVAS_BORDER_SIZE,
            max_row - CANVAS_BORDER_SIZE,
            max_column - CANVAS_BORDER_SIZE,
        )


def get_random_coordinates(canvas: Optional[Any] = None) -> Coordinates:
    """Get random row and column coordinates."""
    max_row, max_column = get_max_allowed_canvas_coordinates(canvas)
    return (
            random.randint(CANVAS_BORDER_SIZE, int(max_row)),
            random.randint(CANVAS_BORDER_SIZE, int(max_column)),
            )


def _get_canvas_size(canvas: Optional[Any] = None) -> Coordinates:
    """Get height (max row value) and width
    (max column value) of the current canvas.
    """
    if not canvas:
        return curses.initscr().getmaxyx()
    max_coordinates: Coordinates = canvas.getmaxyx()
    return max_coordinates


def _get_canvas_coordinates(
        canvas: Optional[Any] = None
) -> RectangleCoordinates:
    """Get current canvas min and max coordinates and return them
    as a tuple: (min_row, min_column, max_row, max_column).
    Coordinates include canvas border.
    """
    min_row, min_column = 0, 0
    max_row, max_column = _get_canvas_size(canvas)
    return min_row, min_column, max_row, max_column
