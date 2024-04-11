from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestBodyParamsPUTMefollowing")


@_attrs_define
class SpotifyRequestBodyParamsPUTMefollowing:
    """
    Attributes:
        ids (Union[Unset, List[str]]):
    """

    ids: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if ids is not UNSET:
            field_dict["ids"] = ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ids = cast(List[str], d.pop("ids", UNSET))

        spotify_request_body_params_put_mefollowing = cls(
            ids=ids,
        )

        return spotify_request_body_params_put_mefollowing
