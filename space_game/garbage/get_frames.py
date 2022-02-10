import os
from typing import List

from space_game.settings import GARBAGE_DIR
from space_game.utilities.read_file import read_file


def get_garbage_frames() -> List[str]:
    """Read frames of garbage from files located
    in the directory specified at GARBAGE_DIR setting.
    """
    files = os.listdir(GARBAGE_DIR)
    return [
            read_file(GARBAGE_DIR + "/" + input_file) for input_file in files
            ]
