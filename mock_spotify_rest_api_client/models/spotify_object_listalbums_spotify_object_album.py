from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_album import SpotifyObjectAlbum


T = TypeVar("T", bound="SpotifyObjectListalbumsSpotifyObjectAlbum")


@_attrs_define
class SpotifyObjectListalbumsSpotifyObjectAlbum:
    """
    Attributes:
        albums (List['SpotifyObjectAlbum']):
    """

    albums: List["SpotifyObjectAlbum"]

    def to_dict(self) -> Dict[str, Any]:
        albums = []
        for albums_item_data in self.albums:
            albums_item = albums_item_data.to_dict()
            albums.append(albums_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "albums": albums,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_album import SpotifyObjectAlbum

        d = src_dict.copy()
        albums = []
        _albums = d.pop("albums")
        for albums_item_data in _albums:
            albums_item = SpotifyObjectAlbum.from_dict(albums_item_data)

            albums.append(albums_item)

        spotify_object_listalbums_spotify_object_album = cls(
            albums=albums,
        )

        return spotify_object_listalbums_spotify_object_album
