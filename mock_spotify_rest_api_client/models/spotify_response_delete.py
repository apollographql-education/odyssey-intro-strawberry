from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_response_delete_playlistsidtracks import (
        SpotifyResponseDELETEPlaylistsidtracks,
    )


T = TypeVar("T", bound="SpotifyResponseDELETE")


@_attrs_define
class SpotifyResponseDELETE:
    """
    Attributes:
        playlistsidtracks (SpotifyResponseDELETEPlaylistsidtracks):
    """

    playlistsidtracks: "SpotifyResponseDELETEPlaylistsidtracks"

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
        from ..models.spotify_response_delete_playlistsidtracks import (
            SpotifyResponseDELETEPlaylistsidtracks,
        )

        d = src_dict.copy()
        playlistsidtracks = SpotifyResponseDELETEPlaylistsidtracks.from_dict(
            d.pop("/playlists/:id/tracks")
        )

        spotify_response_delete = cls(
            playlistsidtracks=playlistsidtracks,
        )

        return spotify_response_delete
