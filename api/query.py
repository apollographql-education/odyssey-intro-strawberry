import strawberry

from .types.playlist import Playlist
from .types.track import Track

from mock_spotify_rest_api_client.api.playlists import get_playlist
from mock_spotify_rest_api_client.api.playlists import get_featured_playlists


@strawberry.type
class Query:
    @strawberry.field(description="Playlists hand-picked to be featured to all users.")
    async def featured_playlists(self, info: strawberry.Info) -> list[Playlist]:
        client = info.context["spotify_client"]

        data = await get_featured_playlists.asyncio(client=client)

        return [
            Playlist(
                id=strawberry.ID(playlist.id),
                name=playlist.name,
                description=playlist.description,
            )
            for playlist in data.playlists.items
        ]

    @strawberry.field(description="Retrieves a specific playlist.")
    async def playlist(
        self, info: strawberry.Info, playlist_id: strawberry.ID
    ) -> Playlist | None:
        client = info.context["spotify_client"]

        data = await get_playlist.asyncio(client=client, playlist_id=playlist_id)

        if data is None:
            return None

        return Playlist(
            id=strawberry.ID(data.id),
            name=data.name,
            description=data.description,
            _tracks=[
                Track(
                    id=strawberry.ID(item.track.id),
                    name=item.track.name,
                    duration_ms=item.track.duration_ms,
                    explicit=item.track.explicit,
                    uri=item.track.uri,
                )
                for item in data.tracks.items
            ],
        )
