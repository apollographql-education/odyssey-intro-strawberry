from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyObjectPlaylistTrackVideoThumbnail")


@_attrs_define
class SpotifyObjectPlaylistTrackVideoThumbnail:
    """
    Attributes:
        url (Union[None, str]):
    """

    url: Union[None, str]

    def to_dict(self) -> Dict[str, Any]:
        url: Union[None, str]
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        url = _parse_url(d.pop("url"))

        spotify_object_playlist_track_video_thumbnail = cls(
            url=url,
        )

        return spotify_object_playlist_track_video_thumbnail
