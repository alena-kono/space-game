import curses
import time
from typing import Any

from space_game.settings import TIC_TIMEOUT
from space_game.spaceship.animate import animate_spaceship, run_spaceship
from space_game.stars.generator import (calculate_optimal_stars_count,
                                        generate_random_stars)


def draw(canvas: Any) -> None:
    """Start and run the space game in the terminal."""
    curses.curs_set(False)
    canvas.border()
    canvas.nodelay(True)

    stars_count = calculate_optimal_stars_count()

    space_objects = generate_random_stars(
        stars_count=stars_count,
        canvas=canvas,
    )
    space_objects.append(animate_spaceship())
    space_objects.append(run_spaceship(canvas))

    while True:
        exhausted_coroutines = []
        for space_object in space_objects:
            try:
                space_object.send(None)
            except StopIteration:
                exhausted_coroutines.append(space_object)
        canvas.border()
        canvas.refresh()
        time.sleep(TIC_TIMEOUT)

        for coroutine in exhausted_coroutines:
            space_objects.remove(coroutine)


def main() -> None:
    """Initialize curses."""
    curses.update_lines_cols()
    curses.wrapper(draw)


if __name__ == "__main__":
    main()
