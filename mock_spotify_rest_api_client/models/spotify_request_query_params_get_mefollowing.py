from typing import Any, Dict, Literal, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETMefollowing")


@_attrs_define
class SpotifyRequestQueryParamsGETMefollowing:
    """
    Attributes:
        type (Literal['artist']):
        after (Union[Unset, str]):
        limit (Union[Unset, float]):
    """

    type: Literal["artist"]
    after: Union[Unset, str] = UNSET
    limit: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        after = self.after

        limit = self.limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )
        if after is not UNSET:
            field_dict["after"] = after
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        after = d.pop("after", UNSET)

        limit = d.pop("limit", UNSET)

        spotify_request_query_params_get_mefollowing = cls(
            type=type,
            after=after,
            limit=limit,
        )

        return spotify_request_query_params_get_mefollowing
