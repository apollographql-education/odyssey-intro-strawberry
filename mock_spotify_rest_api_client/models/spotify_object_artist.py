from typing import TYPE_CHECKING, Any, Dict, List, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
    from ..models.spotify_object_followers import SpotifyObjectFollowers
    from ..models.spotify_object_image import SpotifyObjectImage


T = TypeVar("T", bound="SpotifyObjectArtist")


@_attrs_define
class SpotifyObjectArtist:
    """
    Attributes:
        external_urls (SpotifyObjectExternalUrl):
        followers (SpotifyObjectFollowers):
        genres (List[str]):
        href (str):
        id (str):
        images (List['SpotifyObjectImage']):
        name (str):
        popularity (float):
        type (Literal['artist']):
        uri (str):
    """

    external_urls: "SpotifyObjectExternalUrl"
    followers: "SpotifyObjectFollowers"
    genres: List[str]
    href: str
    id: str
    images: List["SpotifyObjectImage"]
    name: str
    popularity: float
    type: Literal["artist"]
    uri: str

    def to_dict(self) -> Dict[str, Any]:
        external_urls = self.external_urls.to_dict()

        followers = self.followers.to_dict()

        genres = self.genres

        href = self.href

        id = self.id

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        name = self.name

        popularity = self.popularity

        type = self.type

        uri = self.uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "external_urls": external_urls,
                "followers": followers,
                "genres": genres,
                "href": href,
                "id": id,
                "images": images,
                "name": name,
                "popularity": popularity,
                "type": type,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
        from ..models.spotify_object_followers import SpotifyObjectFollowers
        from ..models.spotify_object_image import SpotifyObjectImage

        d = src_dict.copy()
        external_urls = SpotifyObjectExternalUrl.from_dict(d.pop("external_urls"))

        followers = SpotifyObjectFollowers.from_dict(d.pop("followers"))

        genres = cast(List[str], d.pop("genres"))

        href = d.pop("href")

        id = d.pop("id")

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = SpotifyObjectImage.from_dict(images_item_data)

            images.append(images_item)

        name = d.pop("name")

        popularity = d.pop("popularity")

        type = d.pop("type")

        uri = d.pop("uri")

        spotify_object_artist = cls(
            external_urls=external_urls,
            followers=followers,
            genres=genres,
            href=href,
            id=id,
            images=images,
            name=name,
            popularity=popularity,
            type=type,
            uri=uri,
        )

        return spotify_object_artist
