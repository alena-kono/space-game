from typing import Any, Coroutine, List

from space_game.obstacles.obstacles import Obstacle

GameObjects = List[Coroutine[Any, Any, None]]

game_objects: GameObjects = []
spaceship: str = ""

obstacles: List[Obstacle] = []
obstacles_in_last_collisions: List[Obstacle] = []

year: int = 0
