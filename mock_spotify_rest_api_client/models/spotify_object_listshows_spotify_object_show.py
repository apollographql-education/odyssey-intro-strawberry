from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_show import SpotifyObjectShow


T = TypeVar("T", bound="SpotifyObjectListshowsSpotifyObjectShow")


@_attrs_define
class SpotifyObjectListshowsSpotifyObjectShow:
    """
    Attributes:
        shows (List['SpotifyObjectShow']):
    """

    shows: List["SpotifyObjectShow"]

    def to_dict(self) -> Dict[str, Any]:
        shows = []
        for shows_item_data in self.shows:
            shows_item = shows_item_data.to_dict()
            shows.append(shows_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "shows": shows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_show import SpotifyObjectShow

        d = src_dict.copy()
        shows = []
        _shows = d.pop("shows")
        for shows_item_data in _shows:
            shows_item = SpotifyObjectShow.from_dict(shows_item_data)

            shows.append(shows_item)

        spotify_object_listshows_spotify_object_show = cls(
            shows=shows,
        )

        return spotify_object_listshows_spotify_object_show
