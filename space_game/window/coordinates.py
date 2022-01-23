import curses


def _get_window_size():
    return curses.initscr().getmaxyx()


def get_max_window_coordinates():
    window_height, window_width = _get_window_size()
    return (window_height - 1, window_width - 1)


def get_middle_window_coordinates():
    window_height, window_width = _get_window_size()
    return (window_height // 2, window_width // 2)
