from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsPOSTPlaylistsidtracks")


@_attrs_define
class SpotifyRequestQueryParamsPOSTPlaylistsidtracks:
    """
    Attributes:
        position (Union[Unset, float]):
        uris (Union[Unset, List[str]]):
    """

    position: Union[Unset, float] = UNSET
    uris: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        position = self.position

        uris: Union[Unset, List[str]] = UNSET
        if not isinstance(self.uris, Unset):
            uris = self.uris

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if uris is not UNSET:
            field_dict["uris"] = uris

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        position = d.pop("position", UNSET)

        uris = cast(List[str], d.pop("uris", UNSET))

        spotify_request_query_params_post_playlistsidtracks = cls(
            position=position,
            uris=uris,
        )

        return spotify_request_query_params_post_playlistsidtracks
