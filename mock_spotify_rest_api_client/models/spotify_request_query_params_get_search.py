from typing import Any, Dict, Literal, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETSearch")


@_attrs_define
class SpotifyRequestQueryParamsGETSearch:
    """
    Attributes:
        q (str):
        type (str):
        include_external (Union[Literal['audio'], Unset]):
        limit (Union[Unset, float]):
        market (Union[Unset, str]):
        offset (Union[Unset, float]):
    """

    q: str
    type: str
    include_external: Union[Literal["audio"], Unset] = UNSET
    limit: Union[Unset, float] = UNSET
    market: Union[Unset, str] = UNSET
    offset: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        q = self.q

        type = self.type

        include_external = self.include_external

        limit = self.limit

        market = self.market

        offset = self.offset

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "q": q,
                "type": type,
            }
        )
        if include_external is not UNSET:
            field_dict["include_external"] = include_external
        if limit is not UNSET:
            field_dict["limit"] = limit
        if market is not UNSET:
            field_dict["market"] = market
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        q = d.pop("q")

        type = d.pop("type")

        include_external = d.pop("include_external", UNSET)

        limit = d.pop("limit", UNSET)

        market = d.pop("market", UNSET)

        offset = d.pop("offset", UNSET)

        spotify_request_query_params_get_search = cls(
            q=q,
            type=type,
            include_external=include_external,
            limit=limit,
            market=market,
            offset=offset,
        )

        return spotify_request_query_params_get_search
