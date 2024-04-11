from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.spotify_request_query_params_get_metoptracks_time_range import (
    SpotifyRequestQueryParamsGETMetoptracksTimeRange,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETMetoptracks")


@_attrs_define
class SpotifyRequestQueryParamsGETMetoptracks:
    """
    Attributes:
        limit (Union[Unset, float]):
        offset (Union[Unset, float]):
        time_range (Union[Unset, SpotifyRequestQueryParamsGETMetoptracksTimeRange]):
    """

    limit: Union[Unset, float] = UNSET
    offset: Union[Unset, float] = UNSET
    time_range: Union[Unset, SpotifyRequestQueryParamsGETMetoptracksTimeRange] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit

        offset = self.offset

        time_range: Union[Unset, str] = UNSET
        if not isinstance(self.time_range, Unset):
            time_range = self.time_range.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if time_range is not UNSET:
            field_dict["time_range"] = time_range

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        _time_range = d.pop("time_range", UNSET)
        time_range: Union[Unset, SpotifyRequestQueryParamsGETMetoptracksTimeRange]
        if isinstance(_time_range, Unset):
            time_range = UNSET
        else:
            time_range = SpotifyRequestQueryParamsGETMetoptracksTimeRange(_time_range)

        spotify_request_query_params_get_metoptracks = cls(
            limit=limit,
            offset=offset,
            time_range=time_range,
        )

        return spotify_request_query_params_get_metoptracks
