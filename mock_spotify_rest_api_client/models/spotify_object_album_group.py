from enum import Enum


class SpotifyObjectAlbumGroup(str, Enum):
    ALBUM = "album"
    APPEARS_ON = "appears_on"
    COMPILATION = "compilation"
    SINGLE = "single"

    def __str__(self) -> str:
        return str(self.value)
