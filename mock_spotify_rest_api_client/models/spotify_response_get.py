from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_album import SpotifyObjectAlbum
    from ..models.spotify_object_artist import SpotifyObjectArtist
    from ..models.spotify_object_artist_top_tracks import SpotifyObjectArtistTopTracks
    from ..models.spotify_object_authorization_code_credentials import (
        SpotifyObjectAuthorizationCodeCredentials,
    )
    from ..models.spotify_object_current_user import SpotifyObjectCurrentUser
    from ..models.spotify_object_currently_playing import SpotifyObjectCurrentlyPlaying
    from ..models.spotify_object_episode import SpotifyObjectEpisode
    from ..models.spotify_object_featured_playlists import (
        SpotifyObjectFeaturedPlaylists,
    )
    from ..models.spotify_object_listalbums_spotify_object_album import (
        SpotifyObjectListalbumsSpotifyObjectAlbum,
    )
    from ..models.spotify_object_listartists_spotify_object_artist import (
        SpotifyObjectListartistsSpotifyObjectArtist,
    )
    from ..models.spotify_object_listaudio_features_spotify_object_track_audio_features import (
        SpotifyObjectListaudioFeaturesSpotifyObjectTrackAudioFeatures,
    )
    from ..models.spotify_object_listdevices_spotify_object_device import (
        SpotifyObjectListdevicesSpotifyObjectDevice,
    )
    from ..models.spotify_object_listepisodes_spotify_object_episode import (
        SpotifyObjectListepisodesSpotifyObjectEpisode,
    )
    from ..models.spotify_object_listgenresstring import SpotifyObjectListgenresstring
    from ..models.spotify_object_listshows_spotify_object_show import (
        SpotifyObjectListshowsSpotifyObjectShow,
    )
    from ..models.spotify_object_listtracks_spotify_object_track import (
        SpotifyObjectListtracksSpotifyObjectTrack,
    )
    from ..models.spotify_object_new_releases import SpotifyObjectNewReleases
    from ..models.spotify_object_paginated_cursor_based_spotify_object_play_history import (
        SpotifyObjectPaginatedCursorBasedSpotifyObjectPlayHistory,
    )
    from ..models.spotify_object_paginated_spotify_object_album_simplified import (
        SpotifyObjectPaginatedSpotifyObjectAlbumSimplified,
    )
    from ..models.spotify_object_paginated_spotify_object_artist import (
        SpotifyObjectPaginatedSpotifyObjectArtist,
    )
    from ..models.spotify_object_paginated_spotify_object_episode_simplified import (
        SpotifyObjectPaginatedSpotifyObjectEpisodeSimplified,
    )
    from ..models.spotify_object_paginated_spotify_object_playlist import (
        SpotifyObjectPaginatedSpotifyObjectPlaylist,
    )
    from ..models.spotify_object_paginated_spotify_object_playlist_track import (
        SpotifyObjectPaginatedSpotifyObjectPlaylistTrack,
    )
    from ..models.spotify_object_paginated_spotify_object_saved_album import (
        SpotifyObjectPaginatedSpotifyObjectSavedAlbum,
    )
    from ..models.spotify_object_paginated_spotify_object_saved_episode import (
        SpotifyObjectPaginatedSpotifyObjectSavedEpisode,
    )
    from ..models.spotify_object_paginated_spotify_object_saved_show import (
        SpotifyObjectPaginatedSpotifyObjectSavedShow,
    )
    from ..models.spotify_object_paginated_spotify_object_saved_track import (
        SpotifyObjectPaginatedSpotifyObjectSavedTrack,
    )
    from ..models.spotify_object_paginated_spotify_object_track import (
        SpotifyObjectPaginatedSpotifyObjectTrack,
    )
    from ..models.spotify_object_paginated_spotify_object_track_simplified import (
        SpotifyObjectPaginatedSpotifyObjectTrackSimplified,
    )
    from ..models.spotify_object_playback_queue import SpotifyObjectPlaybackQueue
    from ..models.spotify_object_playback_state import SpotifyObjectPlaybackState
    from ..models.spotify_object_playlist import SpotifyObjectPlaylist
    from ..models.spotify_object_recommendations import SpotifyObjectRecommendations
    from ..models.spotify_object_search_results import SpotifyObjectSearchResults
    from ..models.spotify_object_show import SpotifyObjectShow
    from ..models.spotify_object_track import SpotifyObjectTrack
    from ..models.spotify_object_track_audio_features import (
        SpotifyObjectTrackAudioFeatures,
    )
    from ..models.spotify_object_user import SpotifyObjectUser
    from ..models.spotify_response_get_authorize_type_0 import (
        SpotifyResponseGETAuthorizeType0,
    )
    from ..models.spotify_response_get_authorize_type_1 import (
        SpotifyResponseGETAuthorizeType1,
    )
    from ..models.spotify_response_get_mefollowing import SpotifyResponseGETMefollowing


