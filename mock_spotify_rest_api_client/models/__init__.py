"""Contains all the data models used in inputs/outputs"""

from .search_include_external import SearchIncludeExternal
from .search_search_type import SearchSearchType
from .spotify_error_authentication_error import SpotifyErrorAuthenticationError
from .spotify_error_regular_error import SpotifyErrorRegularError
from .spotify_error_regular_error_error import SpotifyErrorRegularErrorError
from .spotify_http_method import SpotifyHTTPMethod
from .spotify_object_actions import SpotifyObjectActions
from .spotify_object_album import SpotifyObjectAlbum
from .spotify_object_album_group import SpotifyObjectAlbumGroup
from .spotify_object_album_simplified import SpotifyObjectAlbumSimplified
from .spotify_object_album_type import SpotifyObjectAlbumType
from .spotify_object_artist import SpotifyObjectArtist
from .spotify_object_artist_simplified import SpotifyObjectArtistSimplified
from .spotify_object_artist_top_tracks import SpotifyObjectArtistTopTracks
from .spotify_object_authorization_code_credentials import (
    SpotifyObjectAuthorizationCodeCredentials,
)
from .spotify_object_context import SpotifyObjectContext
from .spotify_object_context_type import SpotifyObjectContextType
from .spotify_object_copyright import SpotifyObjectCopyright
from .spotify_object_copyright_type import SpotifyObjectCopyrightType
from .spotify_object_current_user import SpotifyObjectCurrentUser
from .spotify_object_currently_playing import SpotifyObjectCurrentlyPlaying
from .spotify_object_currently_playing_type import SpotifyObjectCurrentlyPlayingType
from .spotify_object_cursors import SpotifyObjectCursors
from .spotify_object_device import SpotifyObjectDevice
from .spotify_object_disallows import SpotifyObjectDisallows
from .spotify_object_episode import SpotifyObjectEpisode
from .spotify_object_episode_simplified import SpotifyObjectEpisodeSimplified
from .spotify_object_explicit_content_settings import (
    SpotifyObjectExplicitContentSettings,
)
from .spotify_object_external_id import SpotifyObjectExternalId
from .spotify_object_external_url import SpotifyObjectExternalUrl
from .spotify_object_featured_playlists import SpotifyObjectFeaturedPlaylists
from .spotify_object_followers import SpotifyObjectFollowers
from .spotify_object_image import SpotifyObjectImage
from .spotify_object_listalbums_spotify_object_album import (
    SpotifyObjectListalbumsSpotifyObjectAlbum,
)
from .spotify_object_listartists_spotify_object_artist import (
    SpotifyObjectListartistsSpotifyObjectArtist,
)
from .spotify_object_listaudio_features_spotify_object_track_audio_features import (
    SpotifyObjectListaudioFeaturesSpotifyObjectTrackAudioFeatures,
)
from .spotify_object_listdevices_spotify_object_device import (
    SpotifyObjectListdevicesSpotifyObjectDevice,
)
from .spotify_object_listepisodes_spotify_object_episode import (
    SpotifyObjectListepisodesSpotifyObjectEpisode,
)
from .spotify_object_listgenresstring import SpotifyObjectListgenresstring
from .spotify_object_listshows_spotify_object_show import (
    SpotifyObjectListshowsSpotifyObjectShow,
)
from .spotify_object_listtracks_spotify_object_track import (
    SpotifyObjectListtracksSpotifyObjectTrack,
)
from .spotify_object_new_releases import SpotifyObjectNewReleases
from .spotify_object_paginated_cursor_based_spotify_object_artist import (
    SpotifyObjectPaginatedCursorBasedSpotifyObjectArtist,
)
from .spotify_object_paginated_cursor_based_spotify_object_play_history import (
    SpotifyObjectPaginatedCursorBasedSpotifyObjectPlayHistory,
)
from .spotify_object_paginated_spotify_object_album_simplified import (
    SpotifyObjectPaginatedSpotifyObjectAlbumSimplified,
)
from .spotify_object_paginated_spotify_object_artist import (
    SpotifyObjectPaginatedSpotifyObjectArtist,
)
from .spotify_object_paginated_spotify_object_episode_simplified import (
    SpotifyObjectPaginatedSpotifyObjectEpisodeSimplified,
)
from .spotify_object_paginated_spotify_object_playlist import (
    SpotifyObjectPaginatedSpotifyObjectPlaylist,
)
from .spotify_object_paginated_spotify_object_playlist_simplified import (
    SpotifyObjectPaginatedSpotifyObjectPlaylistSimplified,
)
from .spotify_object_paginated_spotify_object_playlist_track import (
    SpotifyObjectPaginatedSpotifyObjectPlaylistTrack,
)
from .spotify_object_paginated_spotify_object_saved_album import (
    SpotifyObjectPaginatedSpotifyObjectSavedAlbum,
)
from .spotify_object_paginated_spotify_object_saved_episode import (
    SpotifyObjectPaginatedSpotifyObjectSavedEpisode,
)
from .spotify_object_paginated_spotify_object_saved_show import (
    SpotifyObjectPaginatedSpotifyObjectSavedShow,
)
from .spotify_object_paginated_spotify_object_saved_track import (
    SpotifyObjectPaginatedSpotifyObjectSavedTrack,
)
from .spotify_object_paginated_spotify_object_show_simplified import (
    SpotifyObjectPaginatedSpotifyObjectShowSimplified,
)
from .spotify_object_paginated_spotify_object_track import (
    SpotifyObjectPaginatedSpotifyObjectTrack,
)
from .spotify_object_paginated_spotify_object_track_simplified import (
    SpotifyObjectPaginatedSpotifyObjectTrackSimplified,
)
from .spotify_object_play_history import SpotifyObjectPlayHistory
from .spotify_object_playback_queue import SpotifyObjectPlaybackQueue
from .spotify_object_playback_state import SpotifyObjectPlaybackState
from .spotify_object_playlist import SpotifyObjectPlaylist
from .spotify_object_playlist_episode_artist import SpotifyObjectPlaylistEpisodeArtist
from .spotify_object_playlist_episode_item import SpotifyObjectPlaylistEpisodeItem
from .spotify_object_playlist_episode_show import SpotifyObjectPlaylistEpisodeShow
from .spotify_object_playlist_simplified import SpotifyObjectPlaylistSimplified
from .spotify_object_playlist_track import SpotifyObjectPlaylistTrack
from .spotify_object_playlist_track_item import SpotifyObjectPlaylistTrackItem
from .spotify_object_playlist_track_video_thumbnail import (
    SpotifyObjectPlaylistTrackVideoThumbnail,
)
from .spotify_object_playlist_tracks_information import (
    SpotifyObjectPlaylistTracksInformation,
)
from .spotify_object_recommendation_seed import SpotifyObjectRecommendationSeed
from .spotify_object_recommendation_seed_type import SpotifyObjectRecommendationSeedType
from .spotify_object_recommendations import SpotifyObjectRecommendations
from .spotify_object_release_date_precision import SpotifyObjectReleaseDatePrecision
from .spotify_object_repeat_mode import SpotifyObjectRepeatMode
from .spotify_object_restrictions import SpotifyObjectRestrictions
from .spotify_object_restrictions_reason import SpotifyObjectRestrictionsReason
from .spotify_object_resume_point import SpotifyObjectResumePoint
from .spotify_object_saved_album import SpotifyObjectSavedAlbum
from .spotify_object_saved_episode import SpotifyObjectSavedEpisode
from .spotify_object_saved_show import SpotifyObjectSavedShow
from .spotify_object_saved_track import SpotifyObjectSavedTrack
from .spotify_object_search_results import SpotifyObjectSearchResults
from .spotify_object_show import SpotifyObjectShow
from .spotify_object_show_simplified import SpotifyObjectShowSimplified
from .spotify_object_snapshot import SpotifyObjectSnapshot
from .spotify_object_track import SpotifyObjectTrack
from .spotify_object_track_audio_features import SpotifyObjectTrackAudioFeatures
from .spotify_object_track_simplified import SpotifyObjectTrackSimplified
from .spotify_object_track_simplified_linked_from import (
    SpotifyObjectTrackSimplifiedLinkedFrom,
)
from .spotify_object_user import SpotifyObjectUser
from .spotify_object_user_simplified import SpotifyObjectUserSimplified
from .spotify_request_body_params_delete import SpotifyRequestBodyParamsDELETE
from .spotify_request_body_params_delete_mealbums import (
    SpotifyRequestBodyParamsDELETEMealbums,
)
from .spotify_request_body_params_delete_meepisodes import (
    SpotifyRequestBodyParamsDELETEMeepisodes,
)
from .spotify_request_body_params_delete_mefollowing import (
    SpotifyRequestBodyParamsDELETEMefollowing,
)
from .spotify_request_body_params_delete_metracks import (
    SpotifyRequestBodyParamsDELETEMetracks,
)
from .spotify_request_body_params_delete_playlistsidtracks import (
    SpotifyRequestBodyParamsDELETEPlaylistsidtracks,
)
from .spotify_request_body_params_delete_playlistsidtracks_tracks_item import (
    SpotifyRequestBodyParamsDELETEPlaylistsidtracksTracksItem,
)
from .spotify_request_body_params_paths import SpotifyRequestBodyParamsPaths
from .spotify_request_body_params_post import SpotifyRequestBodyParamsPOST
from .spotify_request_body_params_post_playlistsidtracks import (
    SpotifyRequestBodyParamsPOSTPlaylistsidtracks,
)
from .spotify_request_body_params_put import SpotifyRequestBodyParamsPUT
from .spotify_request_body_params_put_mealbums import (
    SpotifyRequestBodyParamsPUTMealbums,
)
from .spotify_request_body_params_put_meepisodes import (
    SpotifyRequestBodyParamsPUTMeepisodes,
)
from .spotify_request_body_params_put_mefollowing import (
    SpotifyRequestBodyParamsPUTMefollowing,
)
from .spotify_request_body_params_put_meplayer import (
    SpotifyRequestBodyParamsPUTMeplayer,
)
from .spotify_request_body_params_put_meplayerplay import (
    SpotifyRequestBodyParamsPUTMeplayerplay,
)
from .spotify_request_body_params_put_meplayerplay_offset import (
    SpotifyRequestBodyParamsPUTMeplayerplayOffset,
)
from .spotify_request_body_params_put_playlistsidfollowers import (
    SpotifyRequestBodyParamsPUTPlaylistsidfollowers,
)
from .spotify_request_query_params_delete import SpotifyRequestQueryParamsDELETE
from .spotify_request_query_params_delete_mealbums import (
    SpotifyRequestQueryParamsDELETEMealbums,
)
from .spotify_request_query_params_delete_meepisodes import (
    SpotifyRequestQueryParamsDELETEMeepisodes,
)
from .spotify_request_query_params_delete_mefollowing import (
    SpotifyRequestQueryParamsDELETEMefollowing,
)
from .spotify_request_query_params_delete_mefollowing_type import (
    SpotifyRequestQueryParamsDELETEMefollowingType,
)
from .spotify_request_query_params_delete_meshows import (
    SpotifyRequestQueryParamsDELETEMeshows,
)
from .spotify_request_query_params_delete_metracks import (
    SpotifyRequestQueryParamsDELETEMetracks,
)
from .spotify_request_query_params_get import SpotifyRequestQueryParamsGET
from .spotify_request_query_params_get_albums import SpotifyRequestQueryParamsGETAlbums
from .spotify_request_query_params_get_albumsid import (
    SpotifyRequestQueryParamsGETAlbumsid,
)
from .spotify_request_query_params_get_albumsidtracks import (
    SpotifyRequestQueryParamsGETAlbumsidtracks,
)
from .spotify_request_query_params_get_artists import (
    SpotifyRequestQueryParamsGETArtists,
)
from .spotify_request_query_params_get_artistsidalbums import (
    SpotifyRequestQueryParamsGETArtistsidalbums,
)
from .spotify_request_query_params_get_artistsidtop_tracks import (
    SpotifyRequestQueryParamsGETArtistsidtopTracks,
)
from .spotify_request_query_params_get_audio_features import (
    SpotifyRequestQueryParamsGETAudioFeatures,
)
from .spotify_request_query_params_get_browsefeatured_playlists import (
    SpotifyRequestQueryParamsGETBrowsefeaturedPlaylists,
)
from .spotify_request_query_params_get_browsenew_releases import (
    SpotifyRequestQueryParamsGETBrowsenewReleases,
)
from .spotify_request_query_params_get_episodes import (
    SpotifyRequestQueryParamsGETEpisodes,
)
from .spotify_request_query_params_get_mealbums import (
    SpotifyRequestQueryParamsGETMealbums,
)
from .spotify_request_query_params_get_mealbumscontains import (
    SpotifyRequestQueryParamsGETMealbumscontains,
)
from .spotify_request_query_params_get_meepisodes import (
    SpotifyRequestQueryParamsGETMeepisodes,
)
from .spotify_request_query_params_get_meepisodescontains import (
    SpotifyRequestQueryParamsGETMeepisodescontains,
)
from .spotify_request_query_params_get_mefollowing import (
    SpotifyRequestQueryParamsGETMefollowing,
)
from .spotify_request_query_params_get_mefollowingcontains import (
    SpotifyRequestQueryParamsGETMefollowingcontains,
)
from .spotify_request_query_params_get_mefollowingcontains_type import (
    SpotifyRequestQueryParamsGETMefollowingcontainsType,
)
from .spotify_request_query_params_get_meplayer import (
    SpotifyRequestQueryParamsGETMeplayer,
)
from .spotify_request_query_params_get_meplayercurrently_playing import (
    SpotifyRequestQueryParamsGETMeplayercurrentlyPlaying,
)
from .spotify_request_query_params_get_meplayerrecently_played import (
    SpotifyRequestQueryParamsGETMeplayerrecentlyPlayed,
)
from .spotify_request_query_params_get_meplaylists import (
    SpotifyRequestQueryParamsGETMeplaylists,
)
from .spotify_request_query_params_get_meshows import (
    SpotifyRequestQueryParamsGETMeshows,
)
from .spotify_request_query_params_get_meshowscontains import (
    SpotifyRequestQueryParamsGETMeshowscontains,
)
from .spotify_request_query_params_get_metopartists import (
    SpotifyRequestQueryParamsGETMetopartists,
)
from .spotify_request_query_params_get_metopartists_time_range import (
    SpotifyRequestQueryParamsGETMetopartistsTimeRange,
)
from .spotify_request_query_params_get_metoptracks import (
    SpotifyRequestQueryParamsGETMetoptracks,
)
from .spotify_request_query_params_get_metoptracks_time_range import (
    SpotifyRequestQueryParamsGETMetoptracksTimeRange,
)
from .spotify_request_query_params_get_metracks import (
    SpotifyRequestQueryParamsGETMetracks,
)
from .spotify_request_query_params_get_metrackscontains import (
    SpotifyRequestQueryParamsGETMetrackscontains,
)
from .spotify_request_query_params_get_playlistsid import (
    SpotifyRequestQueryParamsGETPlaylistsid,
)
from .spotify_request_query_params_get_playlistsidfollowerscontains import (
    SpotifyRequestQueryParamsGETPlaylistsidfollowerscontains,
)
from .spotify_request_query_params_get_playlistsidtracks import (
    SpotifyRequestQueryParamsGETPlaylistsidtracks,
)
from .spotify_request_query_params_get_recommendations import (
    SpotifyRequestQueryParamsGETRecommendations,
)
from .spotify_request_query_params_get_search import SpotifyRequestQueryParamsGETSearch
from .spotify_request_query_params_get_shows import SpotifyRequestQueryParamsGETShows
from .spotify_request_query_params_get_showsidepisodes import (
    SpotifyRequestQueryParamsGETShowsidepisodes,
)
from .spotify_request_query_params_get_tracks import SpotifyRequestQueryParamsGETTracks
from .spotify_request_query_params_get_tracksid import (
    SpotifyRequestQueryParamsGETTracksid,
)
from .spotify_request_query_params_paths import SpotifyRequestQueryParamsPaths
from .spotify_request_query_params_post import SpotifyRequestQueryParamsPOST
from .spotify_request_query_params_post_meplayernext import (
    SpotifyRequestQueryParamsPOSTMeplayernext,
)
from .spotify_request_query_params_post_meplayerprevious import (
    SpotifyRequestQueryParamsPOSTMeplayerprevious,
)
from .spotify_request_query_params_post_meplayerqueue import (
    SpotifyRequestQueryParamsPOSTMeplayerqueue,
)
from .spotify_request_query_params_post_playlistsidtracks import (
    SpotifyRequestQueryParamsPOSTPlaylistsidtracks,
)
from .spotify_request_query_params_put import SpotifyRequestQueryParamsPUT
from .spotify_request_query_params_put_mealbums import (
    SpotifyRequestQueryParamsPUTMealbums,
)
from .spotify_request_query_params_put_meepisodes import (
    SpotifyRequestQueryParamsPUTMeepisodes,
)
from .spotify_request_query_params_put_mefollowing import (
    SpotifyRequestQueryParamsPUTMefollowing,
)
from .spotify_request_query_params_put_mefollowing_type import (
    SpotifyRequestQueryParamsPUTMefollowingType,
)
from .spotify_request_query_params_put_meplayerpause import (
    SpotifyRequestQueryParamsPUTMeplayerpause,
)
from .spotify_request_query_params_put_meplayerplay import (
    SpotifyRequestQueryParamsPUTMeplayerplay,
)
from .spotify_request_query_params_put_meplayerrepeat import (
    SpotifyRequestQueryParamsPUTMeplayerrepeat,
)
from .spotify_request_query_params_put_meplayerseek import (
    SpotifyRequestQueryParamsPUTMeplayerseek,
)
from .spotify_request_query_params_put_meplayershuffle import (
    SpotifyRequestQueryParamsPUTMeplayershuffle,
)
from .spotify_request_query_params_put_meplayervolume import (
    SpotifyRequestQueryParamsPUTMeplayervolume,
)
from .spotify_request_query_params_put_meshows import (
    SpotifyRequestQueryParamsPUTMeshows,
)
from .spotify_request_query_params_put_metracks import (
    SpotifyRequestQueryParamsPUTMetracks,
)
from .spotify_response_delete import SpotifyResponseDELETE
from .spotify_response_delete_playlistsidtracks import (
    SpotifyResponseDELETEPlaylistsidtracks,
)
from .spotify_response_get import SpotifyResponseGET
from .spotify_response_get_authorize_type_0 import SpotifyResponseGETAuthorizeType0
from .spotify_response_get_authorize_type_1 import SpotifyResponseGETAuthorizeType1
from .spotify_response_get_mefollowing import SpotifyResponseGETMefollowing
from .spotify_response_post import SpotifyResponsePOST
from .spotify_response_post_playlistsidtracks import (
    SpotifyResponsePOSTPlaylistsidtracks,
)

