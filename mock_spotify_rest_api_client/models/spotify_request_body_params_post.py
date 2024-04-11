from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_request_body_params_post_playlistsidtracks import (
        SpotifyRequestBodyParamsPOSTPlaylistsidtracks,
    )


T = TypeVar("T", bound="SpotifyRequestBodyParamsPOST")


@_attrs_define
class SpotifyRequestBodyParamsPOST:
    """
    Attributes:
        playlistsidtracks (SpotifyRequestBodyParamsPOSTPlaylistsidtracks):
    """

    playlistsidtracks: "SpotifyRequestBodyParamsPOSTPlaylistsidtracks"

    def to_dict(self) -> Dict[str, Any]:
        playlistsidtracks = self.playlistsidtracks.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "/playlists/:id/tracks": playlistsidtracks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_request_body_params_post_playlistsidtracks import (
            SpotifyRequestBodyParamsPOSTPlaylistsidtracks,
        )

        d = src_dict.copy()
        playlistsidtracks = SpotifyRequestBodyParamsPOSTPlaylistsidtracks.from_dict(
            d.pop("/playlists/:id/tracks")
        )

        spotify_request_body_params_post = cls(
            playlistsidtracks=playlistsidtracks,
        )

        return spotify_request_body_params_post
