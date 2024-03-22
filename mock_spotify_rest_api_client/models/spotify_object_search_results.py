from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spotify_object_paginated_spotify_object_album_simplified import (
        SpotifyObjectPaginatedSpotifyObjectAlbumSimplified,
    )
    from ..models.spotify_object_paginated_spotify_object_artist import (
        SpotifyObjectPaginatedSpotifyObjectArtist,
    )
    from ..models.spotify_object_paginated_spotify_object_episode_simplified import (
        SpotifyObjectPaginatedSpotifyObjectEpisodeSimplified,
    )
    from ..models.spotify_object_paginated_spotify_object_playlist_simplified import (
        SpotifyObjectPaginatedSpotifyObjectPlaylistSimplified,
    )
    from ..models.spotify_object_paginated_spotify_object_show_simplified import (
        SpotifyObjectPaginatedSpotifyObjectShowSimplified,
    )
    from ..models.spotify_object_paginated_spotify_object_track import (
        SpotifyObjectPaginatedSpotifyObjectTrack,
    )


T = TypeVar("T", bound="SpotifyObjectSearchResults")


@_attrs_define
class SpotifyObjectSearchResults:
    """
    Attributes:
        albums (Union[Unset, SpotifyObjectPaginatedSpotifyObjectAlbumSimplified]):
        artists (Union[Unset, SpotifyObjectPaginatedSpotifyObjectArtist]):
        episodes (Union[Unset, SpotifyObjectPaginatedSpotifyObjectEpisodeSimplified]):
        playlists (Union[Unset, SpotifyObjectPaginatedSpotifyObjectPlaylistSimplified]):
        tracks (Union[Unset, SpotifyObjectPaginatedSpotifyObjectTrack]):
        shows (Union[Unset, SpotifyObjectPaginatedSpotifyObjectShowSimplified]):
    """

    albums: Union[Unset, "SpotifyObjectPaginatedSpotifyObjectAlbumSimplified"] = UNSET
    artists: Union[Unset, "SpotifyObjectPaginatedSpotifyObjectArtist"] = UNSET
    episodes: Union[Unset, "SpotifyObjectPaginatedSpotifyObjectEpisodeSimplified"] = (
        UNSET
    )
    playlists: Union[Unset, "SpotifyObjectPaginatedSpotifyObjectPlaylistSimplified"] = (
        UNSET
    )
    tracks: Union[Unset, "SpotifyObjectPaginatedSpotifyObjectTrack"] = UNSET
    shows: Union[Unset, "SpotifyObjectPaginatedSpotifyObjectShowSimplified"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        albums: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.albums, Unset):
            albums = self.albums.to_dict()

        artists: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.artists, Unset):
            artists = self.artists.to_dict()

        episodes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.episodes, Unset):
            episodes = self.episodes.to_dict()

        playlists: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.playlists, Unset):
            playlists = self.playlists.to_dict()

        tracks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tracks, Unset):
            tracks = self.tracks.to_dict()

        shows: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shows, Unset):
            shows = self.shows.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if albums is not UNSET:
            field_dict["albums"] = albums
        if artists is not UNSET:
            field_dict["artists"] = artists
        if episodes is not UNSET:
            field_dict["episodes"] = episodes
        if playlists is not UNSET:
            field_dict["playlists"] = playlists
        if tracks is not UNSET:
            field_dict["tracks"] = tracks
        if shows is not UNSET:
            field_dict["shows"] = shows

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_paginated_spotify_object_album_simplified import (
            SpotifyObjectPaginatedSpotifyObjectAlbumSimplified,
        )
        from ..models.spotify_object_paginated_spotify_object_artist import (
            SpotifyObjectPaginatedSpotifyObjectArtist,
        )
        from ..models.spotify_object_paginated_spotify_object_episode_simplified import (
            SpotifyObjectPaginatedSpotifyObjectEpisodeSimplified,
        )
        from ..models.spotify_object_paginated_spotify_object_playlist_simplified import (
            SpotifyObjectPaginatedSpotifyObjectPlaylistSimplified,
        )
        from ..models.spotify_object_paginated_spotify_object_show_simplified import (
            SpotifyObjectPaginatedSpotifyObjectShowSimplified,
        )
        from ..models.spotify_object_paginated_spotify_object_track import (
            SpotifyObjectPaginatedSpotifyObjectTrack,
        )

        d = src_dict.copy()
        _albums = d.pop("albums", UNSET)
        albums: Union[Unset, SpotifyObjectPaginatedSpotifyObjectAlbumSimplified]
        if isinstance(_albums, Unset):
            albums = UNSET
        else:
            albums = SpotifyObjectPaginatedSpotifyObjectAlbumSimplified.from_dict(
                _albums
            )

        _artists = d.pop("artists", UNSET)
        artists: Union[Unset, SpotifyObjectPaginatedSpotifyObjectArtist]
        if isinstance(_artists, Unset):
            artists = UNSET
        else:
            artists = SpotifyObjectPaginatedSpotifyObjectArtist.from_dict(_artists)

        _episodes = d.pop("episodes", UNSET)
        episodes: Union[Unset, SpotifyObjectPaginatedSpotifyObjectEpisodeSimplified]
        if isinstance(_episodes, Unset):
            episodes = UNSET
        else:
            episodes = SpotifyObjectPaginatedSpotifyObjectEpisodeSimplified.from_dict(
                _episodes
            )

        _playlists = d.pop("playlists", UNSET)
        playlists: Union[Unset, SpotifyObjectPaginatedSpotifyObjectPlaylistSimplified]
        if isinstance(_playlists, Unset):
            playlists = UNSET
        else:
            playlists = SpotifyObjectPaginatedSpotifyObjectPlaylistSimplified.from_dict(
                _playlists
            )

        _tracks = d.pop("tracks", UNSET)
        tracks: Union[Unset, SpotifyObjectPaginatedSpotifyObjectTrack]
        if isinstance(_tracks, Unset):
            tracks = UNSET
        else:
            tracks = SpotifyObjectPaginatedSpotifyObjectTrack.from_dict(_tracks)

        _shows = d.pop("shows", UNSET)
        shows: Union[Unset, SpotifyObjectPaginatedSpotifyObjectShowSimplified]
        if isinstance(_shows, Unset):
            shows = UNSET
        else:
            shows = SpotifyObjectPaginatedSpotifyObjectShowSimplified.from_dict(_shows)

        spotify_object_search_results = cls(
            albums=albums,
            artists=artists,
            episodes=episodes,
            playlists=playlists,
            tracks=tracks,
            shows=shows,
        )

        return spotify_object_search_results
