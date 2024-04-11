from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.spotify_object_context_type import SpotifyObjectContextType

if TYPE_CHECKING:
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl


T = TypeVar("T", bound="SpotifyObjectContext")


@_attrs_define
class SpotifyObjectContext:
    """
    Attributes:
        type (SpotifyObjectContextType):
        href (str):
        external_urls (SpotifyObjectExternalUrl):
        uri (str):
    """

    type: SpotifyObjectContextType
    href: str
    external_urls: "SpotifyObjectExternalUrl"
    uri: str

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        href = self.href

        external_urls = self.external_urls.to_dict()

        uri = self.uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "href": href,
                "external_urls": external_urls,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl

        d = src_dict.copy()
        type = SpotifyObjectContextType(d.pop("type"))

        href = d.pop("href")

        external_urls = SpotifyObjectExternalUrl.from_dict(d.pop("external_urls"))

        uri = d.pop("uri")

        spotify_object_context = cls(
            type=type,
            href=href,
            external_urls=external_urls,
            uri=uri,
        )

        return spotify_object_context
