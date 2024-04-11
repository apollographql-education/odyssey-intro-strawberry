from typing import TYPE_CHECKING, Any, Dict, Literal, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl


T = TypeVar("T", bound="SpotifyObjectUserSimplified")


@_attrs_define
class SpotifyObjectUserSimplified:
    """
    Attributes:
        external_urls (SpotifyObjectExternalUrl):
        href (str):
        id (str):
        type (Literal['user']):
        uri (str):
        display_name (Union[Unset, str]):
    """

    external_urls: "SpotifyObjectExternalUrl"
    href: str
    id: str
    type: Literal["user"]
    uri: str
    display_name: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        external_urls = self.external_urls.to_dict()

        href = self.href

        id = self.id

        type = self.type

        uri = self.uri

        display_name = self.display_name

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
        if display_name is not UNSET:
            field_dict["display_name"] = display_name

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

        display_name = d.pop("display_name", UNSET)

        spotify_object_user_simplified = cls(
            external_urls=external_urls,
            href=href,
            id=id,
            type=type,
            uri=uri,
            display_name=display_name,
        )

        return spotify_object_user_simplified
