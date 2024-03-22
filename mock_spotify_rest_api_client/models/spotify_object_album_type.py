from enum import Enum


class SpotifyObjectAlbumType(str, Enum):
    ALBUM = "album"
    COMPILATION = "compilation"
    SINGLE = "single"

    def __str__(self) -> str:
        return str(self.value)
