from typing import TypedDict
import strawberry

from mock_spotify_rest_api_client.client import Client
from mock_spotify_rest_api_client.api.playlists import (
    get_featured_playlists,
    get_playlists_tracks,
    get_playlist,
    add_tracks_to_playlist,
)


class Context(TypedDict):
    spotify_client: Client


@strawberry.type(description="A single audio file, usually a song.")
class Track:
    id: str = strawberry.field(description="The ID for the track.")
    name: str = strawberry.field(description="The name of the track.")
    duration_ms: float = strawberry.field(
        description="The track length in milliseconds."
    )
    explicit: bool = strawberry.field(
        description="Whether or not the track has explicit lyrics."
    )
    uri: str = strawberry.field(
        description="The URI for the track, usually a Spotify link."
    )


@strawberry.type(
    description="A curated collection of tracks designed for a specific activity or mood."
)
class Playlist:
    id: strawberry.ID = strawberry.field(description="The ID for the playlist.")
    name: str = strawberry.field(description="The name of the playlist.")
    description: str | None = strawberry.field(
        description="Describes the playlist, what to expect and entices the user to listen."
    )

    @strawberry.field(description="The playlist's tracks.")
    async def tracks(self, info: strawberry.Info[Context]) -> list[Track]:
        client = info.context["spotify_client"]

        data = await get_playlists_tracks.asyncio(playlist_id=self.id, client=client)

        if data is None:
            return []

        # TODO: in the first iteration we want to fetch this inside playlist
        # and then explain why that's bad :)

        return [
            Track(
                id=track.track.id,
                name=track.track.name,
                duration_ms=track.track.duration_ms,
                explicit=track.track.explicit,
                uri=track.track.uri,
            )
            for track in data.items
        ]


@strawberry.type
class Query:
    @strawberry.field(description="Playlists hand-picked to be featured to all users.")
    async def featured_playlists(
        self, info: strawberry.Info[Context]
    ) -> list[Playlist]:
        client = info.context["spotify_client"]

        data = await get_featured_playlists.asyncio(client=client)

        if data is None:
            return []  # TODO: raise an error?

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
        self, info: strawberry.Info[Context], id: strawberry.ID
    ) -> Playlist | None:
        client = info.context["spotify_client"]
        data = await get_playlist.asyncio(playlist_id=id, client=client)

        if data is None:
            return None

        return Playlist(
            id=strawberry.ID(data.id),
            name=data.name,
            description=data.description,
        )


@strawberry.type
class AddItemsToPlaylistPayload:
    code: int = strawberry.field(
        description="Similar to HTTP status code, represents the status of the mutation."
    )
    success: bool = strawberry.field(
        description="Whether the mutation was successful or not."
    )
    message: str = strawberry.field(description="Human-readable message for the UI.")
    playlist: Playlist | None = strawberry.field(
        description="The playlist that contains the newly added items."
    )


@strawberry.input
class AddItemsToPlaylistInput:
    playlist_id: strawberry.ID = strawberry.field(description="The ID of the playlist.")
    uris: list[str] = strawberry.field(
        description="A comma-separated list of Spotify URIs to add."
    )


@strawberry.type
class Mutation:
    @strawberry.mutation(description="Add one or more items to a user's playlist.")
    async def add_items_to_playlist(
        self, info: strawberry.Info[Context], input: AddItemsToPlaylistInput
    ) -> AddItemsToPlaylistPayload:
        client = info.context["spotify_client"]
        data = await add_tracks_to_playlist.asyncio(
            playlist_id=input.playlist_id, uris=",".join(input.uris), client=client
        )

        # proper error handling

        if data is None:
            return AddItemsToPlaylistPayload(
                code=500,
                success=False,
                message="Server error",
                playlist=None,
            )

        playlist = await get_playlist.asyncio(
            playlist_id=input.playlist_id, client=client
        )

        assert playlist is not None

        return AddItemsToPlaylistPayload(
            code=200,
            success=True,
            message="Items added to the playlist",
            playlist=Playlist(
                id=strawberry.ID(playlist.id),
                name=playlist.name,
                description=playlist.description,
            ),
        )


schema = strawberry.Schema(Query, mutation=Mutation)
