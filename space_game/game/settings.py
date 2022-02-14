# Debug mode
DEBUG = True

# Game
GAMEOVER_FRAME_FILENAME = "space_game/static/game/game_over.txt"

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
GARBAGE_OCCURRENCE_FREQUENCY_TICS = 10
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
