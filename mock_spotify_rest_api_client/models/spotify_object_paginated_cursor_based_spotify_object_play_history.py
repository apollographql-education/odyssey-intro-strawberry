from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_cursors import SpotifyObjectCursors
    from ..models.spotify_object_play_history import SpotifyObjectPlayHistory


T = TypeVar("T", bound="SpotifyObjectPaginatedCursorBasedSpotifyObjectPlayHistory")


@_attrs_define
class SpotifyObjectPaginatedCursorBasedSpotifyObjectPlayHistory:
    """
    Attributes:
        href (str):
        items (List['SpotifyObjectPlayHistory']):
        limit (float):
        next_ (Union[None, str]):
        cursors (SpotifyObjectCursors):
        total (float):
    """

    href: str
    items: List["SpotifyObjectPlayHistory"]
    limit: float
    next_: Union[None, str]
    cursors: "SpotifyObjectCursors"
    total: float

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        limit = self.limit

        next_: Union[None, str]
        next_ = self.next_

        cursors = self.cursors.to_dict()

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "href": href,
                "items": items,
                "limit": limit,
                "next": next_,
                "cursors": cursors,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_cursors import SpotifyObjectCursors
        from ..models.spotify_object_play_history import SpotifyObjectPlayHistory

        d = src_dict.copy()
        href = d.pop("href")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = SpotifyObjectPlayHistory.from_dict(items_item_data)

            items.append(items_item)

        limit = d.pop("limit")

        def _parse_next_(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        next_ = _parse_next_(d.pop("next"))

        cursors = SpotifyObjectCursors.from_dict(d.pop("cursors"))

        total = d.pop("total")

        spotify_object_paginated_cursor_based_spotify_object_play_history = cls(
            href=href,
            items=items,
            limit=limit,
            next_=next_,
            cursors=cursors,
            total=total,
        )

        return spotify_object_paginated_cursor_based_spotify_object_play_history
