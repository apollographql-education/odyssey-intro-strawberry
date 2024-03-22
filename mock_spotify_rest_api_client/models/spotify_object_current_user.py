from typing import TYPE_CHECKING, Any, Dict, List, Literal, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_explicit_content_settings import (
        SpotifyObjectExplicitContentSettings,
    )
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
    from ..models.spotify_object_followers import SpotifyObjectFollowers
    from ..models.spotify_object_image import SpotifyObjectImage


T = TypeVar("T", bound="SpotifyObjectCurrentUser")


@_attrs_define
class SpotifyObjectCurrentUser:
    """
    Attributes:
        country (str):
        display_name (str):
        email (str):
        explicit_content (SpotifyObjectExplicitContentSettings):
        external_urls (SpotifyObjectExternalUrl):
        followers (SpotifyObjectFollowers):
        href (str):
        id (str):
        images (List['SpotifyObjectImage']):
        product (str):
        type (Literal['user']):
        uri (str):
    """

    country: str
    display_name: str
    email: str
    explicit_content: "SpotifyObjectExplicitContentSettings"
    external_urls: "SpotifyObjectExternalUrl"
    followers: "SpotifyObjectFollowers"
    href: str
    id: str
    images: List["SpotifyObjectImage"]
    product: str
    type: Literal["user"]
    uri: str

    def to_dict(self) -> Dict[str, Any]:
        country = self.country

        display_name = self.display_name

        email = self.email

        explicit_content = self.explicit_content.to_dict()

        external_urls = self.external_urls.to_dict()

        followers = self.followers.to_dict()

        href = self.href

        id = self.id

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        product = self.product

        type = self.type

        uri = self.uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "country": country,
                "display_name": display_name,
                "email": email,
                "explicit_content": explicit_content,
                "external_urls": external_urls,
                "followers": followers,
                "href": href,
                "id": id,
                "images": images,
                "product": product,
                "type": type,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_explicit_content_settings import (
            SpotifyObjectExplicitContentSettings,
        )
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
        from ..models.spotify_object_followers import SpotifyObjectFollowers
        from ..models.spotify_object_image import SpotifyObjectImage

        d = src_dict.copy()
        country = d.pop("country")

        display_name = d.pop("display_name")

        email = d.pop("email")

        explicit_content = SpotifyObjectExplicitContentSettings.from_dict(
            d.pop("explicit_content")
        )

        external_urls = SpotifyObjectExternalUrl.from_dict(d.pop("external_urls"))

        followers = SpotifyObjectFollowers.from_dict(d.pop("followers"))

        href = d.pop("href")

        id = d.pop("id")

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = SpotifyObjectImage.from_dict(images_item_data)

            images.append(images_item)

        product = d.pop("product")

        type = d.pop("type")

        uri = d.pop("uri")

        spotify_object_current_user = cls(
            country=country,
            display_name=display_name,
            email=email,
            explicit_content=explicit_content,
            external_urls=external_urls,
            followers=followers,
            href=href,
            id=id,
            images=images,
            product=product,
            type=type,
            uri=uri,
        )

        return spotify_object_current_user
