from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestBodyParamsPUTMeplayerplayOffset")


@_attrs_define
class SpotifyRequestBodyParamsPUTMeplayerplayOffset:
    """
    Attributes:
        position (Union[Unset, float]):
        uri (Union[Unset, str]):
    """

    position: Union[Unset, float] = UNSET
    uri: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        position = self.position

        uri = self.uri

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        position = d.pop("position", UNSET)

        uri = d.pop("uri", UNSET)

        spotify_request_body_params_put_meplayerplay_offset = cls(
            position=position,
            uri=uri,
        )

        return spotify_request_body_params_put_meplayerplay_offset
