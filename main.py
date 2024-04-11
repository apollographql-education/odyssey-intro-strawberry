from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

app = FastAPI()

graphql_router = GraphQLRouter(..., path="/", graphql_ide="apollo-sandbox")

app.include_router(graphql_router)