__all__ = (
    "SearchIncludeExternal",
    "SearchSearchType",
    "SpotifyErrorAuthenticationError",
    "SpotifyErrorRegularError",
    "SpotifyErrorRegularErrorError",
    "SpotifyHTTPMethod",
    "SpotifyObjectActions",
    "SpotifyObjectAlbum",
    "SpotifyObjectAlbumGroup",
    "SpotifyObjectAlbumSimplified",
    "SpotifyObjectAlbumType",
    "SpotifyObjectArtist",
    "SpotifyObjectArtistSimplified",
    "SpotifyObjectArtistTopTracks",
    "SpotifyObjectAuthorizationCodeCredentials",
    "SpotifyObjectContext",
    "SpotifyObjectContextType",
    "SpotifyObjectCopyright",
    "SpotifyObjectCopyrightType",
    "SpotifyObjectCurrentlyPlaying",
    "SpotifyObjectCurrentlyPlayingType",
    "SpotifyObjectCurrentUser",
    "SpotifyObjectCursors",
    "SpotifyObjectDevice",
    "SpotifyObjectDisallows",
    "SpotifyObjectEpisode",
    "SpotifyObjectEpisodeSimplified",
    "SpotifyObjectExplicitContentSettings",
    "SpotifyObjectExternalId",
    "SpotifyObjectExternalUrl",
    "SpotifyObjectFeaturedPlaylists",
    "SpotifyObjectFollowers",
    "SpotifyObjectImage",
    "SpotifyObjectListalbumsSpotifyObjectAlbum",
    "SpotifyObjectListartistsSpotifyObjectArtist",
    "SpotifyObjectListaudioFeaturesSpotifyObjectTrackAudioFeatures",
    "SpotifyObjectListdevicesSpotifyObjectDevice",
    "SpotifyObjectListepisodesSpotifyObjectEpisode",
    "SpotifyObjectListgenresstring",
    "SpotifyObjectListshowsSpotifyObjectShow",
    "SpotifyObjectListtracksSpotifyObjectTrack",
    "SpotifyObjectNewReleases",
    "SpotifyObjectPaginatedCursorBasedSpotifyObjectArtist",
    "SpotifyObjectPaginatedCursorBasedSpotifyObjectPlayHistory",
    "SpotifyObjectPaginatedSpotifyObjectAlbumSimplified",
    "SpotifyObjectPaginatedSpotifyObjectArtist",
    "SpotifyObjectPaginatedSpotifyObjectEpisodeSimplified",
    "SpotifyObjectPaginatedSpotifyObjectPlaylist",
    "SpotifyObjectPaginatedSpotifyObjectPlaylistSimplified",
    "SpotifyObjectPaginatedSpotifyObjectPlaylistTrack",
    "SpotifyObjectPaginatedSpotifyObjectSavedAlbum",
    "SpotifyObjectPaginatedSpotifyObjectSavedEpisode",
    "SpotifyObjectPaginatedSpotifyObjectSavedShow",
    "SpotifyObjectPaginatedSpotifyObjectSavedTrack",
    "SpotifyObjectPaginatedSpotifyObjectShowSimplified",
    "SpotifyObjectPaginatedSpotifyObjectTrack",
    "SpotifyObjectPaginatedSpotifyObjectTrackSimplified",
    "SpotifyObjectPlaybackQueue",
    "SpotifyObjectPlaybackState",
    "SpotifyObjectPlayHistory",
    "SpotifyObjectPlaylist",
    "SpotifyObjectPlaylistEpisodeArtist",
    "SpotifyObjectPlaylistEpisodeItem",
    "SpotifyObjectPlaylistEpisodeShow",
    "SpotifyObjectPlaylistSimplified",
    "SpotifyObjectPlaylistTrack",
    "SpotifyObjectPlaylistTrackItem",
    "SpotifyObjectPlaylistTracksInformation",
    "SpotifyObjectPlaylistTrackVideoThumbnail",
    "SpotifyObjectRecommendations",
    "SpotifyObjectRecommendationSeed",
    "SpotifyObjectRecommendationSeedType",
    "SpotifyObjectReleaseDatePrecision",
    "SpotifyObjectRepeatMode",
    "SpotifyObjectRestrictions",
    "SpotifyObjectRestrictionsReason",
    "SpotifyObjectResumePoint",
    "SpotifyObjectSavedAlbum",
    "SpotifyObjectSavedEpisode",
    "SpotifyObjectSavedShow",
    "SpotifyObjectSavedTrack",
    "SpotifyObjectSearchResults",
    "SpotifyObjectShow",
    "SpotifyObjectShowSimplified",
    "SpotifyObjectSnapshot",
    "SpotifyObjectTrack",
    "SpotifyObjectTrackAudioFeatures",
    "SpotifyObjectTrackSimplified",
    "SpotifyObjectTrackSimplifiedLinkedFrom",
    "SpotifyObjectUser",
    "SpotifyObjectUserSimplified",
    "SpotifyRequestBodyParamsDELETE",
    "SpotifyRequestBodyParamsDELETEMealbums",
    "SpotifyRequestBodyParamsDELETEMeepisodes",
    "SpotifyRequestBodyParamsDELETEMefollowing",
    "SpotifyRequestBodyParamsDELETEMetracks",
    "SpotifyRequestBodyParamsDELETEPlaylistsidtracks",
    "SpotifyRequestBodyParamsDELETEPlaylistsidtracksTracksItem",
    "SpotifyRequestBodyParamsPaths",
    "SpotifyRequestBodyParamsPOST",
    "SpotifyRequestBodyParamsPOSTPlaylistsidtracks",
    "SpotifyRequestBodyParamsPUT",
    "SpotifyRequestBodyParamsPUTMealbums",
    "SpotifyRequestBodyParamsPUTMeepisodes",
    "SpotifyRequestBodyParamsPUTMefollowing",
    "SpotifyRequestBodyParamsPUTMeplayer",
    "SpotifyRequestBodyParamsPUTMeplayerplay",
    "SpotifyRequestBodyParamsPUTMeplayerplayOffset",
    "SpotifyRequestBodyParamsPUTPlaylistsidfollowers",
    "SpotifyRequestQueryParamsDELETE",
    "SpotifyRequestQueryParamsDELETEMealbums",
    "SpotifyRequestQueryParamsDELETEMeepisodes",
    "SpotifyRequestQueryParamsDELETEMefollowing",
    "SpotifyRequestQueryParamsDELETEMefollowingType",
    "SpotifyRequestQueryParamsDELETEMeshows",
    "SpotifyRequestQueryParamsDELETEMetracks",
    "SpotifyRequestQueryParamsGET",
    "SpotifyRequestQueryParamsGETAlbums",
    "SpotifyRequestQueryParamsGETAlbumsid",
    "SpotifyRequestQueryParamsGETAlbumsidtracks",
    "SpotifyRequestQueryParamsGETArtists",
    "SpotifyRequestQueryParamsGETArtistsidalbums",
    "SpotifyRequestQueryParamsGETArtistsidtopTracks",
    "SpotifyRequestQueryParamsGETAudioFeatures",
    "SpotifyRequestQueryParamsGETBrowsefeaturedPlaylists",
    "SpotifyRequestQueryParamsGETBrowsenewReleases",
    "SpotifyRequestQueryParamsGETEpisodes",
    "SpotifyRequestQueryParamsGETMealbums",
    "SpotifyRequestQueryParamsGETMealbumscontains",
    "SpotifyRequestQueryParamsGETMeepisodes",
    "SpotifyRequestQueryParamsGETMeepisodescontains",
    "SpotifyRequestQueryParamsGETMefollowing",
    "SpotifyRequestQueryParamsGETMefollowingcontains",
    "SpotifyRequestQueryParamsGETMefollowingcontainsType",
    "SpotifyRequestQueryParamsGETMeplayer",
    "SpotifyRequestQueryParamsGETMeplayercurrentlyPlaying",
    "SpotifyRequestQueryParamsGETMeplayerrecentlyPlayed",
    "SpotifyRequestQueryParamsGETMeplaylists",
    "SpotifyRequestQueryParamsGETMeshows",
    "SpotifyRequestQueryParamsGETMeshowscontains",
    "SpotifyRequestQueryParamsGETMetopartists",
    "SpotifyRequestQueryParamsGETMetopartistsTimeRange",
    "SpotifyRequestQueryParamsGETMetoptracks",
    "SpotifyRequestQueryParamsGETMetoptracksTimeRange",
    "SpotifyRequestQueryParamsGETMetracks",
    "SpotifyRequestQueryParamsGETMetrackscontains",
    "SpotifyRequestQueryParamsGETPlaylistsid",
    "SpotifyRequestQueryParamsGETPlaylistsidfollowerscontains",
    "SpotifyRequestQueryParamsGETPlaylistsidtracks",
    "SpotifyRequestQueryParamsGETRecommendations",
    "SpotifyRequestQueryParamsGETSearch",
    "SpotifyRequestQueryParamsGETShows",
    "SpotifyRequestQueryParamsGETShowsidepisodes",
    "SpotifyRequestQueryParamsGETTracks",
    "SpotifyRequestQueryParamsGETTracksid",
    "SpotifyRequestQueryParamsPaths",
    "SpotifyRequestQueryParamsPOST",
    "SpotifyRequestQueryParamsPOSTMeplayernext",
    "SpotifyRequestQueryParamsPOSTMeplayerprevious",
    "SpotifyRequestQueryParamsPOSTMeplayerqueue",
    "SpotifyRequestQueryParamsPOSTPlaylistsidtracks",
    "SpotifyRequestQueryParamsPUT",
    "SpotifyRequestQueryParamsPUTMealbums",
    "SpotifyRequestQueryParamsPUTMeepisodes",
    "SpotifyRequestQueryParamsPUTMefollowing",
    "SpotifyRequestQueryParamsPUTMefollowingType",
    "SpotifyRequestQueryParamsPUTMeplayerpause",
    "SpotifyRequestQueryParamsPUTMeplayerplay",
    "SpotifyRequestQueryParamsPUTMeplayerrepeat",
    "SpotifyRequestQueryParamsPUTMeplayerseek",
    "SpotifyRequestQueryParamsPUTMeplayershuffle",
    "SpotifyRequestQueryParamsPUTMeplayervolume",
    "SpotifyRequestQueryParamsPUTMeshows",
    "SpotifyRequestQueryParamsPUTMetracks",
    "SpotifyResponseDELETE",
    "SpotifyResponseDELETEPlaylistsidtracks",
    "SpotifyResponseGET",
    "SpotifyResponseGETAuthorizeType0",
    "SpotifyResponseGETAuthorizeType1",
    "SpotifyResponseGETMefollowing",
    "SpotifyResponsePOST",
    "SpotifyResponsePOSTPlaylistsidtracks",
)
