from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyResponseGETAuthorizeType1")


@_attrs_define
class SpotifyResponseGETAuthorizeType1:
    """
    Attributes:
        error (str):
        state (Union[Unset, str]):
    """

    error: str
    state: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        error = self.error

        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "error": error,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error = d.pop("error")

        state = d.pop("state", UNSET)

        spotify_response_get_authorize_type_1 = cls(
            error=error,
            state=state,
        )

        return spotify_response_get_authorize_type_1
