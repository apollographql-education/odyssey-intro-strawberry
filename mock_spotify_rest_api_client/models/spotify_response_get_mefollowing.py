from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_paginated_cursor_based_spotify_object_artist import (
        SpotifyObjectPaginatedCursorBasedSpotifyObjectArtist,
    )


T = TypeVar("T", bound="SpotifyResponseGETMefollowing")


@_attrs_define
class SpotifyResponseGETMefollowing:
    """
    Attributes:
        artists (SpotifyObjectPaginatedCursorBasedSpotifyObjectArtist):
    """

    artists: "SpotifyObjectPaginatedCursorBasedSpotifyObjectArtist"

    def to_dict(self) -> Dict[str, Any]:
        artists = self.artists.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "artists": artists,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_paginated_cursor_based_spotify_object_artist import (
            SpotifyObjectPaginatedCursorBasedSpotifyObjectArtist,
        )

        d = src_dict.copy()
        artists = SpotifyObjectPaginatedCursorBasedSpotifyObjectArtist.from_dict(
            d.pop("artists")
        )

        spotify_response_get_mefollowing = cls(
            artists=artists,
        )

        return spotify_response_get_mefollowing
