from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spotify_request_body_params_put_meplayerplay_offset import (
        SpotifyRequestBodyParamsPUTMeplayerplayOffset,
    )


T = TypeVar("T", bound="SpotifyRequestBodyParamsPUTMeplayerplay")


@_attrs_define
class SpotifyRequestBodyParamsPUTMeplayerplay:
    """
    Attributes:
        context_uri (Union[Unset, str]):
        uris (Union[Unset, List[str]]):
        offset (Union[Unset, SpotifyRequestBodyParamsPUTMeplayerplayOffset]):
        position_ms (Union[Unset, float]):
    """

    context_uri: Union[Unset, str] = UNSET
    uris: Union[Unset, List[str]] = UNSET
    offset: Union[Unset, "SpotifyRequestBodyParamsPUTMeplayerplayOffset"] = UNSET
    position_ms: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        context_uri = self.context_uri

        uris: Union[Unset, List[str]] = UNSET
        if not isinstance(self.uris, Unset):
            uris = self.uris

        offset: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.offset, Unset):
            offset = self.offset.to_dict()

        position_ms = self.position_ms

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if context_uri is not UNSET:
            field_dict["context_uri"] = context_uri
        if uris is not UNSET:
            field_dict["uris"] = uris
        if offset is not UNSET:
            field_dict["offset"] = offset
        if position_ms is not UNSET:
            field_dict["position_ms"] = position_ms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_request_body_params_put_meplayerplay_offset import (
            SpotifyRequestBodyParamsPUTMeplayerplayOffset,
        )

        d = src_dict.copy()
        context_uri = d.pop("context_uri", UNSET)

        uris = cast(List[str], d.pop("uris", UNSET))

        _offset = d.pop("offset", UNSET)
        offset: Union[Unset, SpotifyRequestBodyParamsPUTMeplayerplayOffset]
        if isinstance(_offset, Unset):
            offset = UNSET
        else:
            offset = SpotifyRequestBodyParamsPUTMeplayerplayOffset.from_dict(_offset)

        position_ms = d.pop("position_ms", UNSET)

        spotify_request_body_params_put_meplayerplay = cls(
            context_uri=context_uri,
            uris=uris,
            offset=offset,
            position_ms=position_ms,
        )

        return spotify_request_body_params_put_meplayerplay
