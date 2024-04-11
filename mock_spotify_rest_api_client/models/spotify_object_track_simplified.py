from typing import TYPE_CHECKING, Any, Dict, List, Literal, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spotify_object_artist_simplified import SpotifyObjectArtistSimplified
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
    from ..models.spotify_object_restrictions import SpotifyObjectRestrictions
    from ..models.spotify_object_track_simplified_linked_from import (
        SpotifyObjectTrackSimplifiedLinkedFrom,
    )


T = TypeVar("T", bound="SpotifyObjectTrackSimplified")


@_attrs_define
class SpotifyObjectTrackSimplified:
    """
    Attributes:
        artists (List['SpotifyObjectArtistSimplified']):
        available_markets (List[str]):
        disc_number (float):
        duration_ms (float):
        explicit (bool):
        external_urls (SpotifyObjectExternalUrl):
        href (str):
        id (str):
        is_local (bool):
        name (str):
        preview_url (Union[None, str]):
        track_number (float):
        type (Literal['track']):
        uri (str):
        is_playable (Union[Unset, bool]):
        linked_from (Union[Unset, SpotifyObjectTrackSimplifiedLinkedFrom]):
        restrictions (Union[Unset, SpotifyObjectRestrictions]):
    """

    artists: List["SpotifyObjectArtistSimplified"]
    available_markets: List[str]
    disc_number: float
    duration_ms: float
    explicit: bool
    external_urls: "SpotifyObjectExternalUrl"
    href: str
    id: str
    is_local: bool
    name: str
    preview_url: Union[None, str]
    track_number: float
    type: Literal["track"]
    uri: str
    is_playable: Union[Unset, bool] = UNSET
    linked_from: Union[Unset, "SpotifyObjectTrackSimplifiedLinkedFrom"] = UNSET
    restrictions: Union[Unset, "SpotifyObjectRestrictions"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        artists = []
        for artists_item_data in self.artists:
            artists_item = artists_item_data.to_dict()
            artists.append(artists_item)

        available_markets = self.available_markets

        disc_number = self.disc_number

        duration_ms = self.duration_ms

        explicit = self.explicit

        external_urls = self.external_urls.to_dict()

        href = self.href

        id = self.id

        is_local = self.is_local

        name = self.name

        preview_url: Union[None, str]
        preview_url = self.preview_url

        track_number = self.track_number

        type = self.type

        uri = self.uri

        is_playable = self.is_playable

        linked_from: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.linked_from, Unset):
            linked_from = self.linked_from.to_dict()

        restrictions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = self.restrictions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "artists": artists,
                "available_markets": available_markets,
                "disc_number": disc_number,
                "duration_ms": duration_ms,
                "explicit": explicit,
                "external_urls": external_urls,
                "href": href,
                "id": id,
                "is_local": is_local,
                "name": name,
                "preview_url": preview_url,
                "track_number": track_number,
                "type": type,
                "uri": uri,
            }
        )
        if is_playable is not UNSET:
            field_dict["is_playable"] = is_playable
        if linked_from is not UNSET:
            field_dict["linked_from"] = linked_from
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_artist_simplified import (
            SpotifyObjectArtistSimplified,
        )
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
        from ..models.spotify_object_restrictions import SpotifyObjectRestrictions
        from ..models.spotify_object_track_simplified_linked_from import (
            SpotifyObjectTrackSimplifiedLinkedFrom,
        )

        d = src_dict.copy()
        artists = []
        _artists = d.pop("artists")
        for artists_item_data in _artists:
            artists_item = SpotifyObjectArtistSimplified.from_dict(artists_item_data)

            artists.append(artists_item)

        available_markets = cast(List[str], d.pop("available_markets"))

        disc_number = d.pop("disc_number")

        duration_ms = d.pop("duration_ms")

        explicit = d.pop("explicit")

        external_urls = SpotifyObjectExternalUrl.from_dict(d.pop("external_urls"))

        href = d.pop("href")

        id = d.pop("id")

        is_local = d.pop("is_local")

        name = d.pop("name")

        def _parse_preview_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        preview_url = _parse_preview_url(d.pop("preview_url"))

        track_number = d.pop("track_number")

        type = d.pop("type")

        uri = d.pop("uri")

        is_playable = d.pop("is_playable", UNSET)

        _linked_from = d.pop("linked_from", UNSET)
        linked_from: Union[Unset, SpotifyObjectTrackSimplifiedLinkedFrom]
        if isinstance(_linked_from, Unset):
            linked_from = UNSET
        else:
            linked_from = SpotifyObjectTrackSimplifiedLinkedFrom.from_dict(_linked_from)

        _restrictions = d.pop("restrictions", UNSET)
        restrictions: Union[Unset, SpotifyObjectRestrictions]
        if isinstance(_restrictions, Unset):
            restrictions = UNSET
        else:
            restrictions = SpotifyObjectRestrictions.from_dict(_restrictions)

        spotify_object_track_simplified = cls(
            artists=artists,
            available_markets=available_markets,
            disc_number=disc_number,
            duration_ms=duration_ms,
            explicit=explicit,
            external_urls=external_urls,
            href=href,
            id=id,
            is_local=is_local,
            name=name,
            preview_url=preview_url,
            track_number=track_number,
            type=type,
            uri=uri,
            is_playable=is_playable,
            linked_from=linked_from,
            restrictions=restrictions,
        )

        return spotify_object_track_simplified
