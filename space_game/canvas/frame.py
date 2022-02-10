from typing import Any, Tuple, Union

from space_game.canvas.coordinates import get_canvas_available_coordinates


def draw_frame(
    canvas: Any,
    start_row: Union[int, float],
    start_column: Union[int, float],
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
        start_row: int,
        start_column: int,
        row_change: int,
        column_change: int,
) -> Tuple[int, int]:
    """Calculate new frame coordinates based on its start and increment
    coordinates and coordinates of available canvas.
    """
    row, column = start_row + row_change, start_column + column_change
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
