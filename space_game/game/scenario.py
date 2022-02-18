import asyncio
from typing import Any, Optional

from space_game.canvas.frame import draw_frame
from space_game.game.chronology import get_current_year
from space_game.game.settings import INFO_MESSAGE_COORDINATES

PHRASES = {
    1957: "First Sputnik",
    1961: "Gagarin flew!",
    1969: "Armstrong got on the moon!",
    1971: "First orbital space station Salute-1",
    1981: "Flight of the Shuttle Columbia",
    1998: 'ISS start building',
    2011: 'Messenger launch to Mercury',
    2020: "Take the plasma gun! Shoot the garbage!",
}


def get_garbage_delay_tics(year: int) -> Optional[int]:
    """Get garbage delay tics based on the year."""
    if year < 1961:
        return None
    elif year < 1969:
        return 20
    elif year < 1981:
        return 14
    elif year < 1995:
        return 10
    elif year < 2010:
        return 8
    elif year < 2020:
        return 6
    else:
        return 2


async def show_info_message(canvas: Any) -> None:
    """Show info message - year and the related event."""
    row, column = INFO_MESSAGE_COORDINATES
    message_template = "Year {year}\n{text}"
    while True:
        year = get_current_year()
        text = message_template.format(
                year=year,
                text=PHRASES.get(year, "")
                )
        draw_frame(canvas, row, column, text)
        await asyncio.sleep(0)
        draw_frame(canvas, row, column, text, negative=True)
