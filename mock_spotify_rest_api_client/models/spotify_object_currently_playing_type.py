from enum import Enum


class SpotifyObjectCurrentlyPlayingType(str, Enum):
    AD = "ad"
    EPISODE = "episode"
    TRACK = "track"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
