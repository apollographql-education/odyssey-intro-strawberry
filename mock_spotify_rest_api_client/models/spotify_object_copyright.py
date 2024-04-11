from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.spotify_object_copyright_type import SpotifyObjectCopyrightType

T = TypeVar("T", bound="SpotifyObjectCopyright")


@_attrs_define
class SpotifyObjectCopyright:
    """
    Attributes:
        text (str):
        type (SpotifyObjectCopyrightType):
    """

    text: str
    type: SpotifyObjectCopyrightType

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "text": text,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        type = SpotifyObjectCopyrightType(d.pop("type"))

        spotify_object_copyright = cls(
            text=text,
            type=type,
        )

        return spotify_object_copyright
