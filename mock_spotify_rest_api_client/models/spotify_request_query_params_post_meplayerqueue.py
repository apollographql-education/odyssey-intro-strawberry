from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsPOSTMeplayerqueue")


@_attrs_define
class SpotifyRequestQueryParamsPOSTMeplayerqueue:
    """
    Attributes:
        uri (str):
        device_id (Union[Unset, str]):
    """

    uri: str
    device_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        uri = self.uri

        device_id = self.device_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "uri": uri,
            }
        )
        if device_id is not UNSET:
            field_dict["device_id"] = device_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uri = d.pop("uri")

        device_id = d.pop("device_id", UNSET)

        spotify_request_query_params_post_meplayerqueue = cls(
            uri=uri,
            device_id=device_id,
        )

        return spotify_request_query_params_post_meplayerqueue
