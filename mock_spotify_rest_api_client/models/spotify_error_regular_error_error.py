from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyErrorRegularErrorError")


@_attrs_define
class SpotifyErrorRegularErrorError:
    """
    Attributes:
        status (float):
        message (str):
        reason (Union[Unset, str]):
    """

    status: float
    message: str
    reason: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status = self.status

        message = self.message

        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "status": status,
                "message": message,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status")

        message = d.pop("message")

        reason = d.pop("reason", UNSET)

        spotify_error_regular_error_error = cls(
            status=status,
            message=message,
            reason=reason,
        )

        return spotify_error_regular_error_error
