import strawberry


@strawberry.input
class AddItemsToPlaylistInput:
    playlist_id: strawberry.ID = strawberry.field(description="The ID of the playlist.")
    uris: list[str] = strawberry.field(description="A list of Spotify URIs to add.")
