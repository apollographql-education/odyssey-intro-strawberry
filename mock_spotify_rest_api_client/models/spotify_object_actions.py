from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_disallows import SpotifyObjectDisallows


T = TypeVar("T", bound="SpotifyObjectActions")


@_attrs_define
class SpotifyObjectActions:
    """
    Attributes:
        disallows (SpotifyObjectDisallows):
    """

    disallows: "SpotifyObjectDisallows"

    def to_dict(self) -> Dict[str, Any]:
        disallows = self.disallows.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "disallows": disallows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_disallows import SpotifyObjectDisallows

        d = src_dict.copy()
        disallows = SpotifyObjectDisallows.from_dict(d.pop("disallows"))

        spotify_object_actions = cls(
            disallows=disallows,
        )

        return spotify_object_actions
