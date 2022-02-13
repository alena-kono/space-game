from typing import Any, Coroutine, List

from space_game.obstacles.obstacles import Obstacle

space_objects: List[Coroutine[Any, Any, None]] = []
spaceship: str = ""

obstacles: List[Obstacle] = []
