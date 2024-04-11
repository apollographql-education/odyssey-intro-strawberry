import strawberry


def get_hello():
    return "Hello world"


@strawberry.type
class Query:
    hello: str = strawberry.field(resolver=get_hello)
