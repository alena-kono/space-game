import asyncio
import time
import curses
import random


TIC_TIMEOUT = 0.1
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
        for state, timeout in animation_states:
            canvas.addstr(row, column, symbol, state)
            await sleep_for(n_times=timeout)


def get_random_star_coordinates():
    window = curses.initscr()
    height, width = window.getmaxyx()
    return (random.randint(0, height - 1), random.randint(0, width - 1))


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
    stars = generate_random_stars(stars_count=50, canvas=canvas)
    while True:
        for star in stars:
            star.send(None)
        canvas.refresh()
        time.sleep(TIC_TIMEOUT)


def main():
    curses.update_lines_cols()
    curses.wrapper(draw)


if __name__ == "__main__":
    main()
