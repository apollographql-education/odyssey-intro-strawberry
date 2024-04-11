import strawberry

from .query import Query
from .mutation import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)
