import random
from typing import Any, List

from space_game.canvas.coordinates import get_random_coordinates
from space_game.game.globals import space_objects
from space_game.game.settings import GARBAGE_OCCURRENCE_FREQUENCY_TICS
from space_game.garbage.animation import fly_garbage
from space_game.utilities.async_tools import sleep_for


async def fill_orbit_with_garbage(
    canvas: Any,
    garbage_frames: List[str],
) -> None:
    """Fill orbit with garbage randomly."""
    while True:
        random_frame = random.choice(garbage_frames)
        random_column = get_random_coordinates()[1]
        space_objects.append(
                fly_garbage(canvas, random_column, random_frame)
            )
        await sleep_for(GARBAGE_OCCURRENCE_FREQUENCY_TICS)
