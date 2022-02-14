import asyncio
from typing import Any, Generator, List, Optional, Tuple

from space_game.canvas.coordinates import Coordinate, Coordinates
from space_game.canvas.frame import Height, Size, Width, draw_frame


class Obstacle:
    def __init__(
            self,
            row: Coordinate,
            column: Coordinate,
            rows_size: Height = 1,
            columns_size: Width = 1,
            uid: Optional[str] = None
    ) -> None:
        self.row = row
        self.column = column
        self.rows_size = rows_size
        self.columns_size = columns_size
        self.uid = uid

    def get_bounding_box_frame(self) -> str:
        # increment box size to compensate obstacle movement
        rows, columns = self.rows_size + 1, self.columns_size + 1
        return "\n".join(_get_bounding_box_lines(rows, columns))

    def get_bounding_box_corner_pos(self) -> Coordinates:
        return self.row - 1, self.column - 1

    def dump_bounding_box(self) -> Tuple[Coordinate, Coordinate, str]:
        row, column = self.get_bounding_box_corner_pos()
        return row, column, self.get_bounding_box_frame()

    def has_collision(
            self,
            obj_corner_row: Coordinate,
            obj_corner_column: Coordinate,
            obj_size_rows: Height = 1,
            obj_size_columns: Width = 1,
    ) -> bool:
        """Determine if collision has occured. Return True or False."""
        return has_collision(
            (self.row, self.column),
            (self.rows_size, self.columns_size),
            (obj_corner_row, obj_corner_column),
            (obj_size_rows, obj_size_columns),
        )


def _get_bounding_box_lines(
        rows: Height,
        columns: Width,
) -> Generator[str, None, None]:
    yield " " + "-" * columns + " "
    for _ in range(rows):
        yield "|" + " " * columns + "|"
    yield " " + "-" * columns + " "


async def show_obstacles(canvas: Any, obstacles: List[Obstacle]) -> None:
    """Display bounding boxes of every obstacle in a list."""
    while True:
        boxes = []

        for obstacle in obstacles:
            boxes.append(obstacle.dump_bounding_box())

        for row, column, frame in boxes:
            draw_frame(canvas, row, column, frame)

        await asyncio.sleep(0)

        for row, column, frame in boxes:
            draw_frame(canvas, row, column, frame, negative=True)


def _is_point_inside(
        corner_row: Coordinate,
        corner_column: Coordinate,
        size_rows: Height,
        size_columns: Width,
        point_row: Coordinate,
        point_row_column: Coordinate,
) -> bool:
    rows_flag = corner_row <= point_row < corner_row + size_rows
    columns_flag = (
            corner_column <= point_row_column <
            corner_column + size_columns
            )
    return all((rows_flag, columns_flag))


def has_collision(
        obstacle_corner: Coordinates,
        obstacle_size: Size,
        obj_corner: Coordinates,
        obj_size: Size = (1, 1),
) -> bool:
    """Determine if collision has occured. Return True or False."""
    opposite_obstacle_corner = Coordinate
    opposite_obj_corner = Coordinate
    opposite_obstacle_corner = (
        obstacle_corner[0] + obstacle_size[0] - 1,
        obstacle_corner[1] + obstacle_size[1] - 1,
    )
    opposite_obj_corner = (
        obj_corner[0] + obj_size[0] - 1,
        obj_corner[1] + obj_size[1] - 1,
    )
    return any([
        _is_point_inside(*obstacle_corner, *obstacle_size, *obj_corner),
        _is_point_inside(
            *obstacle_corner,
            *obstacle_size,
            *opposite_obj_corner,
            ),
        _is_point_inside(*obj_corner, *obj_size, *obstacle_corner),
        _is_point_inside(*obj_corner, *obj_size, *opposite_obstacle_corner),
    ])
