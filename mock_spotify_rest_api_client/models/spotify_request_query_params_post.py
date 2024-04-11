from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_request_query_params_post_meplayernext import (
        SpotifyRequestQueryParamsPOSTMeplayernext,
    )
    from ..models.spotify_request_query_params_post_meplayerprevious import (
        SpotifyRequestQueryParamsPOSTMeplayerprevious,
    )
    from ..models.spotify_request_query_params_post_meplayerqueue import (
        SpotifyRequestQueryParamsPOSTMeplayerqueue,
    )
    from ..models.spotify_request_query_params_post_playlistsidtracks import (
        SpotifyRequestQueryParamsPOSTPlaylistsidtracks,
    )


T = TypeVar("T", bound="SpotifyRequestQueryParamsPOST")


@_attrs_define
class SpotifyRequestQueryParamsPOST:
    """
    Attributes:
        meplayernext (SpotifyRequestQueryParamsPOSTMeplayernext):
        meplayerprevious (SpotifyRequestQueryParamsPOSTMeplayerprevious):
        meplayerqueue (SpotifyRequestQueryParamsPOSTMeplayerqueue):
        playlistsidtracks (SpotifyRequestQueryParamsPOSTPlaylistsidtracks):
    """

    meplayernext: "SpotifyRequestQueryParamsPOSTMeplayernext"
    meplayerprevious: "SpotifyRequestQueryParamsPOSTMeplayerprevious"
    meplayerqueue: "SpotifyRequestQueryParamsPOSTMeplayerqueue"
    playlistsidtracks: "SpotifyRequestQueryParamsPOSTPlaylistsidtracks"

    def to_dict(self) -> Dict[str, Any]:
        meplayernext = self.meplayernext.to_dict()

        meplayerprevious = self.meplayerprevious.to_dict()

        meplayerqueue = self.meplayerqueue.to_dict()

        playlistsidtracks = self.playlistsidtracks.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "/me/player/next": meplayernext,
                "/me/player/previous": meplayerprevious,
                "/me/player/queue": meplayerqueue,
                "/playlists/:id/tracks": playlistsidtracks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_request_query_params_post_meplayernext import (
            SpotifyRequestQueryParamsPOSTMeplayernext,
        )
        from ..models.spotify_request_query_params_post_meplayerprevious import (
            SpotifyRequestQueryParamsPOSTMeplayerprevious,
        )
        from ..models.spotify_request_query_params_post_meplayerqueue import (
            SpotifyRequestQueryParamsPOSTMeplayerqueue,
        )
        from ..models.spotify_request_query_params_post_playlistsidtracks import (
            SpotifyRequestQueryParamsPOSTPlaylistsidtracks,
        )

        d = src_dict.copy()
        meplayernext = SpotifyRequestQueryParamsPOSTMeplayernext.from_dict(
            d.pop("/me/player/next")
        )

        meplayerprevious = SpotifyRequestQueryParamsPOSTMeplayerprevious.from_dict(
            d.pop("/me/player/previous")
        )

        meplayerqueue = SpotifyRequestQueryParamsPOSTMeplayerqueue.from_dict(
            d.pop("/me/player/queue")
        )

        playlistsidtracks = SpotifyRequestQueryParamsPOSTPlaylistsidtracks.from_dict(
            d.pop("/playlists/:id/tracks")
        )

        spotify_request_query_params_post = cls(
            meplayernext=meplayernext,
            meplayerprevious=meplayerprevious,
            meplayerqueue=meplayerqueue,
            playlistsidtracks=playlistsidtracks,
        )

        return spotify_request_query_params_post
