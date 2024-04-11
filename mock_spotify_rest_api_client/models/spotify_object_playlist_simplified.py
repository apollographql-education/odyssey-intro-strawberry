from typing import TYPE_CHECKING, Any, Dict, List, Literal, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
    from ..models.spotify_object_image import SpotifyObjectImage
    from ..models.spotify_object_playlist_tracks_information import (
        SpotifyObjectPlaylistTracksInformation,
    )
    from ..models.spotify_object_user import SpotifyObjectUser


T = TypeVar("T", bound="SpotifyObjectPlaylistSimplified")


@_attrs_define
class SpotifyObjectPlaylistSimplified:
    """
    Attributes:
        collaborative (bool):
        description (str):
        external_urls (SpotifyObjectExternalUrl):
        href (str):
        id (str):
        images (List['SpotifyObjectImage']):
        name (str):
        owner (SpotifyObjectUser):
        public (bool):
        snapshot_id (str):
        tracks (SpotifyObjectPlaylistTracksInformation):
        type (Literal['playlist']):
        uri (str):
    """

    collaborative: bool
    description: str
    external_urls: "SpotifyObjectExternalUrl"
    href: str
    id: str
    images: List["SpotifyObjectImage"]
    name: str
    owner: "SpotifyObjectUser"
    public: bool
    snapshot_id: str
    tracks: "SpotifyObjectPlaylistTracksInformation"
    type: Literal["playlist"]
    uri: str

    def to_dict(self) -> Dict[str, Any]:
        collaborative = self.collaborative

        description = self.description

        external_urls = self.external_urls.to_dict()

        href = self.href

        id = self.id

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        name = self.name

        owner = self.owner.to_dict()

        public = self.public

        snapshot_id = self.snapshot_id

        tracks = self.tracks.to_dict()

        type = self.type

        uri = self.uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "collaborative": collaborative,
                "description": description,
                "external_urls": external_urls,
                "href": href,
                "id": id,
                "images": images,
                "name": name,
                "owner": owner,
                "public": public,
                "snapshot_id": snapshot_id,
                "tracks": tracks,
                "type": type,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
        from ..models.spotify_object_image import SpotifyObjectImage
        from ..models.spotify_object_playlist_tracks_information import (
            SpotifyObjectPlaylistTracksInformation,
        )
        from ..models.spotify_object_user import SpotifyObjectUser

        d = src_dict.copy()
        collaborative = d.pop("collaborative")

        description = d.pop("description")

        external_urls = SpotifyObjectExternalUrl.from_dict(d.pop("external_urls"))

        href = d.pop("href")

        id = d.pop("id")

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = SpotifyObjectImage.from_dict(images_item_data)

            images.append(images_item)

        name = d.pop("name")

        owner = SpotifyObjectUser.from_dict(d.pop("owner"))

        public = d.pop("public")

        snapshot_id = d.pop("snapshot_id")

        tracks = SpotifyObjectPlaylistTracksInformation.from_dict(d.pop("tracks"))

        type = d.pop("type")

        uri = d.pop("uri")

        spotify_object_playlist_simplified = cls(
            collaborative=collaborative,
            description=description,
            external_urls=external_urls,
            href=href,
            id=id,
            images=images,
            name=name,
            owner=owner,
            public=public,
            snapshot_id=snapshot_id,
            tracks=tracks,
            type=type,
            uri=uri,
        )

        return spotify_object_playlist_simplified
