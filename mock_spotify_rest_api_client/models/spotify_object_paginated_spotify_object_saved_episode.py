from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_saved_episode import SpotifyObjectSavedEpisode


T = TypeVar("T", bound="SpotifyObjectPaginatedSpotifyObjectSavedEpisode")


@_attrs_define
class SpotifyObjectPaginatedSpotifyObjectSavedEpisode:
    """
    Attributes:
        items (List['SpotifyObjectSavedEpisode']):
        href (str):
        limit (float):
        next_ (Union[None, str]):
        offset (float):
        previous (Union[None, str]):
        total (float):
    """

    items: List["SpotifyObjectSavedEpisode"]
    href: str
    limit: float
    next_: Union[None, str]
    offset: float
    previous: Union[None, str]
    total: float

    def to_dict(self) -> Dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        href = self.href

        limit = self.limit

        next_: Union[None, str]
        next_ = self.next_

        offset = self.offset

        previous: Union[None, str]
        previous = self.previous

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "items": items,
                "href": href,
                "limit": limit,
                "next": next_,
                "offset": offset,
                "previous": previous,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_saved_episode import SpotifyObjectSavedEpisode

        d = src_dict.copy()
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = SpotifyObjectSavedEpisode.from_dict(items_item_data)

            items.append(items_item)

        href = d.pop("href")

        limit = d.pop("limit")

        def _parse_next_(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        next_ = _parse_next_(d.pop("next"))

        offset = d.pop("offset")

        def _parse_previous(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        previous = _parse_previous(d.pop("previous"))

        total = d.pop("total")

        spotify_object_paginated_spotify_object_saved_episode = cls(
            items=items,
            href=href,
            limit=limit,
            next_=next_,
            offset=offset,
            previous=previous,
            total=total,
        )

        return spotify_object_paginated_spotify_object_saved_episode
