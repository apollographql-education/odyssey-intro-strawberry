from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_episode import SpotifyObjectEpisode


T = TypeVar("T", bound="SpotifyObjectSavedEpisode")


@_attrs_define
class SpotifyObjectSavedEpisode:
    """
    Attributes:
        added_at (str):
        episode (SpotifyObjectEpisode):
    """

    added_at: str
    episode: "SpotifyObjectEpisode"

    def to_dict(self) -> Dict[str, Any]:
        added_at = self.added_at

        episode = self.episode.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "added_at": added_at,
                "episode": episode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_episode import SpotifyObjectEpisode

        d = src_dict.copy()
        added_at = d.pop("added_at")

        episode = SpotifyObjectEpisode.from_dict(d.pop("episode"))

        spotify_object_saved_episode = cls(
            added_at=added_at,
            episode=episode,
        )

        return spotify_object_saved_episode
