from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_request_query_params_put_mealbums import (
        SpotifyRequestQueryParamsPUTMealbums,
    )
    from ..models.spotify_request_query_params_put_meepisodes import (
        SpotifyRequestQueryParamsPUTMeepisodes,
    )
    from ..models.spotify_request_query_params_put_mefollowing import (
        SpotifyRequestQueryParamsPUTMefollowing,
    )
    from ..models.spotify_request_query_params_put_meplayerpause import (
        SpotifyRequestQueryParamsPUTMeplayerpause,
    )
    from ..models.spotify_request_query_params_put_meplayerplay import (
        SpotifyRequestQueryParamsPUTMeplayerplay,
    )
    from ..models.spotify_request_query_params_put_meplayerrepeat import (
        SpotifyRequestQueryParamsPUTMeplayerrepeat,
    )
    from ..models.spotify_request_query_params_put_meplayerseek import (
        SpotifyRequestQueryParamsPUTMeplayerseek,
    )
    from ..models.spotify_request_query_params_put_meplayershuffle import (
        SpotifyRequestQueryParamsPUTMeplayershuffle,
    )
    from ..models.spotify_request_query_params_put_meplayervolume import (
        SpotifyRequestQueryParamsPUTMeplayervolume,
    )
    from ..models.spotify_request_query_params_put_meshows import (
        SpotifyRequestQueryParamsPUTMeshows,
    )
    from ..models.spotify_request_query_params_put_metracks import (
        SpotifyRequestQueryParamsPUTMetracks,
    )


T = TypeVar("T", bound="SpotifyRequestQueryParamsPUT")


