import random
from typing import Any, Coroutine, List

from space_game.canvas.coordinates import (get_max_allowed_canvas_coordinates,
                                           get_random_coordinates)
from space_game.settings import STAR_SYMBOLS
from space_game.stars.animation import blink


def calculate_stars_amount(density: float = 0.05) -> int:
    """Calculate amount of stars based on density per
    1 row x 1 column square for the current canvas.
    """
    height, width = get_max_allowed_canvas_coordinates()
    return int(height * width * density)


def generate_random_stars(
    stars_count: int,
    canvas: Any
) -> List[Coroutine[Any, Any, None]]:
    """Generate blinking stars with random coordinates and offset timeout."""
    stars = []
    for _ in range(stars_count):
        row, col = get_random_coordinates()
        star = blink(
            canvas,
            row,
            col,
            offset_tick_amount=random.randint(1, 200),
            symbol=random.choice(STAR_SYMBOLS),
        )
        stars.append(star)
    return stars
