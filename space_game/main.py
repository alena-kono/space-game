import curses
import time
from typing import Any

from space_game.canvas.frame import get_frames_from_dir
from space_game.garbage.generator import fill_orbit_with_garbage
from space_game.global_objects import space_objects
from space_game.settings import (CURSOR_STATE, GARBAGE_DIR, STARS_DENSITY,
                                 TIC_TIMEOUT)
from space_game.spaceship.animate import animate_spaceship, run_spaceship
from space_game.stars.generator import (calculate_stars_amount,
                                        generate_random_stars)


def draw(canvas: Any) -> None:
    """Start and run the space game in the terminal."""
    curses.curs_set(CURSOR_STATE)
    canvas.border()
    canvas.nodelay(True)

    stars_count = calculate_stars_amount(density=STARS_DENSITY)

    space_objects.extend(generate_random_stars(
        stars_count=stars_count,
        canvas=canvas,
    ))
    garbage_frames = get_frames_from_dir(GARBAGE_DIR)

    space_objects.append(animate_spaceship())
    space_objects.append(run_spaceship(canvas))
    space_objects.append(fill_orbit_with_garbage(canvas, garbage_frames))

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
