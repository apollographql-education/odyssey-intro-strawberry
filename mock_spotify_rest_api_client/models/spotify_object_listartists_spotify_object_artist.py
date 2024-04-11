from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_artist import SpotifyObjectArtist


T = TypeVar("T", bound="SpotifyObjectListartistsSpotifyObjectArtist")


@_attrs_define
class SpotifyObjectListartistsSpotifyObjectArtist:
    """
    Attributes:
        artists (List['SpotifyObjectArtist']):
    """

    artists: List["SpotifyObjectArtist"]

    def to_dict(self) -> Dict[str, Any]:
        artists = []
        for artists_item_data in self.artists:
            artists_item = artists_item_data.to_dict()
            artists.append(artists_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "artists": artists,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_artist import SpotifyObjectArtist

        d = src_dict.copy()
        artists = []
        _artists = d.pop("artists")
        for artists_item_data in _artists:
            artists_item = SpotifyObjectArtist.from_dict(artists_item_data)

            artists.append(artists_item)

        spotify_object_listartists_spotify_object_artist = cls(
            artists=artists,
        )

        return spotify_object_listartists_spotify_object_artist
