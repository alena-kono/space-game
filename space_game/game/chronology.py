from space_game.game.globals import year
from space_game.game.settings import YEAR_CHANGE_FREQUENCY_TICS
from space_game.utilities.async_tools import sleep_for


async def keep_countdown_of_years(start_year: int) -> None:
    """Keep a countdown of years starting from a start_year."""
    global year
    while True:
        if year < start_year:
            year += start_year
        else:
            year += 1
        await sleep_for(YEAR_CHANGE_FREQUENCY_TICS)


def get_current_year() -> int:
    """Get current year."""
    return int(year)
