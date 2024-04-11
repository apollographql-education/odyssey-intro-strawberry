from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_episode import SpotifyObjectEpisode


T = TypeVar("T", bound="SpotifyObjectListepisodesSpotifyObjectEpisode")


@_attrs_define
class SpotifyObjectListepisodesSpotifyObjectEpisode:
    """
    Attributes:
        episodes (List['SpotifyObjectEpisode']):
    """

    episodes: List["SpotifyObjectEpisode"]

    def to_dict(self) -> Dict[str, Any]:
        episodes = []
        for episodes_item_data in self.episodes:
            episodes_item = episodes_item_data.to_dict()
            episodes.append(episodes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "episodes": episodes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_episode import SpotifyObjectEpisode

        d = src_dict.copy()
        episodes = []
        _episodes = d.pop("episodes")
        for episodes_item_data in _episodes:
            episodes_item = SpotifyObjectEpisode.from_dict(episodes_item_data)

            episodes.append(episodes_item)

        spotify_object_listepisodes_spotify_object_episode = cls(
            episodes=episodes,
        )

        return spotify_object_listepisodes_spotify_object_episode
