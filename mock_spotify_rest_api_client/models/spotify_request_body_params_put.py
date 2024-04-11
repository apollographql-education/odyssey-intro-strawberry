from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_request_body_params_put_mealbums import (
        SpotifyRequestBodyParamsPUTMealbums,
    )
    from ..models.spotify_request_body_params_put_meepisodes import (
        SpotifyRequestBodyParamsPUTMeepisodes,
    )
    from ..models.spotify_request_body_params_put_mefollowing import (
        SpotifyRequestBodyParamsPUTMefollowing,
    )
    from ..models.spotify_request_body_params_put_meplayer import (
        SpotifyRequestBodyParamsPUTMeplayer,
    )
    from ..models.spotify_request_body_params_put_meplayerplay import (
        SpotifyRequestBodyParamsPUTMeplayerplay,
    )
    from ..models.spotify_request_body_params_put_playlistsidfollowers import (
        SpotifyRequestBodyParamsPUTPlaylistsidfollowers,
    )


T = TypeVar("T", bound="SpotifyRequestBodyParamsPUT")


@_attrs_define
class SpotifyRequestBodyParamsPUT:
    """
    Attributes:
        mealbums (SpotifyRequestBodyParamsPUTMealbums):
        meepisodes (SpotifyRequestBodyParamsPUTMeepisodes):
        mefollowing (SpotifyRequestBodyParamsPUTMefollowing):
        meplayer (SpotifyRequestBodyParamsPUTMeplayer):
        meplayerplay (SpotifyRequestBodyParamsPUTMeplayerplay):
        playlistsidfollowers (SpotifyRequestBodyParamsPUTPlaylistsidfollowers):
    """

    mealbums: "SpotifyRequestBodyParamsPUTMealbums"
    meepisodes: "SpotifyRequestBodyParamsPUTMeepisodes"
    mefollowing: "SpotifyRequestBodyParamsPUTMefollowing"
    meplayer: "SpotifyRequestBodyParamsPUTMeplayer"
    meplayerplay: "SpotifyRequestBodyParamsPUTMeplayerplay"
    playlistsidfollowers: "SpotifyRequestBodyParamsPUTPlaylistsidfollowers"

    def to_dict(self) -> Dict[str, Any]:
        mealbums = self.mealbums.to_dict()

        meepisodes = self.meepisodes.to_dict()

        mefollowing = self.mefollowing.to_dict()

        meplayer = self.meplayer.to_dict()

        meplayerplay = self.meplayerplay.to_dict()

        playlistsidfollowers = self.playlistsidfollowers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "/me/albums": mealbums,
                "/me/episodes": meepisodes,
                "/me/following": mefollowing,
                "/me/player": meplayer,
                "/me/player/play": meplayerplay,
                "/playlists/:id/followers": playlistsidfollowers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_request_body_params_put_mealbums import (
            SpotifyRequestBodyParamsPUTMealbums,
        )
        from ..models.spotify_request_body_params_put_meepisodes import (
            SpotifyRequestBodyParamsPUTMeepisodes,
        )
        from ..models.spotify_request_body_params_put_mefollowing import (
            SpotifyRequestBodyParamsPUTMefollowing,
        )
        from ..models.spotify_request_body_params_put_meplayer import (
            SpotifyRequestBodyParamsPUTMeplayer,
        )
        from ..models.spotify_request_body_params_put_meplayerplay import (
            SpotifyRequestBodyParamsPUTMeplayerplay,
        )
        from ..models.spotify_request_body_params_put_playlistsidfollowers import (
            SpotifyRequestBodyParamsPUTPlaylistsidfollowers,
        )

        d = src_dict.copy()
        mealbums = SpotifyRequestBodyParamsPUTMealbums.from_dict(d.pop("/me/albums"))

        meepisodes = SpotifyRequestBodyParamsPUTMeepisodes.from_dict(
            d.pop("/me/episodes")
        )

        mefollowing = SpotifyRequestBodyParamsPUTMefollowing.from_dict(
            d.pop("/me/following")
        )

        meplayer = SpotifyRequestBodyParamsPUTMeplayer.from_dict(d.pop("/me/player"))

        meplayerplay = SpotifyRequestBodyParamsPUTMeplayerplay.from_dict(
            d.pop("/me/player/play")
        )

        playlistsidfollowers = (
            SpotifyRequestBodyParamsPUTPlaylistsidfollowers.from_dict(
                d.pop("/playlists/:id/followers")
            )
        )

        spotify_request_body_params_put = cls(
            mealbums=mealbums,
            meepisodes=meepisodes,
            mefollowing=mefollowing,
            meplayer=meplayer,
            meplayerplay=meplayerplay,
            playlistsidfollowers=playlistsidfollowers,
        )

        return spotify_request_body_params_put
