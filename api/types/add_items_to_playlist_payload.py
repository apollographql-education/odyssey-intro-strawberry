import strawberry
from .playlist import Playlist


@strawberry.type
class AddItemsToPlaylistPayload:
    code: int = strawberry.field(
        description="Similar to HTTP status code, represents the status of the mutation."
    )
    success: bool = strawberry.field(
        description="Indicates whether the mutation was successful."
    )
    message: str = strawberry.field(description="Human-readable message for the UI.")
    playlist: Playlist | None = strawberry.field(
        description="The playlist that contains the newly added items."
    )
