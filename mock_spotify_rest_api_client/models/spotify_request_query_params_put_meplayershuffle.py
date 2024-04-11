from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsPUTMeplayershuffle")


@_attrs_define
class SpotifyRequestQueryParamsPUTMeplayershuffle:
    """
    Attributes:
        state (bool):
        device_id (Union[Unset, str]):
    """

    state: bool
    device_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        state = self.state

        device_id = self.device_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "state": state,
            }
        )
        if device_id is not UNSET:
            field_dict["device_id"] = device_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        state = d.pop("state")

        device_id = d.pop("device_id", UNSET)

        spotify_request_query_params_put_meplayershuffle = cls(
            state=state,
            device_id=device_id,
        )

        return spotify_request_query_params_put_meplayershuffle
