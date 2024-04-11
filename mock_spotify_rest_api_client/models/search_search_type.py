from enum import Enum


class SearchSearchType(str, Enum):
    ALBUM = "album"
    ARTIST = "artist"
    AUDIOBOOK = "audiobook"
    EPISODE = "episode"
    PLAYLIST = "playlist"
    SHOW = "show"
    TRACK = "track"

    def __str__(self) -> str:
        return str(self.value)
