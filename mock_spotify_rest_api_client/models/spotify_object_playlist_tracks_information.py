from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyObjectPlaylistTracksInformation")


@_attrs_define
class SpotifyObjectPlaylistTracksInformation:
    """
    Attributes:
        href (str):
        total (float):
    """

    href: str
    total: float

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "href": href,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        href = d.pop("href")

        total = d.pop("total")

        spotify_object_playlist_tracks_information = cls(
            href=href,
            total=total,
        )

        return spotify_object_playlist_tracks_information
