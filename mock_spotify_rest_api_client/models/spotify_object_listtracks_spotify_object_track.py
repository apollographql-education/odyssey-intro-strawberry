from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_track import SpotifyObjectTrack


T = TypeVar("T", bound="SpotifyObjectListtracksSpotifyObjectTrack")


@_attrs_define
class SpotifyObjectListtracksSpotifyObjectTrack:
    """
    Attributes:
        tracks (List['SpotifyObjectTrack']):
    """

    tracks: List["SpotifyObjectTrack"]

    def to_dict(self) -> Dict[str, Any]:
        tracks = []
        for tracks_item_data in self.tracks:
            tracks_item = tracks_item_data.to_dict()
            tracks.append(tracks_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "tracks": tracks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_track import SpotifyObjectTrack

        d = src_dict.copy()
        tracks = []
        _tracks = d.pop("tracks")
        for tracks_item_data in _tracks:
            tracks_item = SpotifyObjectTrack.from_dict(tracks_item_data)

            tracks.append(tracks_item)

        spotify_object_listtracks_spotify_object_track = cls(
            tracks=tracks,
        )

        return spotify_object_listtracks_spotify_object_track
