from typing import TYPE_CHECKING, Any, Dict, Literal, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl


T = TypeVar("T", bound="SpotifyObjectTrackSimplifiedLinkedFrom")


@_attrs_define
class SpotifyObjectTrackSimplifiedLinkedFrom:
    """
    Attributes:
        external_urls (SpotifyObjectExternalUrl):
        href (str):
        id (str):
        type (Literal['track']):
        uri (str):
    """

    external_urls: "SpotifyObjectExternalUrl"
    href: str
    id: str
    type: Literal["track"]
    uri: str

    def to_dict(self) -> Dict[str, Any]:
        external_urls = self.external_urls.to_dict()

        href = self.href

        id = self.id

        type = self.type

        uri = self.uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "external_urls": external_urls,
                "href": href,
                "id": id,
                "type": type,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl

        d = src_dict.copy()
        external_urls = SpotifyObjectExternalUrl.from_dict(d.pop("external_urls"))

        href = d.pop("href")

        id = d.pop("id")

        type = d.pop("type")

        uri = d.pop("uri")

        spotify_object_track_simplified_linked_from = cls(
            external_urls=external_urls,
            href=href,
            id=id,
            type=type,
            uri=uri,
        )

        return spotify_object_track_simplified_linked_from
