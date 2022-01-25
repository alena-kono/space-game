import random
from typing import Any, Coroutine, List, Tuple

from space_game.settings import STAR_SYMBOLS
from space_game.stars.blink import blink
from space_game.window.coordinates import get_max_window_coordinates


def get_random_star_coordinates() -> Tuple[int, int]:
    """Generate random coordinates of a star."""
    max_height, max_width = get_max_window_coordinates()
    return (random.randint(0, max_height), random.randint(0, max_width))


def calculate_optimal_stars_count() -> int:
    """Calculate amount of stars that is optimal for current window size."""
    height, width = get_max_window_coordinates()
    ratio = 125
    return int(height * width / ratio)


def generate_random_stars(
    stars_count: int,
    canvas: Any
) -> List[Coroutine[Any, Any, None]]:
    """Generate blinking stars with random coordinates and offset timeout."""
    stars = []
    for _ in range(stars_count):
        row, col = get_random_star_coordinates()
        star = blink(
            canvas,
            row,
            col,
            offset_tick_amount=random.randint(1, 200),
            symbol=random.choice(STAR_SYMBOLS),
        )
        stars.append(star)
    return stars
