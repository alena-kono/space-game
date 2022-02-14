import itertools
from typing import Any

from space_game.canvas.controls import read_controls
from space_game.canvas.coordinates import get_middle_window_coordinates
from space_game.canvas.frame import (calculate_frame_coordinates, draw_frame,
                                     get_frames_from_dir,
                                     get_middle_frame_column_coordinate)
from space_game.global_objects import space_objects, spaceship
from space_game.settings import SPACESHIP_FRAMES_DIR
from space_game.spaceship.fire import fire
from space_game.spaceship.physics import Speed, update_speed
from space_game.utilities.async_tools import sleep_for


async def run_spaceship(canvas: Any) -> None:
    """Run spaceship."""
    row, column = get_middle_window_coordinates()
    row_speed: Speed = 0
    column_speed: Speed = 0
    while True:
        tmp_spaceship = spaceship
        row_direction, column_direction, fire_shot = read_controls(canvas)
        row_speed, column_speed = update_speed(
                row_speed,
                column_speed,
                row_direction,
                column_direction,
                )
        row, column = row + row_speed, column + column_speed
        row, column = calculate_frame_coordinates(
                tmp_spaceship,
                row,
                column,
                )
        if fire_shot:
            fire_gun_column = get_middle_frame_column_coordinate(
                    column,
                    tmp_spaceship
                    )
            space_objects.append(fire(canvas, row, fire_gun_column))

        draw_frame(canvas, row, column, tmp_spaceship)
        await sleep_for(1)
        draw_frame(canvas, row, column, tmp_spaceship, negative=True)


async def animate_spaceship() -> None:
    """Display animation of flying spaceship."""
    animation_states = get_frames_from_dir(SPACESHIP_FRAMES_DIR)
    global spaceship
    for state in itertools.cycle(animation_states):
        spaceship = state
        await sleep_for(2)
