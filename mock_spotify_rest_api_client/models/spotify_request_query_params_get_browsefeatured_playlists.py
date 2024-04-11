from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETBrowsefeaturedPlaylists")


@_attrs_define
class SpotifyRequestQueryParamsGETBrowsefeaturedPlaylists:
    """
    Attributes:
        limit (Union[Unset, float]):
        offset (Union[Unset, float]):
        timestamp (Union[Unset, str]):
    """

    limit: Union[Unset, float] = UNSET
    offset: Union[Unset, float] = UNSET
    timestamp: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit

        offset = self.offset

        timestamp = self.timestamp

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        spotify_request_query_params_get_browsefeatured_playlists = cls(
            limit=limit,
            offset=offset,
            timestamp=timestamp,
        )

        return spotify_request_query_params_get_browsefeatured_playlists
