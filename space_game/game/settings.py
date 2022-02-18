# Debug mode
DEBUG = False

# Game
GAMEOVER_FRAME_FILENAME = "space_game/static/game/game_over.txt"
GAME_START_YEAR = 1957
PLASMA_GUN_START_YEAR = 2020
YEAR_CHANGE_FREQUENCY_TICS = 1

# Stars
TIC_TIMEOUT = 0.1
STAR_SYMBOLS = "+*.:"
STARS_DENSITY = 0.05

# Control keys
SPACE_KEY_CODE = 32
LEFT_KEY_CODE = 260
RIGHT_KEY_CODE = 261
UP_KEY_CODE = 259
DOWN_KEY_CODE = 258

# Spaceship
SPACESHIP_FRAMES_DIR = "space_game/static/spaceship"
FIRE_SHOT_SPEED_ABS = 2

# Garbage
GARBAGE_DIR = "space_game/static/garbage"
EXPLOSION_FRAMES = [
    """\
           (_)
       (  (   (  (
      () (  (  )
        ( )  ()
    """,
    """\
           (_)
       (  (   (
         (  (  )
          )  (
    """,
    """\
            (
          (   (
         (     (
          )  (
    """,
    """\
            (
              (
            (
    """,
]

# Canvas
CURSOR_STATE = False
CANVAS_BORDER_SIZE = 1
INFO_WINDOW_HEIGHT = 4
INFO_MESSAGE_COORDINATES = (2, 2)
