from space_game.game.chronology import get_current_year
from space_game.game.globals import score
from space_game.game.settings import (SCORE_PER_TIME,
                                      SCORING_IN_YEARS_DIVISIBLE_BY_VALUE,
                                      YEAR_CHANGE_FREQUENCY_TICS)
from space_game.utilities.async_tools import sleep_for


async def keep_track_of_score() -> None:
    """Keep track of a game score by adding SCORE_PER_TIME
    scores every SCORING_EVERY_YEARS_AMOUNT years.
    """
    global score
    while True:
        year = get_current_year()
        await sleep_for(YEAR_CHANGE_FREQUENCY_TICS)
        if year % SCORING_IN_YEARS_DIVISIBLE_BY_VALUE == 0:
            score += SCORE_PER_TIME


def get_current_score() -> int:
    """Get current game score."""
    return int(score)


def add_score(score_amount: int) -> None:
    """Add score_amount to the global score."""
    global score
    score += score_amount
