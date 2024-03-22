from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.spotify_request_query_params_get_mefollowingcontains_type import (
    SpotifyRequestQueryParamsGETMefollowingcontainsType,
)

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETMefollowingcontains")


@_attrs_define
class SpotifyRequestQueryParamsGETMefollowingcontains:
    """
    Attributes:
        ids (str):
        type (SpotifyRequestQueryParamsGETMefollowingcontainsType):
    """

    ids: str
    type: SpotifyRequestQueryParamsGETMefollowingcontainsType

    def to_dict(self) -> Dict[str, Any]:
        ids = self.ids

        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "ids": ids,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ids = d.pop("ids")

        type = SpotifyRequestQueryParamsGETMefollowingcontainsType(d.pop("type"))

        spotify_request_query_params_get_mefollowingcontains = cls(
            ids=ids,
            type=type,
        )

        return spotify_request_query_params_get_mefollowingcontains
