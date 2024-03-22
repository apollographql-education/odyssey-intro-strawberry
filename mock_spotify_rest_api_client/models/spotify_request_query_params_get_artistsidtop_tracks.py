from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETArtistsidtopTracks")


@_attrs_define
class SpotifyRequestQueryParamsGETArtistsidtopTracks:
    """
    Attributes:
        market (str):
    """

    market: str

    def to_dict(self) -> Dict[str, Any]:
        market = self.market

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "market": market,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        market = d.pop("market")

        spotify_request_query_params_get_artistsidtop_tracks = cls(
            market=market,
        )

        return spotify_request_query_params_get_artistsidtop_tracks
