from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyObjectCursors")


@_attrs_define
class SpotifyObjectCursors:
    """
    Attributes:
        after (Union[Unset, str]):
        before (Union[Unset, str]):
    """

    after: Union[Unset, str] = UNSET
    before: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        after = self.after

        before = self.before

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if after is not UNSET:
            field_dict["after"] = after
        if before is not UNSET:
            field_dict["before"] = before

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        after = d.pop("after", UNSET)

        before = d.pop("before", UNSET)

        spotify_object_cursors = cls(
            after=after,
            before=before,
        )

        return spotify_object_cursors
