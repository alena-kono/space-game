import random
from typing import Any, List

from space_game.canvas.coordinates import get_random_coordinates
from space_game.game.chronology import get_current_year
from space_game.game.globals import space_objects
from space_game.game.scenario import get_garbage_delay_tics
from space_game.garbage.animation import fly_garbage
from space_game.utilities.async_tools import sleep_for


async def fill_orbit_with_garbage(
    canvas: Any,
    garbage_frames: List[str],
) -> None:
    """Fill orbit with garbage randomly."""
    while True:
        year = get_current_year()
        current_year_delay_tics = get_garbage_delay_tics(year)

        if current_year_delay_tics:
            random_frame = random.choice(garbage_frames)
            random_column = get_random_coordinates()[1]
            space_objects.append(
                fly_garbage(canvas, random_column, random_frame)
            )
        await sleep_for(current_year_delay_tics or 1)
