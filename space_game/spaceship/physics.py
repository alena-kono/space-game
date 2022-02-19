import math
from typing import Tuple, Union

Speed = Union[int, float]


def update_speed(
    row_speed: Speed,
    column_speed: Speed,
    rows_direction: int,
    columns_direction: int,
    row_speed_limit:  Speed = 2,
    column_speed_limit:  Speed = 2,
    fading: float = 0.8,
) -> Tuple[Speed, Speed]:
    """Update speed smootly to make control handy for player.
    Return new speed value (row_speed, column_speed).

    rows_direction — is a force direction by rows axis.
    Possible values:
       -1 — if force pulls up.
       0  — if force has no effect.
       1  — if force pulls down.

    columns_direction — is a force direction by colums axis.
    Possible values:
       -1 — if force pulls left.
       0  — if force has no effect.
       1  — if force pulls right.
       """
    template_msg = "Wrong {0} value {1} Expects -1, 0 or 1."
    if rows_direction not in (-1, 0, 1):
        raise ValueError(
                template_msg.format("rows_direction", rows_direction)
                )
    if columns_direction not in (-1, 0, 1):
        raise ValueError(
                template_msg.format("columns_direction", columns_direction)
                )
    if fading < 0 or fading > 1:
        template_msg = "Wrong fading value {0}. Expects float [0,1]."
        raise ValueError(template_msg.format(fading))

    # Decrease speed to make spaceship stop slowly.
    row_speed *= fading
    column_speed *= fading

    row_speed_limit, column_speed_limit = (
            abs(row_speed_limit),
            abs(column_speed_limit),
            )
    if rows_direction != 0:
        row_speed = _apply_acceleration(
            row_speed,
            row_speed_limit,
            rows_direction > 0,
            )
    if columns_direction != 0:
        column_speed = _apply_acceleration(
                column_speed,
                column_speed_limit,
                columns_direction > 0,
            )
    return row_speed, column_speed


def _limit(
    value: Union[int, float],
    min_value: Union[int, float],
    max_value: Union[int, float],
) -> Union[int, float]:
    """Limit value by min_value and max_value."""
    if value < min_value:
        return min_value
    if value > max_value:
        return max_value
    return value


def _apply_acceleration(
    speed: Speed,
    speed_limit: Speed,
    forward: bool = True,
) -> Speed:
    """Change speed — accelerate or brake — according
    to force direction.
    """
    speed_limit = abs(speed_limit)

    speed_fraction = speed / speed_limit

    # If the spaceship is standing still, then accelerate abruptly.
    # If the spaceship is running fastly, then accelerate slowly.
    delta = math.cos(speed_fraction) * 0.75

    if forward:
        result_speed = speed + delta
    else:
        result_speed = speed - delta

    result_speed = _limit(result_speed, -speed_limit, speed_limit)

    # If speed is close to zero, then the spaceship is stopped.
    if abs(result_speed) < 0.1:
        result_speed = 0

    return result_speed
