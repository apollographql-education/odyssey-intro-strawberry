from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyResponsePOSTPlaylistsidtracks")


@_attrs_define
class SpotifyResponsePOSTPlaylistsidtracks:
    """
    Attributes:
        snapshot_id (str):
    """

    snapshot_id: str

    def to_dict(self) -> Dict[str, Any]:
        snapshot_id = self.snapshot_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "snapshot_id": snapshot_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        snapshot_id = d.pop("snapshot_id")

        spotify_response_post_playlistsidtracks = cls(
            snapshot_id=snapshot_id,
        )

        return spotify_response_post_playlistsidtracks
