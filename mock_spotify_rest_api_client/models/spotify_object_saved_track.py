from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_track import SpotifyObjectTrack


T = TypeVar("T", bound="SpotifyObjectSavedTrack")


@_attrs_define
class SpotifyObjectSavedTrack:
    """
    Attributes:
        added_at (str):
        track (SpotifyObjectTrack):
    """

    added_at: str
    track: "SpotifyObjectTrack"

    def to_dict(self) -> Dict[str, Any]:
        added_at = self.added_at

        track = self.track.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "added_at": added_at,
                "track": track,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_track import SpotifyObjectTrack

        d = src_dict.copy()
        added_at = d.pop("added_at")

        track = SpotifyObjectTrack.from_dict(d.pop("track"))

        spotify_object_saved_track = cls(
            added_at=added_at,
            track=track,
        )

        return spotify_object_saved_track
