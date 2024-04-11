from enum import Enum


class SpotifyRequestQueryParamsGETMetopartistsTimeRange(str, Enum):
    LONG_TERM = "long_term"
    MEDIUM_TERM = "medium_term"
    SHORT_TERM = "short_term"

    def __str__(self) -> str:
        return str(self.value)
