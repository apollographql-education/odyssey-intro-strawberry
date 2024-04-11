from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyObjectExternalUrl")


@_attrs_define
class SpotifyObjectExternalUrl:
    """
    Attributes:
        spotify (str):
    """

    spotify: str

    def to_dict(self) -> Dict[str, Any]:
        spotify = self.spotify

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "spotify": spotify,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        spotify = d.pop("spotify")

        spotify_object_external_url = cls(
            spotify=spotify,
        )

        return spotify_object_external_url
