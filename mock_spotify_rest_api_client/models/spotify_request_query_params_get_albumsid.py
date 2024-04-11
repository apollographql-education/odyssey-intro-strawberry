from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETAlbumsid")


@_attrs_define
class SpotifyRequestQueryParamsGETAlbumsid:
    """
    Attributes:
        market (Union[Unset, str]):
    """

    market: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        market = self.market

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        market = d.pop("market", UNSET)

        spotify_request_query_params_get_albumsid = cls(
            market=market,
        )

        return spotify_request_query_params_get_albumsid
