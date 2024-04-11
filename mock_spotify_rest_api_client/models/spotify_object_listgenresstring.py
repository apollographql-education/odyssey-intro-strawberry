from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyObjectListgenresstring")


@_attrs_define
class SpotifyObjectListgenresstring:
    """
    Attributes:
        genres (List[str]):
    """

    genres: List[str]

    def to_dict(self) -> Dict[str, Any]:
        genres = self.genres

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "genres": genres,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        genres = cast(List[str], d.pop("genres"))

        spotify_object_listgenresstring = cls(
            genres=genres,
        )

        return spotify_object_listgenresstring
