from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_playlist_episode_item import (
        SpotifyObjectPlaylistEpisodeItem,
    )
    from ..models.spotify_object_playlist_track_item import (
        SpotifyObjectPlaylistTrackItem,
    )
    from ..models.spotify_object_playlist_track_video_thumbnail import (
        SpotifyObjectPlaylistTrackVideoThumbnail,
    )
    from ..models.spotify_object_user_simplified import SpotifyObjectUserSimplified


T = TypeVar("T", bound="SpotifyObjectPlaylistTrack")


@_attrs_define
class SpotifyObjectPlaylistTrack:
    """
    Attributes:
        added_at (str):
        added_by (SpotifyObjectUserSimplified):
        is_local (bool):
        track (Union['SpotifyObjectPlaylistEpisodeItem', 'SpotifyObjectPlaylistTrackItem']):
        video_thumbnail (SpotifyObjectPlaylistTrackVideoThumbnail):
    """

    added_at: str
    added_by: "SpotifyObjectUserSimplified"
    is_local: bool
    track: Union["SpotifyObjectPlaylistEpisodeItem", "SpotifyObjectPlaylistTrackItem"]
    video_thumbnail: "SpotifyObjectPlaylistTrackVideoThumbnail"

    def to_dict(self) -> Dict[str, Any]:
        from ..models.spotify_object_playlist_track_item import (
            SpotifyObjectPlaylistTrackItem,
        )

        added_at = self.added_at

        added_by = self.added_by.to_dict()

        is_local = self.is_local

        track: Dict[str, Any]
        if isinstance(self.track, SpotifyObjectPlaylistTrackItem):
            track = self.track.to_dict()
        else:
            track = self.track.to_dict()

        video_thumbnail = self.video_thumbnail.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "added_at": added_at,
                "added_by": added_by,
                "is_local": is_local,
                "track": track,
                "video_thumbnail": video_thumbnail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_playlist_episode_item import (
            SpotifyObjectPlaylistEpisodeItem,
        )
        from ..models.spotify_object_playlist_track_item import (
            SpotifyObjectPlaylistTrackItem,
        )
        from ..models.spotify_object_playlist_track_video_thumbnail import (
            SpotifyObjectPlaylistTrackVideoThumbnail,
        )
        from ..models.spotify_object_user_simplified import SpotifyObjectUserSimplified

        d = src_dict.copy()
        added_at = d.pop("added_at")

        added_by = SpotifyObjectUserSimplified.from_dict(d.pop("added_by"))

        is_local = d.pop("is_local")

        def _parse_track(
            data: object,
        ) -> Union[
            "SpotifyObjectPlaylistEpisodeItem", "SpotifyObjectPlaylistTrackItem"
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                track_type_0 = SpotifyObjectPlaylistTrackItem.from_dict(data)

                return track_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            track_type_1 = SpotifyObjectPlaylistEpisodeItem.from_dict(data)

            return track_type_1

        track = _parse_track(d.pop("track"))

        video_thumbnail = SpotifyObjectPlaylistTrackVideoThumbnail.from_dict(
            d.pop("video_thumbnail")
        )

        spotify_object_playlist_track = cls(
            added_at=added_at,
            added_by=added_by,
            is_local=is_local,
            track=track,
            video_thumbnail=video_thumbnail,
        )

        return spotify_object_playlist_track
