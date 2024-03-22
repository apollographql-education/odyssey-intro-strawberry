from enum import Enum


class SpotifyObjectRepeatMode(str, Enum):
    CONTEXT = "context"
    OFF = "off"
    TRACK = "track"

    def __str__(self) -> str:
        return str(self.value)
