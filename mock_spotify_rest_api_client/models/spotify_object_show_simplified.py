from typing import TYPE_CHECKING, Any, Dict, List, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_copyright import SpotifyObjectCopyright
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
    from ..models.spotify_object_image import SpotifyObjectImage


T = TypeVar("T", bound="SpotifyObjectShowSimplified")


@_attrs_define
class SpotifyObjectShowSimplified:
    """
    Attributes:
        available_markets (List[str]):
        copyrights (List['SpotifyObjectCopyright']):
        description (str):
        explicit (bool):
        external_urls (SpotifyObjectExternalUrl):
        href (str):
        html_description (str):
        id (str):
        images (List['SpotifyObjectImage']):
        is_externally_hosted (bool):
        languages (List[str]):
        media_type (str):
        name (str):
        publisher (str):
        total_episodes (float):
        type (Literal['show']):
        uri (str):
    """

    available_markets: List[str]
    copyrights: List["SpotifyObjectCopyright"]
    description: str
    explicit: bool
    external_urls: "SpotifyObjectExternalUrl"
    href: str
    html_description: str
    id: str
    images: List["SpotifyObjectImage"]
    is_externally_hosted: bool
    languages: List[str]
    media_type: str
    name: str
    publisher: str
    total_episodes: float
    type: Literal["show"]
    uri: str

    def to_dict(self) -> Dict[str, Any]:
        available_markets = self.available_markets

        copyrights = []
        for copyrights_item_data in self.copyrights:
            copyrights_item = copyrights_item_data.to_dict()
            copyrights.append(copyrights_item)

        description = self.description

        explicit = self.explicit

        external_urls = self.external_urls.to_dict()

        href = self.href

        html_description = self.html_description

        id = self.id

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        is_externally_hosted = self.is_externally_hosted

        languages = self.languages

        media_type = self.media_type

        name = self.name

        publisher = self.publisher

        total_episodes = self.total_episodes

        type = self.type

        uri = self.uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "available_markets": available_markets,
                "copyrights": copyrights,
                "description": description,
                "explicit": explicit,
                "external_urls": external_urls,
                "href": href,
                "html_description": html_description,
                "id": id,
                "images": images,
                "is_externally_hosted": is_externally_hosted,
                "languages": languages,
                "media_type": media_type,
                "name": name,
                "publisher": publisher,
                "total_episodes": total_episodes,
                "type": type,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_copyright import SpotifyObjectCopyright
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
        from ..models.spotify_object_image import SpotifyObjectImage

        d = src_dict.copy()
        available_markets = cast(List[str], d.pop("available_markets"))

        copyrights = []
        _copyrights = d.pop("copyrights")
        for copyrights_item_data in _copyrights:
            copyrights_item = SpotifyObjectCopyright.from_dict(copyrights_item_data)

            copyrights.append(copyrights_item)

        description = d.pop("description")

        explicit = d.pop("explicit")

        external_urls = SpotifyObjectExternalUrl.from_dict(d.pop("external_urls"))

        href = d.pop("href")

        html_description = d.pop("html_description")

        id = d.pop("id")

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = SpotifyObjectImage.from_dict(images_item_data)

            images.append(images_item)

        is_externally_hosted = d.pop("is_externally_hosted")

        languages = cast(List[str], d.pop("languages"))

        media_type = d.pop("media_type")

        name = d.pop("name")

        publisher = d.pop("publisher")

        total_episodes = d.pop("total_episodes")

        type = d.pop("type")

        uri = d.pop("uri")

        spotify_object_show_simplified = cls(
            available_markets=available_markets,
            copyrights=copyrights,
            description=description,
            explicit=explicit,
            external_urls=external_urls,
            href=href,
            html_description=html_description,
            id=id,
            images=images,
            is_externally_hosted=is_externally_hosted,
            languages=languages,
            media_type=media_type,
            name=name,
            publisher=publisher,
            total_episodes=total_episodes,
            type=type,
            uri=uri,
        )

        return spotify_object_show_simplified
