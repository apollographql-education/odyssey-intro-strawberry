from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_album import SpotifyObjectAlbum


T = TypeVar("T", bound="SpotifyObjectSavedAlbum")


@_attrs_define
class SpotifyObjectSavedAlbum:
    """
    Attributes:
        added_at (str):
        album (SpotifyObjectAlbum):
    """

    added_at: str
    album: "SpotifyObjectAlbum"

    def to_dict(self) -> Dict[str, Any]:
        added_at = self.added_at

        album = self.album.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "added_at": added_at,
                "album": album,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_album import SpotifyObjectAlbum

        d = src_dict.copy()
        added_at = d.pop("added_at")

        album = SpotifyObjectAlbum.from_dict(d.pop("album"))

        spotify_object_saved_album = cls(
            added_at=added_at,
            album=album,
        )

        return spotify_object_saved_album
