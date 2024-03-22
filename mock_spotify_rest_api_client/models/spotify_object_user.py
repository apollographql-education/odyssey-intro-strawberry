from typing import TYPE_CHECKING, Any, Dict, List, Literal, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
    from ..models.spotify_object_followers import SpotifyObjectFollowers
    from ..models.spotify_object_image import SpotifyObjectImage


T = TypeVar("T", bound="SpotifyObjectUser")


@_attrs_define
class SpotifyObjectUser:
    """
    Attributes:
        display_name (str):
        external_urls (SpotifyObjectExternalUrl):
        followers (SpotifyObjectFollowers):
        href (str):
        id (str):
        type (Literal['user']):
        uri (str):
        images (Union[Unset, List['SpotifyObjectImage']]):
    """

    display_name: str
    external_urls: "SpotifyObjectExternalUrl"
    followers: "SpotifyObjectFollowers"
    href: str
    id: str
    type: Literal["user"]
    uri: str
    images: Union[Unset, List["SpotifyObjectImage"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name

        external_urls = self.external_urls.to_dict()

        followers = self.followers.to_dict()

        href = self.href

        id = self.id

        type = self.type

        uri = self.uri

        images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "display_name": display_name,
                "external_urls": external_urls,
                "followers": followers,
                "href": href,
                "id": id,
                "type": type,
                "uri": uri,
            }
        )
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
        from ..models.spotify_object_followers import SpotifyObjectFollowers
        from ..models.spotify_object_image import SpotifyObjectImage

        d = src_dict.copy()
        display_name = d.pop("display_name")

        external_urls = SpotifyObjectExternalUrl.from_dict(d.pop("external_urls"))

        followers = SpotifyObjectFollowers.from_dict(d.pop("followers"))

        href = d.pop("href")

        id = d.pop("id")

        type = d.pop("type")

        uri = d.pop("uri")

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = SpotifyObjectImage.from_dict(images_item_data)

            images.append(images_item)

        spotify_object_user = cls(
            display_name=display_name,
            external_urls=external_urls,
            followers=followers,
            href=href,
            id=id,
            type=type,
            uri=uri,
            images=images,
        )

        return spotify_object_user
