import strawberry


@strawberry.type(
    description="A curated collection of tracks designed for a specific activity or mood."
)
class Playlist:
    id: strawberry.ID = strawberry.field(description="The ID for the playlist.")
    name: str = strawberry.field(description="The name of the playlist.")
    description: str | None = strawberry.field(
        description="Describes the playlist, what to expect and entices the user to listen."
    )
