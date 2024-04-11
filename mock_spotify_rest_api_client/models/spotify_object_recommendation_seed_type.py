from enum import Enum


class SpotifyObjectRecommendationSeedType(str, Enum):
    ARTIST = "ARTIST"
    GENRE = "GENRE"
    TRACK = "TRACK"

    def __str__(self) -> str:
        return str(self.value)
