from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETMeepisodes")


@_attrs_define
class SpotifyRequestQueryParamsGETMeepisodes:
    """
    Attributes:
        limit (Union[Unset, float]):
        offset (Union[Unset, float]):
        market (Union[Unset, str]):
    """

    limit: Union[Unset, float] = UNSET
    offset: Union[Unset, float] = UNSET
    market: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit

        offset = self.offset

        market = self.market

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if market is not UNSET:
            field_dict["market"] = market

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        market = d.pop("market", UNSET)

        spotify_request_query_params_get_meepisodes = cls(
            limit=limit,
            offset=offset,
            market=market,
        )

        return spotify_request_query_params_get_meepisodes
