from enum import Enum


class SpotifyObjectContextType(str, Enum):
    ALBUM = "album"
    ARTIST = "artist"
    PLAYLIST = "playlist"
    SHOW = "show"

    def __str__(self) -> str:
        return str(self.value)
