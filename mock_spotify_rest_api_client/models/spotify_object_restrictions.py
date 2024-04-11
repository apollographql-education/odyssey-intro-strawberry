from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.spotify_object_restrictions_reason import SpotifyObjectRestrictionsReason

T = TypeVar("T", bound="SpotifyObjectRestrictions")


@_attrs_define
class SpotifyObjectRestrictions:
    """
    Attributes:
        reason (SpotifyObjectRestrictionsReason):
    """

    reason: SpotifyObjectRestrictionsReason

    def to_dict(self) -> Dict[str, Any]:
        reason = self.reason.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reason = SpotifyObjectRestrictionsReason(d.pop("reason"))

        spotify_object_restrictions = cls(
            reason=reason,
        )

        return spotify_object_restrictions
