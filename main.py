from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from api.schema import schema

app = FastAPI()

graphql_router = GraphQLRouter(schema, path="/", graphql_ide="apollo-sandbox")

app.include_router(graphql_router)
