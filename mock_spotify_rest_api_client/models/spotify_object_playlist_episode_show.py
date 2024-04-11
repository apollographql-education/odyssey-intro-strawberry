from typing import TYPE_CHECKING, Any, Dict, List, Literal, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.spotify_object_album_type import SpotifyObjectAlbumType
from ..models.spotify_object_release_date_precision import (
    SpotifyObjectReleaseDatePrecision,
)

if TYPE_CHECKING:
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
    from ..models.spotify_object_image import SpotifyObjectImage
    from ..models.spotify_object_playlist_episode_artist import (
        SpotifyObjectPlaylistEpisodeArtist,
    )
    from ..models.spotify_object_restrictions import SpotifyObjectRestrictions


T = TypeVar("T", bound="SpotifyObjectPlaylistEpisodeShow")


@_attrs_define
class SpotifyObjectPlaylistEpisodeShow:
    """
    Attributes:
        album_type (SpotifyObjectAlbumType):
        artists (List['SpotifyObjectPlaylistEpisodeArtist']):
        available_markets (List[str]):
        external_urls (SpotifyObjectExternalUrl):
        href (str):
        id (str):
        images (List['SpotifyObjectImage']):
        is_playable (bool):
        name (str):
        release_date (str):
        release_date_precision (Union[None, SpotifyObjectReleaseDatePrecision]):
        restrictions (SpotifyObjectRestrictions):
        total_tracks (float):
        type (Literal['show']):
        uri (str):
    """

    album_type: SpotifyObjectAlbumType
    artists: List["SpotifyObjectPlaylistEpisodeArtist"]
    available_markets: List[str]
    external_urls: "SpotifyObjectExternalUrl"
    href: str
    id: str
    images: List["SpotifyObjectImage"]
    is_playable: bool
    name: str
    release_date: str
    release_date_precision: Union[None, SpotifyObjectReleaseDatePrecision]
    restrictions: "SpotifyObjectRestrictions"
    total_tracks: float
    type: Literal["show"]
    uri: str

    def to_dict(self) -> Dict[str, Any]:
        album_type = self.album_type.value

        artists = []
        for artists_item_data in self.artists:
            artists_item = artists_item_data.to_dict()
            artists.append(artists_item)

        available_markets = self.available_markets

        external_urls = self.external_urls.to_dict()

        href = self.href

        id = self.id

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        is_playable = self.is_playable

        name = self.name

        release_date = self.release_date

        release_date_precision: Union[None, str]
        if isinstance(self.release_date_precision, SpotifyObjectReleaseDatePrecision):
            release_date_precision = self.release_date_precision.value
        else:
            release_date_precision = self.release_date_precision

        restrictions = self.restrictions.to_dict()

        total_tracks = self.total_tracks

        type = self.type

        uri = self.uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "album_type": album_type,
                "artists": artists,
                "available_markets": available_markets,
                "external_urls": external_urls,
                "href": href,
                "id": id,
                "images": images,
                "is_playable": is_playable,
                "name": name,
                "release_date": release_date,
                "release_date_precision": release_date_precision,
                "restrictions": restrictions,
                "total_tracks": total_tracks,
                "type": type,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
        from ..models.spotify_object_image import SpotifyObjectImage
        from ..models.spotify_object_playlist_episode_artist import (
            SpotifyObjectPlaylistEpisodeArtist,
        )
        from ..models.spotify_object_restrictions import SpotifyObjectRestrictions

        d = src_dict.copy()
        album_type = SpotifyObjectAlbumType(d.pop("album_type"))

        artists = []
        _artists = d.pop("artists")
        for artists_item_data in _artists:
            artists_item = SpotifyObjectPlaylistEpisodeArtist.from_dict(
                artists_item_data
            )

            artists.append(artists_item)

        available_markets = cast(List[str], d.pop("available_markets"))

        external_urls = SpotifyObjectExternalUrl.from_dict(d.pop("external_urls"))

        href = d.pop("href")

        id = d.pop("id")

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = SpotifyObjectImage.from_dict(images_item_data)

            images.append(images_item)

        is_playable = d.pop("is_playable")

        name = d.pop("name")

        release_date = d.pop("release_date")

        def _parse_release_date_precision(
            data: object,
        ) -> Union[None, SpotifyObjectReleaseDatePrecision]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                release_date_precision_type_0 = SpotifyObjectReleaseDatePrecision(data)

                return release_date_precision_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, SpotifyObjectReleaseDatePrecision], data)

        release_date_precision = _parse_release_date_precision(
            d.pop("release_date_precision")
        )

        restrictions = SpotifyObjectRestrictions.from_dict(d.pop("restrictions"))

        total_tracks = d.pop("total_tracks")

        type = d.pop("type")

        uri = d.pop("uri")

        spotify_object_playlist_episode_show = cls(
            album_type=album_type,
            artists=artists,
            available_markets=available_markets,
            external_urls=external_urls,
            href=href,
            id=id,
            images=images,
            is_playable=is_playable,
            name=name,
            release_date=release_date,
            release_date_precision=release_date_precision,
            restrictions=restrictions,
            total_tracks=total_tracks,
            type=type,
            uri=uri,
        )

        return spotify_object_playlist_episode_show