@_attrs_define
class SpotifyRequestQueryParamsPUT:
    """
    Attributes:
        mealbums (SpotifyRequestQueryParamsPUTMealbums):
        meepisodes (SpotifyRequestQueryParamsPUTMeepisodes):
        mefollowing (SpotifyRequestQueryParamsPUTMefollowing):
        meplayerpause (SpotifyRequestQueryParamsPUTMeplayerpause):
        meplayerplay (SpotifyRequestQueryParamsPUTMeplayerplay):
        meplayerrepeat (SpotifyRequestQueryParamsPUTMeplayerrepeat):
        meplayerseek (SpotifyRequestQueryParamsPUTMeplayerseek):
        meplayershuffle (SpotifyRequestQueryParamsPUTMeplayershuffle):
        meplayervolume (SpotifyRequestQueryParamsPUTMeplayervolume):
        meshows (SpotifyRequestQueryParamsPUTMeshows):
        metracks (SpotifyRequestQueryParamsPUTMetracks):
    """

    mealbums: "SpotifyRequestQueryParamsPUTMealbums"
    meepisodes: "SpotifyRequestQueryParamsPUTMeepisodes"
    mefollowing: "SpotifyRequestQueryParamsPUTMefollowing"
    meplayerpause: "SpotifyRequestQueryParamsPUTMeplayerpause"
    meplayerplay: "SpotifyRequestQueryParamsPUTMeplayerplay"
    meplayerrepeat: "SpotifyRequestQueryParamsPUTMeplayerrepeat"
    meplayerseek: "SpotifyRequestQueryParamsPUTMeplayerseek"
    meplayershuffle: "SpotifyRequestQueryParamsPUTMeplayershuffle"
    meplayervolume: "SpotifyRequestQueryParamsPUTMeplayervolume"
    meshows: "SpotifyRequestQueryParamsPUTMeshows"
    metracks: "SpotifyRequestQueryParamsPUTMetracks"

    def to_dict(self) -> Dict[str, Any]:
        mealbums = self.mealbums.to_dict()

        meepisodes = self.meepisodes.to_dict()

        mefollowing = self.mefollowing.to_dict()

        meplayerpause = self.meplayerpause.to_dict()

        meplayerplay = self.meplayerplay.to_dict()

        meplayerrepeat = self.meplayerrepeat.to_dict()

        meplayerseek = self.meplayerseek.to_dict()

        meplayershuffle = self.meplayershuffle.to_dict()

        meplayervolume = self.meplayervolume.to_dict()

        meshows = self.meshows.to_dict()

        metracks = self.metracks.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "/me/albums": mealbums,
                "/me/episodes": meepisodes,
                "/me/following": mefollowing,
                "/me/player/pause": meplayerpause,
                "/me/player/play": meplayerplay,
                "/me/player/repeat": meplayerrepeat,
                "/me/player/seek": meplayerseek,
                "/me/player/shuffle": meplayershuffle,
                "/me/player/volume": meplayervolume,
                "/me/shows": meshows,
                "/me/tracks": metracks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_request_query_params_put_mealbums import (
            SpotifyRequestQueryParamsPUTMealbums,
        )
        from ..models.spotify_request_query_params_put_meepisodes import (
            SpotifyRequestQueryParamsPUTMeepisodes,
        )
        from ..models.spotify_request_query_params_put_mefollowing import (
            SpotifyRequestQueryParamsPUTMefollowing,
        )
        from ..models.spotify_request_query_params_put_meplayerpause import (
            SpotifyRequestQueryParamsPUTMeplayerpause,
        )
        from ..models.spotify_request_query_params_put_meplayerplay import (
            SpotifyRequestQueryParamsPUTMeplayerplay,
        )
        from ..models.spotify_request_query_params_put_meplayerrepeat import (
            SpotifyRequestQueryParamsPUTMeplayerrepeat,
        )
        from ..models.spotify_request_query_params_put_meplayerseek import (
            SpotifyRequestQueryParamsPUTMeplayerseek,
        )
        from ..models.spotify_request_query_params_put_meplayershuffle import (
            SpotifyRequestQueryParamsPUTMeplayershuffle,
        )
        from ..models.spotify_request_query_params_put_meplayervolume import (
            SpotifyRequestQueryParamsPUTMeplayervolume,
        )
        from ..models.spotify_request_query_params_put_meshows import (
            SpotifyRequestQueryParamsPUTMeshows,
        )
        from ..models.spotify_request_query_params_put_metracks import (
            SpotifyRequestQueryParamsPUTMetracks,
        )

        d = src_dict.copy()
        mealbums = SpotifyRequestQueryParamsPUTMealbums.from_dict(d.pop("/me/albums"))

        meepisodes = SpotifyRequestQueryParamsPUTMeepisodes.from_dict(
            d.pop("/me/episodes")
        )

        mefollowing = SpotifyRequestQueryParamsPUTMefollowing.from_dict(
            d.pop("/me/following")
        )

        meplayerpause = SpotifyRequestQueryParamsPUTMeplayerpause.from_dict(
            d.pop("/me/player/pause")
        )

        meplayerplay = SpotifyRequestQueryParamsPUTMeplayerplay.from_dict(
            d.pop("/me/player/play")
        )

        meplayerrepeat = SpotifyRequestQueryParamsPUTMeplayerrepeat.from_dict(
            d.pop("/me/player/repeat")
        )

        meplayerseek = SpotifyRequestQueryParamsPUTMeplayerseek.from_dict(
            d.pop("/me/player/seek")
        )

        meplayershuffle = SpotifyRequestQueryParamsPUTMeplayershuffle.from_dict(
            d.pop("/me/player/shuffle")
        )

        meplayervolume = SpotifyRequestQueryParamsPUTMeplayervolume.from_dict(
            d.pop("/me/player/volume")
        )

        meshows = SpotifyRequestQueryParamsPUTMeshows.from_dict(d.pop("/me/shows"))

        metracks = SpotifyRequestQueryParamsPUTMetracks.from_dict(d.pop("/me/tracks"))

        spotify_request_query_params_put = cls(
            mealbums=mealbums,
            meepisodes=meepisodes,
            mefollowing=mefollowing,
            meplayerpause=meplayerpause,
            meplayerplay=meplayerplay,
            meplayerrepeat=meplayerrepeat,
            meplayerseek=meplayerseek,
            meplayershuffle=meplayershuffle,
            meplayervolume=meplayervolume,
            meshows=meshows,
            metracks=metracks,
        )

        return spotify_request_query_params_put
