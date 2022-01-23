import asyncio
import curses
import random
import time

from space_game.window.coordinates import (get_max_window_coordinates,
                                           get_middle_window_coordinates)

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


async def blink(canvas, row, column, offset_tick_amount, symbol="*"):
    animation_states = generate_animation_states()

    state, timeout = animation_states[0]
    canvas.addstr(row, column, symbol, state)
    await asyncio.sleep(0)

    await sleep_for(offset_tick_amount)
    while True:
        for state, timeout in animation_states:
            canvas.addstr(row, column, symbol, state)
            await sleep_for(timeout)


def get_random_star_coordinates():
    max_height, max_width = get_max_window_coordinates()
    return (random.randint(0, max_height), random.randint(0, max_width))


def calculate_optimal_stars_count():
    height, width = get_max_window_coordinates()
    ratio = 125
    return int(height * width / ratio)


def generate_random_stars(stars_count: int, canvas):
    stars = []
    for _ in range(stars_count):
        row, col = get_random_star_coordinates()
        star = blink(
            canvas,
            row,
            col,
            offset_tick_amount=random.randint(1, 200),
            symbol=random.choice(STAR_SYMBOLS),
        )
        stars.append(star)
    return stars


async def fire(canvas, start_row, start_column, rows_speed=-0.3, columns_speed=0):
    """Display animation of gun shot, direction and speed can be specified."""

    row, column = start_row, start_column

    canvas.addstr(round(row), round(column), '*')
    await asyncio.sleep(0)

    canvas.addstr(round(row), round(column), 'O')
    await asyncio.sleep(0)
    canvas.addstr(round(row), round(column), ' ')

    row += rows_speed
    column += columns_speed

    symbol = '-' if columns_speed else '|'

    rows, columns = canvas.getmaxyx()
    max_row, max_column = rows - 1, columns - 1

    curses.beep()

    while 0 < row < max_row and 0 < column < max_column:
        canvas.addstr(round(row), round(column), symbol)
        await asyncio.sleep(0)
        canvas.addstr(round(row), round(column), ' ')
        row += rows_speed
        column += columns_speed


def draw(canvas):
    curses.curs_set(False)
    canvas.border()
    stars_count = calculate_optimal_stars_count()

    space_objects = generate_random_stars(stars_count=stars_count, canvas=canvas)
    space_objects.append(fire(canvas, *get_middle_window_coordinates()))

    while True:
        exhausted_coroutines = []
        for space_object in space_objects:
            try:
                space_object.send(None)
            except StopIteration:
                exhausted_coroutines.append(space_object)
        canvas.border()
        canvas.refresh()
        time.sleep(TIC_TIMEOUT)

        for coroutine in exhausted_coroutines:
            space_objects.remove(coroutine)


def main():
    curses.update_lines_cols()
    curses.wrapper(draw)


if __name__ == "__main__":
    main()
