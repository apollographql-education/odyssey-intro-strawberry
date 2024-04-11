from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETMeplayerrecentlyPlayed")


@_attrs_define
class SpotifyRequestQueryParamsGETMeplayerrecentlyPlayed:
    """
    Attributes:
        after (Union[Unset, float]):
        before (Union[Unset, float]):
        limit (Union[Unset, float]):
    """

    after: Union[Unset, float] = UNSET
    before: Union[Unset, float] = UNSET
    limit: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        after = self.after

        before = self.before

        limit = self.limit

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if after is not UNSET:
            field_dict["after"] = after
        if before is not UNSET:
            field_dict["before"] = before
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        after = d.pop("after", UNSET)

        before = d.pop("before", UNSET)

        limit = d.pop("limit", UNSET)

        spotify_request_query_params_get_meplayerrecently_played = cls(
            after=after,
            before=before,
            limit=limit,
        )

        return spotify_request_query_params_get_meplayerrecently_played
