from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_request_query_params_get_albums import (
        SpotifyRequestQueryParamsGETAlbums,
    )
    from ..models.spotify_request_query_params_get_albumsid import (
        SpotifyRequestQueryParamsGETAlbumsid,
    )
    from ..models.spotify_request_query_params_get_albumsidtracks import (
        SpotifyRequestQueryParamsGETAlbumsidtracks,
    )
    from ..models.spotify_request_query_params_get_artists import (
        SpotifyRequestQueryParamsGETArtists,
    )
    from ..models.spotify_request_query_params_get_artistsidalbums import (
        SpotifyRequestQueryParamsGETArtistsidalbums,
    )
    from ..models.spotify_request_query_params_get_artistsidtop_tracks import (
        SpotifyRequestQueryParamsGETArtistsidtopTracks,
    )
    from ..models.spotify_request_query_params_get_audio_features import (
        SpotifyRequestQueryParamsGETAudioFeatures,
    )
    from ..models.spotify_request_query_params_get_browsefeatured_playlists import (
        SpotifyRequestQueryParamsGETBrowsefeaturedPlaylists,
    )
    from ..models.spotify_request_query_params_get_browsenew_releases import (
        SpotifyRequestQueryParamsGETBrowsenewReleases,
    )
    from ..models.spotify_request_query_params_get_episodes import (
        SpotifyRequestQueryParamsGETEpisodes,
    )
    from ..models.spotify_request_query_params_get_mealbums import (
        SpotifyRequestQueryParamsGETMealbums,
    )
    from ..models.spotify_request_query_params_get_mealbumscontains import (
        SpotifyRequestQueryParamsGETMealbumscontains,
    )
    from ..models.spotify_request_query_params_get_meepisodes import (
        SpotifyRequestQueryParamsGETMeepisodes,
    )
    from ..models.spotify_request_query_params_get_meepisodescontains import (
        SpotifyRequestQueryParamsGETMeepisodescontains,
    )
    from ..models.spotify_request_query_params_get_mefollowing import (
        SpotifyRequestQueryParamsGETMefollowing,
    )
    from ..models.spotify_request_query_params_get_mefollowingcontains import (
        SpotifyRequestQueryParamsGETMefollowingcontains,
    )
    from ..models.spotify_request_query_params_get_meplayer import (
        SpotifyRequestQueryParamsGETMeplayer,
    )
    from ..models.spotify_request_query_params_get_meplayercurrently_playing import (
        SpotifyRequestQueryParamsGETMeplayercurrentlyPlaying,
    )
    from ..models.spotify_request_query_params_get_meplayerrecently_played import (
        SpotifyRequestQueryParamsGETMeplayerrecentlyPlayed,
    )
    from ..models.spotify_request_query_params_get_meplaylists import (
        SpotifyRequestQueryParamsGETMeplaylists,
    )
    from ..models.spotify_request_query_params_get_meshows import (
        SpotifyRequestQueryParamsGETMeshows,
    )
    from ..models.spotify_request_query_params_get_meshowscontains import (
        SpotifyRequestQueryParamsGETMeshowscontains,
    )
    from ..models.spotify_request_query_params_get_metopartists import (
        SpotifyRequestQueryParamsGETMetopartists,
    )
    from ..models.spotify_request_query_params_get_metoptracks import (
        SpotifyRequestQueryParamsGETMetoptracks,
    )
    from ..models.spotify_request_query_params_get_metracks import (
        SpotifyRequestQueryParamsGETMetracks,
    )
    from ..models.spotify_request_query_params_get_metrackscontains import (
        SpotifyRequestQueryParamsGETMetrackscontains,
    )
    from ..models.spotify_request_query_params_get_playlistsid import (
        SpotifyRequestQueryParamsGETPlaylistsid,
    )
    from ..models.spotify_request_query_params_get_playlistsidfollowerscontains import (
        SpotifyRequestQueryParamsGETPlaylistsidfollowerscontains,
    )
    from ..models.spotify_request_query_params_get_playlistsidtracks import (
        SpotifyRequestQueryParamsGETPlaylistsidtracks,
    )
    from ..models.spotify_request_query_params_get_recommendations import (
        SpotifyRequestQueryParamsGETRecommendations,
    )
    from ..models.spotify_request_query_params_get_search import (
        SpotifyRequestQueryParamsGETSearch,
    )
    from ..models.spotify_request_query_params_get_shows import (
        SpotifyRequestQueryParamsGETShows,
    )
    from ..models.spotify_request_query_params_get_showsidepisodes import (
        SpotifyRequestQueryParamsGETShowsidepisodes,
    )
    from ..models.spotify_request_query_params_get_tracks import (
        SpotifyRequestQueryParamsGETTracks,
    )
    from ..models.spotify_request_query_params_get_tracksid import (
        SpotifyRequestQueryParamsGETTracksid,
    )


