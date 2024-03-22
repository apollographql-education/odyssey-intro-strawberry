from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_response_post_playlistsidtracks import (
        SpotifyResponsePOSTPlaylistsidtracks,
    )


T = TypeVar("T", bound="SpotifyResponsePOST")


@_attrs_define
class SpotifyResponsePOST:
    """
    Attributes:
        playlistsidtracks (SpotifyResponsePOSTPlaylistsidtracks):
    """

    playlistsidtracks: "SpotifyResponsePOSTPlaylistsidtracks"

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
        from ..models.spotify_response_post_playlistsidtracks import (
            SpotifyResponsePOSTPlaylistsidtracks,
        )

        d = src_dict.copy()
        playlistsidtracks = SpotifyResponsePOSTPlaylistsidtracks.from_dict(
            d.pop("/playlists/:id/tracks")
        )

        spotify_response_post = cls(
            playlistsidtracks=playlistsidtracks,
        )

        return spotify_response_post
