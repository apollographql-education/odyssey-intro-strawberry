from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsPOSTMeplayernext")


@_attrs_define
class SpotifyRequestQueryParamsPOSTMeplayernext:
    """
    Attributes:
        device_id (Union[Unset, str]):
    """

    device_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        device_id = self.device_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["device_id"] = device_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        device_id = d.pop("device_id", UNSET)

        spotify_request_query_params_post_meplayernext = cls(
            device_id=device_id,
        )

        return spotify_request_query_params_post_meplayernext
