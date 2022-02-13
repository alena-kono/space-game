import os
from typing import Any, List, Tuple, Union

from space_game.canvas.coordinates import (Coordinate, Coordinates,
                                           get_canvas_available_coordinates)
from space_game.utilities.read_file import read_file


def draw_frame(
    canvas: Any,
    start_row: Coordinate,
    start_column: Coordinate,
    text: str,
    negative: bool = False,
) -> None:
    """Draw multiline text fragment on canvas, erase text instead of
    drawing if negative=True is specified.
    """
    rows_number, columns_number = canvas.getmaxyx()

    for row, line in enumerate(text.splitlines(), round(start_row)):
        if row < 0:
            continue

        if row >= rows_number:
            break

        for column, symbol in enumerate(line, round(start_column)):
            if column < 0:
                continue

            if column >= columns_number:
                break

            if symbol == " ":
                continue

            # Check that current position it is not in a lower right
            # corner of the canvas
            # Curses will raise exception in that case. Don`t ask why…
            # https://docs.python.org/3/library/curses.html#curses.window.addch
            if row == rows_number - 1 and column == columns_number - 1:
                continue

            symbol = symbol if not negative else " "
            canvas.addch(row, column, symbol)


def get_frames_from_dir(dir_path: str) -> List[str]:
    """Read frames from files located in the directory
    specified at dir_path.
    """
    files = os.listdir(dir_path)
    return [
            read_file(dir_path + "/" + input_file) for input_file in files
            ]


def get_frame_size(text: str) -> Tuple[int, int]:
    """Calculate size of multiline text fragment,
    return pair — number of rows and columns.
    """
    lines = text.splitlines()
    rows = len(lines)
    columns = max([len(line) for line in lines])
    return rows, columns


def calculate_frame_coordinates(
        frame: str,
        row: Union[int, float],
        column: Union[int, float],
) -> Coordinates:
    """Calculate new frame coordinates based on its
    coordinates and coordinates of available canvas.
    """
    (
        min_row,
        min_column,
        max_row,
        max_column
    ) = get_canvas_available_coordinates()
    frame_rows_amount, frame_columns_amount = get_frame_size(frame)

    updated_row = min(
            max(row, min_row),
            max_row - frame_rows_amount,
        )
    updated_column = min(
            max(column, min_column),
            max_column - frame_columns_amount,
        )
    return updated_row, updated_column


def get_middle_frame_column_coordinate(
        start_column: Coordinate,
        frame: str,
) -> Coordinate:
    """Get coordinate which represents middle point of
    frame at the column axis.
    """
    frame_columns = get_frame_size(frame)[1]
    return start_column + frame_columns / 2
