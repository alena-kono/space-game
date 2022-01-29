from typing import List

from space_game.settings import (SPACESHIP_FRAME_0_FILENAME,
                                 SPACESHIP_FRAME_1_FILENAME)
from space_game.utilities.read_file import read_file


def get_spaceship_frames() -> List[str]:
    """Read frames of a spaceship from files."""
    return [
        read_file(SPACESHIP_FRAME_0_FILENAME),
        read_file(SPACESHIP_FRAME_1_FILENAME),
    ]
