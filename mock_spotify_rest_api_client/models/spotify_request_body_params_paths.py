from enum import Enum


class SpotifyRequestBodyParamsPaths(str, Enum):
    VALUE_0 = "/playlists/:id/tracks"
    VALUE_1 = "/me/albums"
    VALUE_2 = "/me/episodes"
    VALUE_3 = "/me/following"
    VALUE_4 = "/me/player"
    VALUE_5 = "/me/player/play"
    VALUE_6 = "/playlists/:id/followers"
    VALUE_7 = "/me/tracks"

    def __str__(self) -> str:
        return str(self.value)
