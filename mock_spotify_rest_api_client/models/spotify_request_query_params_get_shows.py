from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETShows")


@_attrs_define
class SpotifyRequestQueryParamsGETShows:
    """
    Attributes:
        ids (str):
        market (Union[Unset, str]):
    """

    ids: str
    market: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        ids = self.ids

        market = self.market

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "ids": ids,
            }
        )
        if market is not UNSET:
            field_dict["market"] = market

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ids = d.pop("ids")

        market = d.pop("market", UNSET)

        spotify_request_query_params_get_shows = cls(
            ids=ids,
            market=market,
        )

        return spotify_request_query_params_get_shows
