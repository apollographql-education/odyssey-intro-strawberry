from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyRequestBodyParamsDELETEPlaylistsidtracksTracksItem")


@_attrs_define
class SpotifyRequestBodyParamsDELETEPlaylistsidtracksTracksItem:
    """
    Attributes:
        uri (str):
    """

    uri: str

    def to_dict(self) -> Dict[str, Any]:
        uri = self.uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uri = d.pop("uri")

        spotify_request_body_params_delete_playlistsidtracks_tracks_item = cls(
            uri=uri,
        )

        return spotify_request_body_params_delete_playlistsidtracks_tracks_item
