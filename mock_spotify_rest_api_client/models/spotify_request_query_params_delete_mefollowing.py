from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.spotify_request_query_params_delete_mefollowing_type import (
    SpotifyRequestQueryParamsDELETEMefollowingType,
)

T = TypeVar("T", bound="SpotifyRequestQueryParamsDELETEMefollowing")


@_attrs_define
class SpotifyRequestQueryParamsDELETEMefollowing:
    """
    Attributes:
        ids (str):
        type (SpotifyRequestQueryParamsDELETEMefollowingType):
    """

    ids: str
    type: SpotifyRequestQueryParamsDELETEMefollowingType

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

        type = SpotifyRequestQueryParamsDELETEMefollowingType(d.pop("type"))

        spotify_request_query_params_delete_mefollowing = cls(
            ids=ids,
            type=type,
        )

        return spotify_request_query_params_delete_mefollowing
