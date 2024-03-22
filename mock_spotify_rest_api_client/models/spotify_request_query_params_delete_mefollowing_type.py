from enum import Enum


class SpotifyRequestQueryParamsDELETEMefollowingType(str, Enum):
    ARTIST = "artist"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
