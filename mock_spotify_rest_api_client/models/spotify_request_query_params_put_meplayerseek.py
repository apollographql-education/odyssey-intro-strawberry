from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsPUTMeplayerseek")


@_attrs_define
class SpotifyRequestQueryParamsPUTMeplayerseek:
    """
    Attributes:
        position_ms (float):
        device_id (Union[Unset, str]):
    """

    position_ms: float
    device_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        position_ms = self.position_ms

        device_id = self.device_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "position_ms": position_ms,
            }
        )
        if device_id is not UNSET:
            field_dict["device_id"] = device_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        position_ms = d.pop("position_ms")

        device_id = d.pop("device_id", UNSET)

        spotify_request_query_params_put_meplayerseek = cls(
            position_ms=position_ms,
            device_id=device_id,
        )

        return spotify_request_query_params_put_meplayerseek
