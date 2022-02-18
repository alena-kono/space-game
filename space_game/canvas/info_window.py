from typing import Any

from space_game.canvas.coordinates import get_max_allowed_canvas_coordinates
from space_game.canvas.frame import Height
from space_game.game.settings import INFO_WINDOW_HEIGHT


def get_info_window(canvas: Any) -> Any:
    """Get info window based on canvas."""
    max_row, max_column = get_max_allowed_canvas_coordinates(canvas)
    height = _get_info_window_height()
    row, column = max_row - height, 0
    return canvas.derwin(height, max_column, row, column)


def _get_info_window_height() -> Height:
    """Get info window height from settings."""
    return INFO_WINDOW_HEIGHT
