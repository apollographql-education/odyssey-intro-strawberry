from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETMeplayer")


@_attrs_define
class SpotifyRequestQueryParamsGETMeplayer:
    """
    Attributes:
        additional_types (Union[Unset, str]):
    """

    additional_types: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        additional_types = self.additional_types

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if additional_types is not UNSET:
            field_dict["additional_types"] = additional_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        additional_types = d.pop("additional_types", UNSET)

        spotify_request_query_params_get_meplayer = cls(
            additional_types=additional_types,
        )

        return spotify_request_query_params_get_meplayer