T = TypeVar("T", bound="SpotifyRequestQueryParamsGET")


@_attrs_define
class SpotifyRequestQueryParamsGET:
    """
    Attributes:
        albums (SpotifyRequestQueryParamsGETAlbums):
        albumsid (SpotifyRequestQueryParamsGETAlbumsid):
        albumsidtracks (SpotifyRequestQueryParamsGETAlbumsidtracks):
        artists (SpotifyRequestQueryParamsGETArtists):
        artistsidalbums (SpotifyRequestQueryParamsGETArtistsidalbums):
        artistsidtop_tracks (SpotifyRequestQueryParamsGETArtistsidtopTracks):
        audio_features (SpotifyRequestQueryParamsGETAudioFeatures):
        browsefeatured_playlists (SpotifyRequestQueryParamsGETBrowsefeaturedPlaylists):
        browsenew_releases (SpotifyRequestQueryParamsGETBrowsenewReleases):
        episodes (SpotifyRequestQueryParamsGETEpisodes):
        recommendations (SpotifyRequestQueryParamsGETRecommendations):
        mealbums (SpotifyRequestQueryParamsGETMealbums):
        mealbumscontains (SpotifyRequestQueryParamsGETMealbumscontains):
        meepisodes (SpotifyRequestQueryParamsGETMeepisodes):
        meepisodescontains (SpotifyRequestQueryParamsGETMeepisodescontains):
        mefollowing (SpotifyRequestQueryParamsGETMefollowing):
        mefollowingcontains (SpotifyRequestQueryParamsGETMefollowingcontains):
        meshows (SpotifyRequestQueryParamsGETMeshows):
        meshowscontains (SpotifyRequestQueryParamsGETMeshowscontains):
        metopartists (SpotifyRequestQueryParamsGETMetopartists):
        metoptracks (SpotifyRequestQueryParamsGETMetoptracks):
        metrackscontains (SpotifyRequestQueryParamsGETMetrackscontains):
        meplayer (SpotifyRequestQueryParamsGETMeplayer):
        meplayercurrently_playing (SpotifyRequestQueryParamsGETMeplayercurrentlyPlaying):
        meplayerrecently_played (SpotifyRequestQueryParamsGETMeplayerrecentlyPlayed):
        meplaylists (SpotifyRequestQueryParamsGETMeplaylists):
        metracks (SpotifyRequestQueryParamsGETMetracks):
        playlistsidfollowerscontains (SpotifyRequestQueryParamsGETPlaylistsidfollowerscontains):
        playlistsidtracks (SpotifyRequestQueryParamsGETPlaylistsidtracks):
        playlistsid (SpotifyRequestQueryParamsGETPlaylistsid):
        search (SpotifyRequestQueryParamsGETSearch):
        shows (SpotifyRequestQueryParamsGETShows):
        showsidepisodes (SpotifyRequestQueryParamsGETShowsidepisodes):
        tracks (SpotifyRequestQueryParamsGETTracks):
        tracksid (SpotifyRequestQueryParamsGETTracksid):
    """

    albums: "SpotifyRequestQueryParamsGETAlbums"
    albumsid: "SpotifyRequestQueryParamsGETAlbumsid"
    albumsidtracks: "SpotifyRequestQueryParamsGETAlbumsidtracks"
    artists: "SpotifyRequestQueryParamsGETArtists"
    artistsidalbums: "SpotifyRequestQueryParamsGETArtistsidalbums"
    artistsidtop_tracks: "SpotifyRequestQueryParamsGETArtistsidtopTracks"
    audio_features: "SpotifyRequestQueryParamsGETAudioFeatures"
    browsefeatured_playlists: "SpotifyRequestQueryParamsGETBrowsefeaturedPlaylists"
    browsenew_releases: "SpotifyRequestQueryParamsGETBrowsenewReleases"
    episodes: "SpotifyRequestQueryParamsGETEpisodes"
    recommendations: "SpotifyRequestQueryParamsGETRecommendations"
    mealbums: "SpotifyRequestQueryParamsGETMealbums"
    mealbumscontains: "SpotifyRequestQueryParamsGETMealbumscontains"
    meepisodes: "SpotifyRequestQueryParamsGETMeepisodes"
    meepisodescontains: "SpotifyRequestQueryParamsGETMeepisodescontains"
    mefollowing: "SpotifyRequestQueryParamsGETMefollowing"
    mefollowingcontains: "SpotifyRequestQueryParamsGETMefollowingcontains"
    meshows: "SpotifyRequestQueryParamsGETMeshows"
    meshowscontains: "SpotifyRequestQueryParamsGETMeshowscontains"
    metopartists: "SpotifyRequestQueryParamsGETMetopartists"
    metoptracks: "SpotifyRequestQueryParamsGETMetoptracks"
    metrackscontains: "SpotifyRequestQueryParamsGETMetrackscontains"
    meplayer: "SpotifyRequestQueryParamsGETMeplayer"
    meplayercurrently_playing: "SpotifyRequestQueryParamsGETMeplayercurrentlyPlaying"
    meplayerrecently_played: "SpotifyRequestQueryParamsGETMeplayerrecentlyPlayed"
    meplaylists: "SpotifyRequestQueryParamsGETMeplaylists"
    metracks: "SpotifyRequestQueryParamsGETMetracks"
    playlistsidfollowerscontains: (
        "SpotifyRequestQueryParamsGETPlaylistsidfollowerscontains"
    )
    playlistsidtracks: "SpotifyRequestQueryParamsGETPlaylistsidtracks"
    playlistsid: "SpotifyRequestQueryParamsGETPlaylistsid"
    search: "SpotifyRequestQueryParamsGETSearch"
    shows: "SpotifyRequestQueryParamsGETShows"
    showsidepisodes: "SpotifyRequestQueryParamsGETShowsidepisodes"
    tracks: "SpotifyRequestQueryParamsGETTracks"
    tracksid: "SpotifyRequestQueryParamsGETTracksid"

    def to_dict(self) -> Dict[str, Any]:
        albums = self.albums.to_dict()

        albumsid = self.albumsid.to_dict()

        albumsidtracks = self.albumsidtracks.to_dict()

        artists = self.artists.to_dict()

        artistsidalbums = self.artistsidalbums.to_dict()

        artistsidtop_tracks = self.artistsidtop_tracks.to_dict()

        audio_features = self.audio_features.to_dict()

        browsefeatured_playlists = self.browsefeatured_playlists.to_dict()

        browsenew_releases = self.browsenew_releases.to_dict()

        episodes = self.episodes.to_dict()

        recommendations = self.recommendations.to_dict()

        mealbums = self.mealbums.to_dict()

        mealbumscontains = self.mealbumscontains.to_dict()

        meepisodes = self.meepisodes.to_dict()

        meepisodescontains = self.meepisodescontains.to_dict()

        mefollowing = self.mefollowing.to_dict()

        mefollowingcontains = self.mefollowingcontains.to_dict()

        meshows = self.meshows.to_dict()

        meshowscontains = self.meshowscontains.to_dict()

        metopartists = self.metopartists.to_dict()

        metoptracks = self.metoptracks.to_dict()

        metrackscontains = self.metrackscontains.to_dict()

        meplayer = self.meplayer.to_dict()

        meplayercurrently_playing = self.meplayercurrently_playing.to_dict()

        meplayerrecently_played = self.meplayerrecently_played.to_dict()

        meplaylists = self.meplaylists.to_dict()

        metracks = self.metracks.to_dict()

        playlistsidfollowerscontains = self.playlistsidfollowerscontains.to_dict()

        playlistsidtracks = self.playlistsidtracks.to_dict()

        playlistsid = self.playlistsid.to_dict()

        search = self.search.to_dict()

        shows = self.shows.to_dict()

        showsidepisodes = self.showsidepisodes.to_dict()

        tracks = self.tracks.to_dict()

        tracksid = self.tracksid.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "/albums": albums,
                "/albums/:id": albumsid,
                "/albums/:id/tracks": albumsidtracks,
                "/artists": artists,
                "/artists/:id/albums": artistsidalbums,
                "/artists/:id/top-tracks": artistsidtop_tracks,
                "/audio-features": audio_features,
                "/browse/featured-playlists": browsefeatured_playlists,
                "/browse/new-releases": browsenew_releases,
                "/episodes": episodes,
                "/recommendations": recommendations,
                "/me/albums": mealbums,
                "/me/albums/contains": mealbumscontains,
                "/me/episodes": meepisodes,
                "/me/episodes/contains": meepisodescontains,
                "/me/following": mefollowing,
                "/me/following/contains": mefollowingcontains,
                "/me/shows": meshows,
                "/me/shows/contains": meshowscontains,
                "/me/top/artists": metopartists,
                "/me/top/tracks": metoptracks,
                "/me/tracks/contains": metrackscontains,
                "/me/player": meplayer,
                "/me/player/currently-playing": meplayercurrently_playing,
                "/me/player/recently-played": meplayerrecently_played,
                "/me/playlists": meplaylists,
                "/me/tracks": metracks,
                "/playlists/:id/followers/contains": playlistsidfollowerscontains,
                "/playlists/:id/tracks": playlistsidtracks,
                "/playlists/:id": playlistsid,
                "/search": search,
                "/shows": shows,
                "/shows/:id/episodes": showsidepisodes,
                "/tracks": tracks,
                "/tracks/:id": tracksid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_request_query_params_get_albums import (
            SpotifyRequestQueryParamsGETAlbums,
        )
        from ..models.spotify_request_query_params_get_albumsid import (
            SpotifyRequestQueryParamsGETAlbumsid,
        )
        from ..models.spotify_request_query_params_get_albumsidtracks import (
            SpotifyRequestQueryParamsGETAlbumsidtracks,
        )
        from ..models.spotify_request_query_params_get_artists import (
            SpotifyRequestQueryParamsGETArtists,
        )
        from ..models.spotify_request_query_params_get_artistsidalbums import (
            SpotifyRequestQueryParamsGETArtistsidalbums,
        )
        from ..models.spotify_request_query_params_get_artistsidtop_tracks import (
            SpotifyRequestQueryParamsGETArtistsidtopTracks,
        )
        from ..models.spotify_request_query_params_get_audio_features import (
            SpotifyRequestQueryParamsGETAudioFeatures,
        )
        from ..models.spotify_request_query_params_get_browsefeatured_playlists import (
            SpotifyRequestQueryParamsGETBrowsefeaturedPlaylists,
        )
        from ..models.spotify_request_query_params_get_browsenew_releases import (
            SpotifyRequestQueryParamsGETBrowsenewReleases,
        )
        from ..models.spotify_request_query_params_get_episodes import (
            SpotifyRequestQueryParamsGETEpisodes,
        )
        from ..models.spotify_request_query_params_get_mealbums import (
            SpotifyRequestQueryParamsGETMealbums,
        )
        from ..models.spotify_request_query_params_get_mealbumscontains import (
            SpotifyRequestQueryParamsGETMealbumscontains,
        )
        from ..models.spotify_request_query_params_get_meepisodes import (
            SpotifyRequestQueryParamsGETMeepisodes,
        )
        from ..models.spotify_request_query_params_get_meepisodescontains import (
            SpotifyRequestQueryParamsGETMeepisodescontains,
        )
        from ..models.spotify_request_query_params_get_mefollowing import (
            SpotifyRequestQueryParamsGETMefollowing,
        )
        from ..models.spotify_request_query_params_get_mefollowingcontains import (
            SpotifyRequestQueryParamsGETMefollowingcontains,
        )
        from ..models.spotify_request_query_params_get_meplayer import (
            SpotifyRequestQueryParamsGETMeplayer,
        )
        from ..models.spotify_request_query_params_get_meplayercurrently_playing import (
            SpotifyRequestQueryParamsGETMeplayercurrentlyPlaying,
        )
        from ..models.spotify_request_query_params_get_meplayerrecently_played import (
            SpotifyRequestQueryParamsGETMeplayerrecentlyPlayed,
        )
        from ..models.spotify_request_query_params_get_meplaylists import (
            SpotifyRequestQueryParamsGETMeplaylists,
        )
        from ..models.spotify_request_query_params_get_meshows import (
            SpotifyRequestQueryParamsGETMeshows,
        )
        from ..models.spotify_request_query_params_get_meshowscontains import (
            SpotifyRequestQueryParamsGETMeshowscontains,
        )
        from ..models.spotify_request_query_params_get_metopartists import (
            SpotifyRequestQueryParamsGETMetopartists,
        )
        from ..models.spotify_request_query_params_get_metoptracks import (
            SpotifyRequestQueryParamsGETMetoptracks,
        )
        from ..models.spotify_request_query_params_get_metracks import (
            SpotifyRequestQueryParamsGETMetracks,
        )
        from ..models.spotify_request_query_params_get_metrackscontains import (
            SpotifyRequestQueryParamsGETMetrackscontains,
        )
        from ..models.spotify_request_query_params_get_playlistsid import (
            SpotifyRequestQueryParamsGETPlaylistsid,
        )
        from ..models.spotify_request_query_params_get_playlistsidfollowerscontains import (
            SpotifyRequestQueryParamsGETPlaylistsidfollowerscontains,
        )
        from ..models.spotify_request_query_params_get_playlistsidtracks import (
            SpotifyRequestQueryParamsGETPlaylistsidtracks,
        )
        from ..models.spotify_request_query_params_get_recommendations import (
            SpotifyRequestQueryParamsGETRecommendations,
        )
        from ..models.spotify_request_query_params_get_search import (
            SpotifyRequestQueryParamsGETSearch,
        )
        from ..models.spotify_request_query_params_get_shows import (
            SpotifyRequestQueryParamsGETShows,
        )
        from ..models.spotify_request_query_params_get_showsidepisodes import (
            SpotifyRequestQueryParamsGETShowsidepisodes,
        )
        from ..models.spotify_request_query_params_get_tracks import (
            SpotifyRequestQueryParamsGETTracks,
        )
        from ..models.spotify_request_query_params_get_tracksid import (
            SpotifyRequestQueryParamsGETTracksid,
        )

        d = src_dict.copy()
        albums = SpotifyRequestQueryParamsGETAlbums.from_dict(d.pop("/albums"))

        albumsid = SpotifyRequestQueryParamsGETAlbumsid.from_dict(d.pop("/albums/:id"))

        albumsidtracks = SpotifyRequestQueryParamsGETAlbumsidtracks.from_dict(
            d.pop("/albums/:id/tracks")
        )

        artists = SpotifyRequestQueryParamsGETArtists.from_dict(d.pop("/artists"))

        artistsidalbums = SpotifyRequestQueryParamsGETArtistsidalbums.from_dict(
            d.pop("/artists/:id/albums")
        )

        artistsidtop_tracks = SpotifyRequestQueryParamsGETArtistsidtopTracks.from_dict(
            d.pop("/artists/:id/top-tracks")
        )

        audio_features = SpotifyRequestQueryParamsGETAudioFeatures.from_dict(
            d.pop("/audio-features")
        )

        browsefeatured_playlists = (
            SpotifyRequestQueryParamsGETBrowsefeaturedPlaylists.from_dict(
                d.pop("/browse/featured-playlists")
            )
        )

        browsenew_releases = SpotifyRequestQueryParamsGETBrowsenewReleases.from_dict(
            d.pop("/browse/new-releases")
        )

        episodes = SpotifyRequestQueryParamsGETEpisodes.from_dict(d.pop("/episodes"))

        recommendations = SpotifyRequestQueryParamsGETRecommendations.from_dict(
            d.pop("/recommendations")
        )

        mealbums = SpotifyRequestQueryParamsGETMealbums.from_dict(d.pop("/me/albums"))

        mealbumscontains = SpotifyRequestQueryParamsGETMealbumscontains.from_dict(
            d.pop("/me/albums/contains")
        )

        meepisodes = SpotifyRequestQueryParamsGETMeepisodes.from_dict(
            d.pop("/me/episodes")
        )

        meepisodescontains = SpotifyRequestQueryParamsGETMeepisodescontains.from_dict(
            d.pop("/me/episodes/contains")
        )

        mefollowing = SpotifyRequestQueryParamsGETMefollowing.from_dict(
            d.pop("/me/following")
        )

        mefollowingcontains = SpotifyRequestQueryParamsGETMefollowingcontains.from_dict(
            d.pop("/me/following/contains")
        )

        meshows = SpotifyRequestQueryParamsGETMeshows.from_dict(d.pop("/me/shows"))

        meshowscontains = SpotifyRequestQueryParamsGETMeshowscontains.from_dict(
            d.pop("/me/shows/contains")
        )

        metopartists = SpotifyRequestQueryParamsGETMetopartists.from_dict(
            d.pop("/me/top/artists")
        )

        metoptracks = SpotifyRequestQueryParamsGETMetoptracks.from_dict(
            d.pop("/me/top/tracks")
        )

        metrackscontains = SpotifyRequestQueryParamsGETMetrackscontains.from_dict(
            d.pop("/me/tracks/contains")
        )

        meplayer = SpotifyRequestQueryParamsGETMeplayer.from_dict(d.pop("/me/player"))

        meplayercurrently_playing = (
            SpotifyRequestQueryParamsGETMeplayercurrentlyPlaying.from_dict(
                d.pop("/me/player/currently-playing")
            )
        )

        meplayerrecently_played = (
            SpotifyRequestQueryParamsGETMeplayerrecentlyPlayed.from_dict(
                d.pop("/me/player/recently-played")
            )
        )

        meplaylists = SpotifyRequestQueryParamsGETMeplaylists.from_dict(
            d.pop("/me/playlists")
        )

        metracks = SpotifyRequestQueryParamsGETMetracks.from_dict(d.pop("/me/tracks"))

        playlistsidfollowerscontains = (
            SpotifyRequestQueryParamsGETPlaylistsidfollowerscontains.from_dict(
                d.pop("/playlists/:id/followers/contains")
            )
        )

        playlistsidtracks = SpotifyRequestQueryParamsGETPlaylistsidtracks.from_dict(
            d.pop("/playlists/:id/tracks")
        )

        playlistsid = SpotifyRequestQueryParamsGETPlaylistsid.from_dict(
            d.pop("/playlists/:id")
        )

        search = SpotifyRequestQueryParamsGETSearch.from_dict(d.pop("/search"))

        shows = SpotifyRequestQueryParamsGETShows.from_dict(d.pop("/shows"))

        showsidepisodes = SpotifyRequestQueryParamsGETShowsidepisodes.from_dict(
            d.pop("/shows/:id/episodes")
        )

        tracks = SpotifyRequestQueryParamsGETTracks.from_dict(d.pop("/tracks"))

        tracksid = SpotifyRequestQueryParamsGETTracksid.from_dict(d.pop("/tracks/:id"))

        spotify_request_query_params_get = cls(
            albums=albums,
            albumsid=albumsid,
            albumsidtracks=albumsidtracks,
            artists=artists,
            artistsidalbums=artistsidalbums,
            artistsidtop_tracks=artistsidtop_tracks,
            audio_features=audio_features,
            browsefeatured_playlists=browsefeatured_playlists,
            browsenew_releases=browsenew_releases,
            episodes=episodes,
            recommendations=recommendations,
            mealbums=mealbums,
            mealbumscontains=mealbumscontains,
            meepisodes=meepisodes,
            meepisodescontains=meepisodescontains,
            mefollowing=mefollowing,
            mefollowingcontains=mefollowingcontains,
            meshows=meshows,
            meshowscontains=meshowscontains,
            metopartists=metopartists,
            metoptracks=metoptracks,
            metrackscontains=metrackscontains,
            meplayer=meplayer,
            meplayercurrently_playing=meplayercurrently_playing,
            meplayerrecently_played=meplayerrecently_played,
            meplaylists=meplaylists,
            metracks=metracks,
            playlistsidfollowerscontains=playlistsidfollowerscontains,
            playlistsidtracks=playlistsidtracks,
            playlistsid=playlistsid,
            search=search,
            shows=shows,
            showsidepisodes=showsidepisodes,
            tracks=tracks,
            tracksid=tracksid,
        )

        return spotify_request_query_params_get
