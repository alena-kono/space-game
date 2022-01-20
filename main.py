import asyncio
import curses
import random
import time

TIC_TIMEOUT = 0.01
STAR_SYMBOLS = "+*.:"


def generate_animation_states():
    return [
      (curses.A_DIM, int(2 / TIC_TIMEOUT)),
      (curses.A_NORMAL, int(0.3 / TIC_TIMEOUT)),
      (curses.A_BOLD, int(0.5 / TIC_TIMEOUT)),
      (curses.A_NORMAL, int(0.3 / TIC_TIMEOUT)),
    ]


async def sleep_for(n_times: int):
    for _ in range(n_times):
        await asyncio.sleep(0)


async def blink(canvas, row, column, symbol="*"):
    animation_states = generate_animation_states()
    while True:
        for state, _ in animation_states:
            canvas.addstr(row, column, symbol, state)
            await asyncio.sleep(0)
            time.sleep(TIC_TIMEOUT)


def get_window_size():
    return curses.initscr().getmaxyx()


def get_random_star_coordinates():
    height, width = get_window_size()
    return (random.randint(0, height - 1), random.randint(0, width - 1))


def calculate_optimal_stars_count():
    height, width = get_window_size()
    ratio = 125
    return int(height * width / ratio)


def generate_random_stars(stars_count: int, canvas):
    stars = []
    for _ in range(stars_count):
        row, col = get_random_star_coordinates()
        star = blink(canvas, row, col, random.choice(STAR_SYMBOLS))
        stars.append(star)
    return stars


def draw(canvas):
    curses.curs_set(False)
    canvas.border()
    stars_count = calculate_optimal_stars_count()
    stars = generate_random_stars(stars_count=stars_count, canvas=canvas)

    for star in stars:
        star.send(None)
        canvas.refresh()
        time.sleep(0)

    while True:
        random_star = random.randint(0, len(stars) - 1)
        stars[random_star].send(None)
        canvas.refresh()
        time.sleep(0)


def main():
    curses.update_lines_cols()
    curses.wrapper(draw)


if __name__ == "__main__":
    main()
