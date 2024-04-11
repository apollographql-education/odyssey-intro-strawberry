from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestBodyParamsPUTPlaylistsidfollowers")


@_attrs_define
class SpotifyRequestBodyParamsPUTPlaylistsidfollowers:
    """
    Attributes:
        public (Union[Unset, bool]):
    """

    public: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        public = self.public

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if public is not UNSET:
            field_dict["public"] = public

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        public = d.pop("public", UNSET)

        spotify_request_body_params_put_playlistsidfollowers = cls(
            public=public,
        )

        return spotify_request_body_params_put_playlistsidfollowers
