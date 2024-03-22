from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestBodyParamsPUTMeplayer")


@_attrs_define
class SpotifyRequestBodyParamsPUTMeplayer:
    """
    Attributes:
        device_ids (List[str]):
        play (Union[Unset, bool]):
    """

    device_ids: List[str]
    play: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        device_ids = self.device_ids

        play = self.play

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "device_ids": device_ids,
            }
        )
        if play is not UNSET:
            field_dict["play"] = play

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        device_ids = cast(List[str], d.pop("device_ids"))

        play = d.pop("play", UNSET)

        spotify_request_body_params_put_meplayer = cls(
            device_ids=device_ids,
            play=play,
        )

        return spotify_request_body_params_put_meplayer
