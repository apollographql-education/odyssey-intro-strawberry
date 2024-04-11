from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_request_query_params_delete_mealbums import (
        SpotifyRequestQueryParamsDELETEMealbums,
    )
    from ..models.spotify_request_query_params_delete_meepisodes import (
        SpotifyRequestQueryParamsDELETEMeepisodes,
    )
    from ..models.spotify_request_query_params_delete_mefollowing import (
        SpotifyRequestQueryParamsDELETEMefollowing,
    )
    from ..models.spotify_request_query_params_delete_meshows import (
        SpotifyRequestQueryParamsDELETEMeshows,
    )
    from ..models.spotify_request_query_params_delete_metracks import (
        SpotifyRequestQueryParamsDELETEMetracks,
    )


T = TypeVar("T", bound="SpotifyRequestQueryParamsDELETE")


@_attrs_define
class SpotifyRequestQueryParamsDELETE:
    """
    Attributes:
        mealbums (SpotifyRequestQueryParamsDELETEMealbums):
        meepisodes (SpotifyRequestQueryParamsDELETEMeepisodes):
        mefollowing (SpotifyRequestQueryParamsDELETEMefollowing):
        meshows (SpotifyRequestQueryParamsDELETEMeshows):
        metracks (SpotifyRequestQueryParamsDELETEMetracks):
    """

    mealbums: "SpotifyRequestQueryParamsDELETEMealbums"
    meepisodes: "SpotifyRequestQueryParamsDELETEMeepisodes"
    mefollowing: "SpotifyRequestQueryParamsDELETEMefollowing"
    meshows: "SpotifyRequestQueryParamsDELETEMeshows"
    metracks: "SpotifyRequestQueryParamsDELETEMetracks"

    def to_dict(self) -> Dict[str, Any]:
        mealbums = self.mealbums.to_dict()

        meepisodes = self.meepisodes.to_dict()

        mefollowing = self.mefollowing.to_dict()

        meshows = self.meshows.to_dict()

        metracks = self.metracks.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "/me/albums": mealbums,
                "/me/episodes": meepisodes,
                "/me/following": mefollowing,
                "/me/shows": meshows,
                "/me/tracks": metracks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_request_query_params_delete_mealbums import (
            SpotifyRequestQueryParamsDELETEMealbums,
        )
        from ..models.spotify_request_query_params_delete_meepisodes import (
            SpotifyRequestQueryParamsDELETEMeepisodes,
        )
        from ..models.spotify_request_query_params_delete_mefollowing import (
            SpotifyRequestQueryParamsDELETEMefollowing,
        )
        from ..models.spotify_request_query_params_delete_meshows import (
            SpotifyRequestQueryParamsDELETEMeshows,
        )
        from ..models.spotify_request_query_params_delete_metracks import (
            SpotifyRequestQueryParamsDELETEMetracks,
        )

        d = src_dict.copy()
        mealbums = SpotifyRequestQueryParamsDELETEMealbums.from_dict(
            d.pop("/me/albums")
        )

        meepisodes = SpotifyRequestQueryParamsDELETEMeepisodes.from_dict(
            d.pop("/me/episodes")
        )

        mefollowing = SpotifyRequestQueryParamsDELETEMefollowing.from_dict(
            d.pop("/me/following")
        )

        meshows = SpotifyRequestQueryParamsDELETEMeshows.from_dict(d.pop("/me/shows"))

        metracks = SpotifyRequestQueryParamsDELETEMetracks.from_dict(
            d.pop("/me/tracks")
        )

        spotify_request_query_params_delete = cls(
            mealbums=mealbums,
            meepisodes=meepisodes,
            mefollowing=mefollowing,
            meshows=meshows,
            metracks=metracks,
        )

        return spotify_request_query_params_delete
