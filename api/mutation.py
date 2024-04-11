import strawberry
from mock_spotify_rest_api_client.api.playlists import (
    add_tracks_to_playlist,
    get_playlist,
)
from .types.add_items_to_playlist_input import AddItemsToPlaylistInput
from .types.add_items_to_playlist_payload import AddItemsToPlaylistPayload
from .types.playlist import Playlist


@strawberry.type
class Mutation:
    @strawberry.mutation(description="Add one or more items to a user's playlist.")
    async def add_items_to_playlist(
        self, info: strawberry.Info, input: AddItemsToPlaylistInput
    ) -> AddItemsToPlaylistPayload:
        client = info.context["spotify_client"]

        try:
            await add_tracks_to_playlist.asyncio(
                playlist_id=input.playlist_id, uris=",".join(input.uris), client=client
            )

            data = await get_playlist.asyncio(
                playlist_id=input.playlist_id, client=client
            )

            playlist = Playlist(
                id=data.id, name=data.name, description=data.description
            )

            return AddItemsToPlaylistPayload(
                code=200,
                success=True,
                message="Successfully added items to playlist.",
                playlist=playlist,
            )
        except Exception as e:
            return AddItemsToPlaylistPayload(
                code=500,
                success=False,
                message=str(e),
                playlist=None,
            )
