from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.spotify_request_query_params_put_mefollowing_type import (
    SpotifyRequestQueryParamsPUTMefollowingType,
)

T = TypeVar("T", bound="SpotifyRequestQueryParamsPUTMefollowing")


@_attrs_define
class SpotifyRequestQueryParamsPUTMefollowing:
    """
    Attributes:
        ids (str):
        type (SpotifyRequestQueryParamsPUTMefollowingType):
    """

    ids: str
    type: SpotifyRequestQueryParamsPUTMefollowingType

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

        type = SpotifyRequestQueryParamsPUTMefollowingType(d.pop("type"))

        spotify_request_query_params_put_mefollowing = cls(
            ids=ids,
            type=type,
        )

        return spotify_request_query_params_put_mefollowing
