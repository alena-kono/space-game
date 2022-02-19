import curses
import time
from typing import Any

from space_game.canvas.info_window import get_info_window
from space_game.game.chronology import keep_countdown_of_years
from space_game.game.globals import game_objects, obstacles
from space_game.game.scenario import show_info_message
from space_game.game.score import keep_track_of_score
from space_game.game.settings import (CURSOR_STATE, DEBUG, GAME_START_YEAR,
                                      STARS_DENSITY, TIC_TIMEOUT)
from space_game.garbage.generator import fill_orbit_with_garbage
from space_game.obstacles.obstacles import show_obstacles
from space_game.spaceship.animation import animate_spaceship, run_spaceship
from space_game.stars.generator import (calculate_stars_amount,
                                        generate_random_stars)


def draw(canvas: Any) -> None:
    """Start and run the space game in the terminal."""
    curses.curs_set(CURSOR_STATE)
    canvas.border()
    canvas.nodelay(True)

    info_window = get_info_window(canvas)

    stars_count = calculate_stars_amount(density=STARS_DENSITY)

    game_objects.extend(generate_random_stars(
        stars_count=stars_count,
        canvas=canvas,
    ))
    game_objects.append(keep_countdown_of_years(GAME_START_YEAR))
    game_objects.append(show_info_message(info_window))
    game_objects.append(keep_track_of_score())

    game_objects.append(animate_spaceship())
    game_objects.append(run_spaceship(canvas))
    game_objects.append(fill_orbit_with_garbage(canvas))
    if DEBUG:
        game_objects.append(show_obstacles(canvas, obstacles))

    while True:
        exhausted_coroutines = []
        for game_object in game_objects:
            try:
                game_object.send(None)
            except StopIteration:
                exhausted_coroutines.append(game_object)
        canvas.border()
        canvas.refresh()
        time.sleep(TIC_TIMEOUT)

        for coroutine in exhausted_coroutines:
            game_objects.remove(coroutine)


def main() -> None:
    """Initialize curses."""
    curses.update_lines_cols()
    curses.wrapper(draw)


if __name__ == "__main__":
    main()
