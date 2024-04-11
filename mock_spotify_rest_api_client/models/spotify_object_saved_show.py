from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_show import SpotifyObjectShow


T = TypeVar("T", bound="SpotifyObjectSavedShow")


@_attrs_define
class SpotifyObjectSavedShow:
    """
    Attributes:
        added_at (str):
        show (SpotifyObjectShow):
    """

    added_at: str
    show: "SpotifyObjectShow"

    def to_dict(self) -> Dict[str, Any]:
        added_at = self.added_at

        show = self.show.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "added_at": added_at,
                "show": show,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_show import SpotifyObjectShow

        d = src_dict.copy()
        added_at = d.pop("added_at")

        show = SpotifyObjectShow.from_dict(d.pop("show"))

        spotify_object_saved_show = cls(
            added_at=added_at,
            show=show,
        )

        return spotify_object_saved_show
