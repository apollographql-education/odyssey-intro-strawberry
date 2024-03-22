from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsPUTMeplayervolume")


@_attrs_define
class SpotifyRequestQueryParamsPUTMeplayervolume:
    """
    Attributes:
        volume_percent (float):
        device_id (Union[Unset, str]):
    """

    volume_percent: float
    device_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        volume_percent = self.volume_percent

        device_id = self.device_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "volume_percent": volume_percent,
            }
        )
        if device_id is not UNSET:
            field_dict["device_id"] = device_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        volume_percent = d.pop("volume_percent")

        device_id = d.pop("device_id", UNSET)

        spotify_request_query_params_put_meplayervolume = cls(
            volume_percent=volume_percent,
            device_id=device_id,
        )

        return spotify_request_query_params_put_meplayervolume
