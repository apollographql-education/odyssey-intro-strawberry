from typing import TYPE_CHECKING, Any, Dict, List, Literal, Type, TypeVar, cast

from attrs import define as _attrs_define

from ..models.spotify_object_release_date_precision import (
    SpotifyObjectReleaseDatePrecision,
)

if TYPE_CHECKING:
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
    from ..models.spotify_object_image import SpotifyObjectImage
    from ..models.spotify_object_resume_point import SpotifyObjectResumePoint
    from ..models.spotify_object_show_simplified import SpotifyObjectShowSimplified


T = TypeVar("T", bound="SpotifyObjectEpisode")


@_attrs_define
class SpotifyObjectEpisode:
    """
    Attributes:
        audio_preview_url (str):
        description (str):
        duration_ms (float):
        explicit (bool):
        external_urls (SpotifyObjectExternalUrl):
        href (str):
        html_description (str):
        id (str):
        images (List['SpotifyObjectImage']):
        is_externally_hosted (bool):
        is_playable (bool):
        language (str): The language used in the episode, identified by a  {@link  https://en.wikipedia.org/wiki/ISO_639
            ISO 639 }  code.
        languages (List[str]):
        name (str):
        release_date (str):
        release_date_precision (SpotifyObjectReleaseDatePrecision):
        resume_point (SpotifyObjectResumePoint):
        show (SpotifyObjectShowSimplified):
        type (Literal['episode']):
        uri (str):
    """

    audio_preview_url: str
    description: str
    duration_ms: float
    explicit: bool
    external_urls: "SpotifyObjectExternalUrl"
    href: str
    html_description: str
    id: str
    images: List["SpotifyObjectImage"]
    is_externally_hosted: bool
    is_playable: bool
    language: str
    languages: List[str]
    name: str
    release_date: str
    release_date_precision: SpotifyObjectReleaseDatePrecision
    resume_point: "SpotifyObjectResumePoint"
    show: "SpotifyObjectShowSimplified"
    type: Literal["episode"]
    uri: str

    def to_dict(self) -> Dict[str, Any]:
        audio_preview_url = self.audio_preview_url

        description = self.description

        duration_ms = self.duration_ms

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

        is_playable = self.is_playable

        language = self.language

        languages = self.languages

        name = self.name

        release_date = self.release_date

        release_date_precision = self.release_date_precision.value

        resume_point = self.resume_point.to_dict()

        show = self.show.to_dict()

        type = self.type

        uri = self.uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "audio_preview_url": audio_preview_url,
                "description": description,
                "duration_ms": duration_ms,
                "explicit": explicit,
                "external_urls": external_urls,
                "href": href,
                "html_description": html_description,
                "id": id,
                "images": images,
                "is_externally_hosted": is_externally_hosted,
                "is_playable": is_playable,
                "language": language,
                "languages": languages,
                "name": name,
                "release_date": release_date,
                "release_date_precision": release_date_precision,
                "resume_point": resume_point,
                "show": show,
                "type": type,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
        from ..models.spotify_object_image import SpotifyObjectImage
        from ..models.spotify_object_resume_point import SpotifyObjectResumePoint
        from ..models.spotify_object_show_simplified import SpotifyObjectShowSimplified

        d = src_dict.copy()
        audio_preview_url = d.pop("audio_preview_url")

        description = d.pop("description")

        duration_ms = d.pop("duration_ms")

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

        is_playable = d.pop("is_playable")

        language = d.pop("language")

        languages = cast(List[str], d.pop("languages"))

        name = d.pop("name")

        release_date = d.pop("release_date")

        release_date_precision = SpotifyObjectReleaseDatePrecision(
            d.pop("release_date_precision")
        )

        resume_point = SpotifyObjectResumePoint.from_dict(d.pop("resume_point"))

        show = SpotifyObjectShowSimplified.from_dict(d.pop("show"))

        type = d.pop("type")

        uri = d.pop("uri")

        spotify_object_episode = cls(
            audio_preview_url=audio_preview_url,
            description=description,
            duration_ms=duration_ms,
            explicit=explicit,
            external_urls=external_urls,
            href=href,
            html_description=html_description,
            id=id,
            images=images,
            is_externally_hosted=is_externally_hosted,
            is_playable=is_playable,
            language=language,
            languages=languages,
            name=name,
            release_date=release_date,
            release_date_precision=release_date_precision,
            resume_point=resume_point,
            show=show,
            type=type,
            uri=uri,
        )

        return spotify_object_episode
