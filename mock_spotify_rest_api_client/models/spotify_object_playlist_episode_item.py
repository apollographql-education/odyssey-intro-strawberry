from typing import TYPE_CHECKING, Any, Dict, List, Literal, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_external_id import SpotifyObjectExternalId
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
    from ..models.spotify_object_playlist_episode_artist import (
        SpotifyObjectPlaylistEpisodeArtist,
    )
    from ..models.spotify_object_playlist_episode_show import (
        SpotifyObjectPlaylistEpisodeShow,
    )


T = TypeVar("T", bound="SpotifyObjectPlaylistEpisodeItem")


@_attrs_define
class SpotifyObjectPlaylistEpisodeItem:
    """
    Attributes:
        album (SpotifyObjectPlaylistEpisodeShow):
        artists (List['SpotifyObjectPlaylistEpisodeArtist']):
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
        is_playable (bool):
        name (str):
        popularity (float):
        preview_url (Union[None, str]):
        track (bool):
        track_number (float):
        type (Literal['episode']):
        uri (str):
    """

    album: "SpotifyObjectPlaylistEpisodeShow"
    artists: List["SpotifyObjectPlaylistEpisodeArtist"]
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
    is_playable: bool
    name: str
    popularity: float
    preview_url: Union[None, str]
    track: bool
    track_number: float
    type: Literal["episode"]
    uri: str

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

        is_playable = self.is_playable

        name = self.name

        popularity = self.popularity

        preview_url: Union[None, str]
        preview_url = self.preview_url

        track = self.track

        track_number = self.track_number

        type = self.type

        uri = self.uri

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
                "is_playable": is_playable,
                "name": name,
                "popularity": popularity,
                "preview_url": preview_url,
                "track": track,
                "track_number": track_number,
                "type": type,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_external_id import SpotifyObjectExternalId
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
        from ..models.spotify_object_playlist_episode_artist import (
            SpotifyObjectPlaylistEpisodeArtist,
        )
        from ..models.spotify_object_playlist_episode_show import (
            SpotifyObjectPlaylistEpisodeShow,
        )

        d = src_dict.copy()
        album = SpotifyObjectPlaylistEpisodeShow.from_dict(d.pop("album"))

        artists = []
        _artists = d.pop("artists")
        for artists_item_data in _artists:
            artists_item = SpotifyObjectPlaylistEpisodeArtist.from_dict(
                artists_item_data
            )

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

        is_playable = d.pop("is_playable")

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

        spotify_object_playlist_episode_item = cls(
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
            is_playable=is_playable,
            name=name,
            popularity=popularity,
            preview_url=preview_url,
            track=track,
            track_number=track_number,
            type=type,
            uri=uri,
        )

        return spotify_object_playlist_episode_item
