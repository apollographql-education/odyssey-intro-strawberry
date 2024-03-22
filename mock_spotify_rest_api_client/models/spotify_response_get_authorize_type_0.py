from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyResponseGETAuthorizeType0")


@_attrs_define
class SpotifyResponseGETAuthorizeType0:
    """
    Attributes:
        code (str):
        state (Union[Unset, str]):
    """

    code: str
    state: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "code": code,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code")

        state = d.pop("state", UNSET)

        spotify_response_get_authorize_type_0 = cls(
            code=code,
            state=state,
        )

        return spotify_response_get_authorize_type_0
