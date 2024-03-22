from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestBodyParamsPOSTPlaylistsidtracks")


@_attrs_define
class SpotifyRequestBodyParamsPOSTPlaylistsidtracks:
    """
    Attributes:
        uris (Union[Unset, List[str]]):
        position (Union[Unset, float]):
    """

    uris: Union[Unset, List[str]] = UNSET
    position: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        uris: Union[Unset, List[str]] = UNSET
        if not isinstance(self.uris, Unset):
            uris = self.uris

        position = self.position

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if uris is not UNSET:
            field_dict["uris"] = uris
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uris = cast(List[str], d.pop("uris", UNSET))

        position = d.pop("position", UNSET)

        spotify_request_body_params_post_playlistsidtracks = cls(
            uris=uris,
            position=position,
        )

        return spotify_request_body_params_post_playlistsidtracks