T = TypeVar("T", bound="SpotifyResponseGET")


@_attrs_define
class SpotifyResponseGET:
    """
    Attributes:
        albums (SpotifyObjectListalbumsSpotifyObjectAlbum):
        albumsid (SpotifyObjectAlbum):
        albumsidtracks (SpotifyObjectPaginatedSpotifyObjectTrackSimplified):
        artists (SpotifyObjectListartistsSpotifyObjectArtist):
        artistsid (SpotifyObjectArtist):
        artistsidalbums (SpotifyObjectPaginatedSpotifyObjectAlbumSimplified):
        artistsidrelated_artists (SpotifyObjectListartistsSpotifyObjectArtist):
        artistsidtop_tracks (SpotifyObjectArtistTopTracks):
        audio_features (SpotifyObjectListaudioFeaturesSpotifyObjectTrackAudioFeatures):
        audio_featuresid (SpotifyObjectTrackAudioFeatures):
        authorize (Union['SpotifyResponseGETAuthorizeType0', 'SpotifyResponseGETAuthorizeType1']):
        apitoken (SpotifyObjectAuthorizationCodeCredentials):
        browsefeatured_playlists (SpotifyObjectFeaturedPlaylists):
        browsenew_releases (SpotifyObjectNewReleases):
        episodes (SpotifyObjectListepisodesSpotifyObjectEpisode):
        episodesid (SpotifyObjectEpisode):
        me (SpotifyObjectCurrentUser):
        mealbums (SpotifyObjectPaginatedSpotifyObjectSavedAlbum):
        mealbumscontains (List[bool]):
        meepisodes (SpotifyObjectPaginatedSpotifyObjectSavedEpisode):
        meepisodescontains (List[bool]):
        mefollowing (SpotifyResponseGETMefollowing):
        mefollowingcontains (List[bool]):
        meplayer (SpotifyObjectPlaybackState):
        meplayercurrently_playing (SpotifyObjectCurrentlyPlaying):
        meplayerdevices (SpotifyObjectListdevicesSpotifyObjectDevice):
        meplayerqueue (SpotifyObjectPlaybackQueue):
        meplayerrecently_played (SpotifyObjectPaginatedCursorBasedSpotifyObjectPlayHistory):
        meplaylists (SpotifyObjectPaginatedSpotifyObjectPlaylist):
        meshows (SpotifyObjectPaginatedSpotifyObjectSavedShow):
        meshowscontains (List[bool]):
        metopartists (SpotifyObjectPaginatedSpotifyObjectArtist):
        metoptracks (SpotifyObjectPaginatedSpotifyObjectTrack):
        metracks (SpotifyObjectPaginatedSpotifyObjectSavedTrack):
        metrackscontains (List[bool]):
        playlistsid (SpotifyObjectPlaylist):
        playlistsidfollowerscontains (List[bool]):
        playlistsidtracks (SpotifyObjectPaginatedSpotifyObjectPlaylistTrack):
        recommendations (SpotifyObjectRecommendations):
        recommendationsavailable_genre_seeds (SpotifyObjectListgenresstring):
        search (SpotifyObjectSearchResults):
        shows (SpotifyObjectListshowsSpotifyObjectShow):
        showsid (SpotifyObjectShow):
        showsidepisodes (SpotifyObjectPaginatedSpotifyObjectEpisodeSimplified):
        tracks (SpotifyObjectListtracksSpotifyObjectTrack):
        tracksid (SpotifyObjectTrack):
        usersid (SpotifyObjectUser):
    """

    albums: "SpotifyObjectListalbumsSpotifyObjectAlbum"
    albumsid: "SpotifyObjectAlbum"
    albumsidtracks: "SpotifyObjectPaginatedSpotifyObjectTrackSimplified"
    artists: "SpotifyObjectListartistsSpotifyObjectArtist"
    artistsid: "SpotifyObjectArtist"
    artistsidalbums: "SpotifyObjectPaginatedSpotifyObjectAlbumSimplified"
    artistsidrelated_artists: "SpotifyObjectListartistsSpotifyObjectArtist"
    artistsidtop_tracks: "SpotifyObjectArtistTopTracks"
    audio_features: "SpotifyObjectListaudioFeaturesSpotifyObjectTrackAudioFeatures"
    audio_featuresid: "SpotifyObjectTrackAudioFeatures"
    authorize: Union[
        "SpotifyResponseGETAuthorizeType0", "SpotifyResponseGETAuthorizeType1"
    ]
    apitoken: "SpotifyObjectAuthorizationCodeCredentials"
    browsefeatured_playlists: "SpotifyObjectFeaturedPlaylists"
    browsenew_releases: "SpotifyObjectNewReleases"
    episodes: "SpotifyObjectListepisodesSpotifyObjectEpisode"
    episodesid: "SpotifyObjectEpisode"
    me: "SpotifyObjectCurrentUser"
    mealbums: "SpotifyObjectPaginatedSpotifyObjectSavedAlbum"
    mealbumscontains: List[bool]
    meepisodes: "SpotifyObjectPaginatedSpotifyObjectSavedEpisode"
    meepisodescontains: List[bool]
    mefollowing: "SpotifyResponseGETMefollowing"
    mefollowingcontains: List[bool]
    meplayer: "SpotifyObjectPlaybackState"
    meplayercurrently_playing: "SpotifyObjectCurrentlyPlaying"
    meplayerdevices: "SpotifyObjectListdevicesSpotifyObjectDevice"
    meplayerqueue: "SpotifyObjectPlaybackQueue"
    meplayerrecently_played: "SpotifyObjectPaginatedCursorBasedSpotifyObjectPlayHistory"
    meplaylists: "SpotifyObjectPaginatedSpotifyObjectPlaylist"
    meshows: "SpotifyObjectPaginatedSpotifyObjectSavedShow"
    meshowscontains: List[bool]
    metopartists: "SpotifyObjectPaginatedSpotifyObjectArtist"
    metoptracks: "SpotifyObjectPaginatedSpotifyObjectTrack"
    metracks: "SpotifyObjectPaginatedSpotifyObjectSavedTrack"
    metrackscontains: List[bool]
    playlistsid: "SpotifyObjectPlaylist"
    playlistsidfollowerscontains: List[bool]
    playlistsidtracks: "SpotifyObjectPaginatedSpotifyObjectPlaylistTrack"
    recommendations: "SpotifyObjectRecommendations"
    recommendationsavailable_genre_seeds: "SpotifyObjectListgenresstring"
    search: "SpotifyObjectSearchResults"
    shows: "SpotifyObjectListshowsSpotifyObjectShow"
    showsid: "SpotifyObjectShow"
    showsidepisodes: "SpotifyObjectPaginatedSpotifyObjectEpisodeSimplified"
    tracks: "SpotifyObjectListtracksSpotifyObjectTrack"
    tracksid: "SpotifyObjectTrack"
    usersid: "SpotifyObjectUser"

    def to_dict(self) -> Dict[str, Any]:
        from ..models.spotify_response_get_authorize_type_0 import (
            SpotifyResponseGETAuthorizeType0,
        )

        albums = self.albums.to_dict()

        albumsid = self.albumsid.to_dict()

        albumsidtracks = self.albumsidtracks.to_dict()

        artists = self.artists.to_dict()

        artistsid = self.artistsid.to_dict()

        artistsidalbums = self.artistsidalbums.to_dict()

        artistsidrelated_artists = self.artistsidrelated_artists.to_dict()

        artistsidtop_tracks = self.artistsidtop_tracks.to_dict()

        audio_features = self.audio_features.to_dict()

        audio_featuresid = self.audio_featuresid.to_dict()

        authorize: Dict[str, Any]
        if isinstance(self.authorize, SpotifyResponseGETAuthorizeType0):
            authorize = self.authorize.to_dict()
        else:
            authorize = self.authorize.to_dict()

        apitoken = self.apitoken.to_dict()

        browsefeatured_playlists = self.browsefeatured_playlists.to_dict()

        browsenew_releases = self.browsenew_releases.to_dict()

        episodes = self.episodes.to_dict()

        episodesid = self.episodesid.to_dict()

        me = self.me.to_dict()

        mealbums = self.mealbums.to_dict()

        mealbumscontains = self.mealbumscontains

        meepisodes = self.meepisodes.to_dict()

        meepisodescontains = self.meepisodescontains

        mefollowing = self.mefollowing.to_dict()

        mefollowingcontains = self.mefollowingcontains

        meplayer = self.meplayer.to_dict()

        meplayercurrently_playing = self.meplayercurrently_playing.to_dict()

        meplayerdevices = self.meplayerdevices.to_dict()

        meplayerqueue = self.meplayerqueue.to_dict()

        meplayerrecently_played = self.meplayerrecently_played.to_dict()

        meplaylists = self.meplaylists.to_dict()

        meshows = self.meshows.to_dict()

        meshowscontains = self.meshowscontains

        metopartists = self.metopartists.to_dict()

        metoptracks = self.metoptracks.to_dict()

        metracks = self.metracks.to_dict()

        metrackscontains = self.metrackscontains

        playlistsid = self.playlistsid.to_dict()

        playlistsidfollowerscontains = self.playlistsidfollowerscontains

        playlistsidtracks = self.playlistsidtracks.to_dict()

        recommendations = self.recommendations.to_dict()

        recommendationsavailable_genre_seeds = (
            self.recommendationsavailable_genre_seeds.to_dict()
        )

        search = self.search.to_dict()

        shows = self.shows.to_dict()

        showsid = self.showsid.to_dict()

        showsidepisodes = self.showsidepisodes.to_dict()

        tracks = self.tracks.to_dict()

        tracksid = self.tracksid.to_dict()

        usersid = self.usersid.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "/albums": albums,
                "/albums/:id": albumsid,
                "/albums/:id/tracks": albumsidtracks,
                "/artists": artists,
                "/artists/:id": artistsid,
                "/artists/:id/albums": artistsidalbums,
                "/artists/:id/related-artists": artistsidrelated_artists,
                "/artists/:id/top-tracks": artistsidtop_tracks,
                "/audio-features": audio_features,
                "/audio-features/:id": audio_featuresid,
                "/authorize": authorize,
                "/api/token": apitoken,
                "/browse/featured-playlists": browsefeatured_playlists,
                "/browse/new-releases": browsenew_releases,
                "/episodes": episodes,
                "/episodes/:id": episodesid,
                "/me": me,
                "/me/albums": mealbums,
                "/me/albums/contains": mealbumscontains,
                "/me/episodes": meepisodes,
                "/me/episodes/contains": meepisodescontains,
                "/me/following": mefollowing,
                "/me/following/contains": mefollowingcontains,
                "/me/player": meplayer,
                "/me/player/currently-playing": meplayercurrently_playing,
                "/me/player/devices": meplayerdevices,
                "/me/player/queue": meplayerqueue,
                "/me/player/recently-played": meplayerrecently_played,
                "/me/playlists": meplaylists,
                "/me/shows": meshows,
                "/me/shows/contains": meshowscontains,
                "/me/top/artists": metopartists,
                "/me/top/tracks": metoptracks,
                "/me/tracks": metracks,
                "/me/tracks/contains": metrackscontains,
                "/playlists/:id": playlistsid,
                "/playlists/:id/followers/contains": playlistsidfollowerscontains,
                "/playlists/:id/tracks": playlistsidtracks,
                "/recommendations": recommendations,
                "/recommendations/available-genre-seeds": recommendationsavailable_genre_seeds,
                "/search": search,
                "/shows": shows,
                "/shows/:id": showsid,
                "/shows/:id/episodes": showsidepisodes,
                "/tracks": tracks,
                "/tracks/:id": tracksid,
                "/users/:id": usersid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_album import SpotifyObjectAlbum
        from ..models.spotify_object_artist import SpotifyObjectArtist
        from ..models.spotify_object_artist_top_tracks import (
            SpotifyObjectArtistTopTracks,
        )
        from ..models.spotify_object_authorization_code_credentials import (
            SpotifyObjectAuthorizationCodeCredentials,
        )
        from ..models.spotify_object_current_user import SpotifyObjectCurrentUser
        from ..models.spotify_object_currently_playing import (
            SpotifyObjectCurrentlyPlaying,
        )
        from ..models.spotify_object_episode import SpotifyObjectEpisode
        from ..models.spotify_object_featured_playlists import (
            SpotifyObjectFeaturedPlaylists,
        )
        from ..models.spotify_object_listalbums_spotify_object_album import (
            SpotifyObjectListalbumsSpotifyObjectAlbum,
        )
        from ..models.spotify_object_listartists_spotify_object_artist import (
            SpotifyObjectListartistsSpotifyObjectArtist,
        )
        from ..models.spotify_object_listaudio_features_spotify_object_track_audio_features import (
            SpotifyObjectListaudioFeaturesSpotifyObjectTrackAudioFeatures,
        )
        from ..models.spotify_object_listdevices_spotify_object_device import (
            SpotifyObjectListdevicesSpotifyObjectDevice,
        )
        from ..models.spotify_object_listepisodes_spotify_object_episode import (
            SpotifyObjectListepisodesSpotifyObjectEpisode,
        )
        from ..models.spotify_object_listgenresstring import (
            SpotifyObjectListgenresstring,
        )
        from ..models.spotify_object_listshows_spotify_object_show import (
            SpotifyObjectListshowsSpotifyObjectShow,
        )
        from ..models.spotify_object_listtracks_spotify_object_track import (
            SpotifyObjectListtracksSpotifyObjectTrack,
        )
        from ..models.spotify_object_new_releases import SpotifyObjectNewReleases
        from ..models.spotify_object_paginated_cursor_based_spotify_object_play_history import (
            SpotifyObjectPaginatedCursorBasedSpotifyObjectPlayHistory,
        )
        from ..models.spotify_object_paginated_spotify_object_album_simplified import (
            SpotifyObjectPaginatedSpotifyObjectAlbumSimplified,
        )
        from ..models.spotify_object_paginated_spotify_object_artist import (
            SpotifyObjectPaginatedSpotifyObjectArtist,
        )
        from ..models.spotify_object_paginated_spotify_object_episode_simplified import (
            SpotifyObjectPaginatedSpotifyObjectEpisodeSimplified,
        )
        from ..models.spotify_object_paginated_spotify_object_playlist import (
            SpotifyObjectPaginatedSpotifyObjectPlaylist,
        )
        from ..models.spotify_object_paginated_spotify_object_playlist_track import (
            SpotifyObjectPaginatedSpotifyObjectPlaylistTrack,
        )
        from ..models.spotify_object_paginated_spotify_object_saved_album import (
            SpotifyObjectPaginatedSpotifyObjectSavedAlbum,
        )
        from ..models.spotify_object_paginated_spotify_object_saved_episode import (
            SpotifyObjectPaginatedSpotifyObjectSavedEpisode,
        )
        from ..models.spotify_object_paginated_spotify_object_saved_show import (
            SpotifyObjectPaginatedSpotifyObjectSavedShow,
        )
        from ..models.spotify_object_paginated_spotify_object_saved_track import (
            SpotifyObjectPaginatedSpotifyObjectSavedTrack,
        )
        from ..models.spotify_object_paginated_spotify_object_track import (
            SpotifyObjectPaginatedSpotifyObjectTrack,
        )
        from ..models.spotify_object_paginated_spotify_object_track_simplified import (
            SpotifyObjectPaginatedSpotifyObjectTrackSimplified,
        )
        from ..models.spotify_object_playback_queue import SpotifyObjectPlaybackQueue
        from ..models.spotify_object_playback_state import SpotifyObjectPlaybackState
        from ..models.spotify_object_playlist import SpotifyObjectPlaylist
        from ..models.spotify_object_recommendations import SpotifyObjectRecommendations
        from ..models.spotify_object_search_results import SpotifyObjectSearchResults
        from ..models.spotify_object_show import SpotifyObjectShow
        from ..models.spotify_object_track import SpotifyObjectTrack
        from ..models.spotify_object_track_audio_features import (
            SpotifyObjectTrackAudioFeatures,
        )
        from ..models.spotify_object_user import SpotifyObjectUser
        from ..models.spotify_response_get_authorize_type_0 import (
            SpotifyResponseGETAuthorizeType0,
        )
        from ..models.spotify_response_get_authorize_type_1 import (
            SpotifyResponseGETAuthorizeType1,
        )
        from ..models.spotify_response_get_mefollowing import (
            SpotifyResponseGETMefollowing,
        )

        d = src_dict.copy()
        albums = SpotifyObjectListalbumsSpotifyObjectAlbum.from_dict(d.pop("/albums"))

        albumsid = SpotifyObjectAlbum.from_dict(d.pop("/albums/:id"))

        albumsidtracks = SpotifyObjectPaginatedSpotifyObjectTrackSimplified.from_dict(
            d.pop("/albums/:id/tracks")
        )

        artists = SpotifyObjectListartistsSpotifyObjectArtist.from_dict(
            d.pop("/artists")
        )

        artistsid = SpotifyObjectArtist.from_dict(d.pop("/artists/:id"))

        artistsidalbums = SpotifyObjectPaginatedSpotifyObjectAlbumSimplified.from_dict(
            d.pop("/artists/:id/albums")
        )

        artistsidrelated_artists = (
            SpotifyObjectListartistsSpotifyObjectArtist.from_dict(
                d.pop("/artists/:id/related-artists")
            )
        )

        artistsidtop_tracks = SpotifyObjectArtistTopTracks.from_dict(
            d.pop("/artists/:id/top-tracks")
        )

        audio_features = (
            SpotifyObjectListaudioFeaturesSpotifyObjectTrackAudioFeatures.from_dict(
                d.pop("/audio-features")
            )
        )

        audio_featuresid = SpotifyObjectTrackAudioFeatures.from_dict(
            d.pop("/audio-features/:id")
        )

        def _parse_authorize(
            data: object,
        ) -> Union[
            "SpotifyResponseGETAuthorizeType0", "SpotifyResponseGETAuthorizeType1"
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                authorize_type_0 = SpotifyResponseGETAuthorizeType0.from_dict(data)

                return authorize_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            authorize_type_1 = SpotifyResponseGETAuthorizeType1.from_dict(data)

            return authorize_type_1

        authorize = _parse_authorize(d.pop("/authorize"))

        apitoken = SpotifyObjectAuthorizationCodeCredentials.from_dict(
            d.pop("/api/token")
        )

        browsefeatured_playlists = SpotifyObjectFeaturedPlaylists.from_dict(
            d.pop("/browse/featured-playlists")
        )

        browsenew_releases = SpotifyObjectNewReleases.from_dict(
            d.pop("/browse/new-releases")
        )

        episodes = SpotifyObjectListepisodesSpotifyObjectEpisode.from_dict(
            d.pop("/episodes")
        )

        episodesid = SpotifyObjectEpisode.from_dict(d.pop("/episodes/:id"))

        me = SpotifyObjectCurrentUser.from_dict(d.pop("/me"))

        mealbums = SpotifyObjectPaginatedSpotifyObjectSavedAlbum.from_dict(
            d.pop("/me/albums")
        )

        mealbumscontains = cast(List[bool], d.pop("/me/albums/contains"))

        meepisodes = SpotifyObjectPaginatedSpotifyObjectSavedEpisode.from_dict(
            d.pop("/me/episodes")
        )

        meepisodescontains = cast(List[bool], d.pop("/me/episodes/contains"))

        mefollowing = SpotifyResponseGETMefollowing.from_dict(d.pop("/me/following"))

        mefollowingcontains = cast(List[bool], d.pop("/me/following/contains"))

        meplayer = SpotifyObjectPlaybackState.from_dict(d.pop("/me/player"))

        meplayercurrently_playing = SpotifyObjectCurrentlyPlaying.from_dict(
            d.pop("/me/player/currently-playing")
        )

        meplayerdevices = SpotifyObjectListdevicesSpotifyObjectDevice.from_dict(
            d.pop("/me/player/devices")
        )

        meplayerqueue = SpotifyObjectPlaybackQueue.from_dict(d.pop("/me/player/queue"))

        meplayerrecently_played = (
            SpotifyObjectPaginatedCursorBasedSpotifyObjectPlayHistory.from_dict(
                d.pop("/me/player/recently-played")
            )
        )

        meplaylists = SpotifyObjectPaginatedSpotifyObjectPlaylist.from_dict(
            d.pop("/me/playlists")
        )

        meshows = SpotifyObjectPaginatedSpotifyObjectSavedShow.from_dict(
            d.pop("/me/shows")
        )

        meshowscontains = cast(List[bool], d.pop("/me/shows/contains"))

        metopartists = SpotifyObjectPaginatedSpotifyObjectArtist.from_dict(
            d.pop("/me/top/artists")
        )

        metoptracks = SpotifyObjectPaginatedSpotifyObjectTrack.from_dict(
            d.pop("/me/top/tracks")
        )

        metracks = SpotifyObjectPaginatedSpotifyObjectSavedTrack.from_dict(
            d.pop("/me/tracks")
        )

        metrackscontains = cast(List[bool], d.pop("/me/tracks/contains"))

        playlistsid = SpotifyObjectPlaylist.from_dict(d.pop("/playlists/:id"))

        playlistsidfollowerscontains = cast(
            List[bool], d.pop("/playlists/:id/followers/contains")
        )

        playlistsidtracks = SpotifyObjectPaginatedSpotifyObjectPlaylistTrack.from_dict(
            d.pop("/playlists/:id/tracks")
        )

        recommendations = SpotifyObjectRecommendations.from_dict(
            d.pop("/recommendations")
        )

        recommendationsavailable_genre_seeds = SpotifyObjectListgenresstring.from_dict(
            d.pop("/recommendations/available-genre-seeds")
        )

        search = SpotifyObjectSearchResults.from_dict(d.pop("/search"))

        shows = SpotifyObjectListshowsSpotifyObjectShow.from_dict(d.pop("/shows"))

        showsid = SpotifyObjectShow.from_dict(d.pop("/shows/:id"))

        showsidepisodes = (
            SpotifyObjectPaginatedSpotifyObjectEpisodeSimplified.from_dict(
                d.pop("/shows/:id/episodes")
            )
        )

        tracks = SpotifyObjectListtracksSpotifyObjectTrack.from_dict(d.pop("/tracks"))

        tracksid = SpotifyObjectTrack.from_dict(d.pop("/tracks/:id"))

        usersid = SpotifyObjectUser.from_dict(d.pop("/users/:id"))

        spotify_response_get = cls(
            albums=albums,
            albumsid=albumsid,
            albumsidtracks=albumsidtracks,
            artists=artists,
            artistsid=artistsid,
            artistsidalbums=artistsidalbums,
            artistsidrelated_artists=artistsidrelated_artists,
            artistsidtop_tracks=artistsidtop_tracks,
            audio_features=audio_features,
            audio_featuresid=audio_featuresid,
            authorize=authorize,
            apitoken=apitoken,
            browsefeatured_playlists=browsefeatured_playlists,
            browsenew_releases=browsenew_releases,
            episodes=episodes,
            episodesid=episodesid,
            me=me,
            mealbums=mealbums,
            mealbumscontains=mealbumscontains,
            meepisodes=meepisodes,
            meepisodescontains=meepisodescontains,
            mefollowing=mefollowing,
            mefollowingcontains=mefollowingcontains,
            meplayer=meplayer,
            meplayercurrently_playing=meplayercurrently_playing,
            meplayerdevices=meplayerdevices,
            meplayerqueue=meplayerqueue,
            meplayerrecently_played=meplayerrecently_played,
            meplaylists=meplaylists,
            meshows=meshows,
            meshowscontains=meshowscontains,
            metopartists=metopartists,
            metoptracks=metoptracks,
            metracks=metracks,
            metrackscontains=metrackscontains,
            playlistsid=playlistsid,
            playlistsidfollowerscontains=playlistsidfollowerscontains,
            playlistsidtracks=playlistsidtracks,
            recommendations=recommendations,
            recommendationsavailable_genre_seeds=recommendationsavailable_genre_seeds,
            search=search,
            shows=shows,
            showsid=showsid,
            showsidepisodes=showsidepisodes,
            tracks=tracks,
            tracksid=tracksid,
            usersid=usersid,
        )

        return spotify_response_get
