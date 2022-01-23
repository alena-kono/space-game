import curses
import random

from space_game.settings import STAR_SYMBOLS, TIC_TIMEOUT
from space_game.stars.blink import blink
from space_game.window.coordinates import get_max_window_coordinates


def generate_animation_states():
    return [
      (curses.A_DIM, int(2 / TIC_TIMEOUT)),
      (curses.A_NORMAL, int(0.3 / TIC_TIMEOUT)),
      (curses.A_BOLD, int(0.5 / TIC_TIMEOUT)),
      (curses.A_NORMAL, int(0.3 / TIC_TIMEOUT)),
    ]


def get_random_star_coordinates():
    max_height, max_width = get_max_window_coordinates()
    return (random.randint(0, max_height), random.randint(0, max_width))


def calculate_optimal_stars_count():
    height, width = get_max_window_coordinates()
    ratio = 125
    return int(height * width / ratio)


def generate_random_stars(stars_count: int, canvas):
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
