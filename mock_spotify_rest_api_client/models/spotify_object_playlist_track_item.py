from typing import TYPE_CHECKING, Any, Dict, List, Literal, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spotify_object_album_simplified import SpotifyObjectAlbumSimplified
    from ..models.spotify_object_artist_simplified import SpotifyObjectArtistSimplified
    from ..models.spotify_object_external_id import SpotifyObjectExternalId
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
    from ..models.spotify_object_restrictions import SpotifyObjectRestrictions
    from ..models.spotify_object_track import SpotifyObjectTrack


T = TypeVar("T", bound="SpotifyObjectPlaylistTrackItem")


@_attrs_define
class SpotifyObjectPlaylistTrackItem:
    """
    Attributes:
        album (SpotifyObjectAlbumSimplified):
        artists (List['SpotifyObjectArtistSimplified']):
        available_markets (List[str]):
        disc_number (float):
        duration_ms (float):
        episode (bool):
        explicit (bool):
        external_ids (SpotifyObjectExternalId):
        external_urls (SpotifyObjectExternalUrl):
        href (str):
        id (str):
        is_local (bool):
        name (str):
        popularity (float):
        preview_url (Union[None, str]):
        track (bool):
        track_number (float):
        type (Literal['track']):
        uri (str):
        is_playable (Union[Unset, bool]):
        linked_from (Union[Unset, SpotifyObjectTrack]):
        restrictions (Union[Unset, SpotifyObjectRestrictions]):
    """

    album: "SpotifyObjectAlbumSimplified"
    artists: List["SpotifyObjectArtistSimplified"]
    available_markets: List[str]
    disc_number: float
    duration_ms: float
    episode: bool
    explicit: bool
    external_ids: "SpotifyObjectExternalId"
    external_urls: "SpotifyObjectExternalUrl"
    href: str
    id: str
    is_local: bool
    name: str
    popularity: float
    preview_url: Union[None, str]
    track: bool
    track_number: float
    type: Literal["track"]
    uri: str
    is_playable: Union[Unset, bool] = UNSET
    linked_from: Union[Unset, "SpotifyObjectTrack"] = UNSET
    restrictions: Union[Unset, "SpotifyObjectRestrictions"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        album = self.album.to_dict()

        artists = []
        for artists_item_data in self.artists:
            artists_item = artists_item_data.to_dict()
            artists.append(artists_item)

        available_markets = self.available_markets

        disc_number = self.disc_number

        duration_ms = self.duration_ms

        episode = self.episode

        explicit = self.explicit

        external_ids = self.external_ids.to_dict()

        external_urls = self.external_urls.to_dict()

        href = self.href

        id = self.id

        is_local = self.is_local

        name = self.name

        popularity = self.popularity

        preview_url: Union[None, str]
        preview_url = self.preview_url

        track = self.track

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
                "album": album,
                "artists": artists,
                "available_markets": available_markets,
                "disc_number": disc_number,
                "duration_ms": duration_ms,
                "episode": episode,
                "explicit": explicit,
                "external_ids": external_ids,
                "external_urls": external_urls,
                "href": href,
                "id": id,
                "is_local": is_local,
                "name": name,
                "popularity": popularity,
                "preview_url": preview_url,
                "track": track,
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
        from ..models.spotify_object_album_simplified import (
            SpotifyObjectAlbumSimplified,
        )
        from ..models.spotify_object_artist_simplified import (
            SpotifyObjectArtistSimplified,
        )
        from ..models.spotify_object_external_id import SpotifyObjectExternalId
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
        from ..models.spotify_object_restrictions import SpotifyObjectRestrictions
        from ..models.spotify_object_track import SpotifyObjectTrack

        d = src_dict.copy()
        album = SpotifyObjectAlbumSimplified.from_dict(d.pop("album"))

        artists = []
        _artists = d.pop("artists")
        for artists_item_data in _artists:
            artists_item = SpotifyObjectArtistSimplified.from_dict(artists_item_data)

            artists.append(artists_item)

        available_markets = cast(List[str], d.pop("available_markets"))

        disc_number = d.pop("disc_number")

        duration_ms = d.pop("duration_ms")

        episode = d.pop("episode")

        explicit = d.pop("explicit")

        external_ids = SpotifyObjectExternalId.from_dict(d.pop("external_ids"))

        external_urls = SpotifyObjectExternalUrl.from_dict(d.pop("external_urls"))

        href = d.pop("href")

        id = d.pop("id")

        is_local = d.pop("is_local")

        name = d.pop("name")

        popularity = d.pop("popularity")

        def _parse_preview_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        preview_url = _parse_preview_url(d.pop("preview_url"))

        track = d.pop("track")

        track_number = d.pop("track_number")

        type = d.pop("type")

        uri = d.pop("uri")

        is_playable = d.pop("is_playable", UNSET)

        _linked_from = d.pop("linked_from", UNSET)
        linked_from: Union[Unset, SpotifyObjectTrack]
        if isinstance(_linked_from, Unset):
            linked_from = UNSET
        else:
            linked_from = SpotifyObjectTrack.from_dict(_linked_from)

        _restrictions = d.pop("restrictions", UNSET)
        restrictions: Union[Unset, SpotifyObjectRestrictions]
        if isinstance(_restrictions, Unset):
            restrictions = UNSET
        else:
            restrictions = SpotifyObjectRestrictions.from_dict(_restrictions)

        spotify_object_playlist_track_item = cls(
            album=album,
            artists=artists,
            available_markets=available_markets,
            disc_number=disc_number,
            duration_ms=duration_ms,
            episode=episode,
            explicit=explicit,
            external_ids=external_ids,
            external_urls=external_urls,
            href=href,
            id=id,
            is_local=is_local,
            name=name,
            popularity=popularity,
            preview_url=preview_url,
            track=track,
            track_number=track_number,
            type=type,
            uri=uri,
            is_playable=is_playable,
            linked_from=linked_from,
            restrictions=restrictions,
        )

        return spotify_object_playlist_track_item
