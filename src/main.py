from typing import Optional
from fastapi import FastAPI
import graphene
from starlette.graphql import GraphQLApp
from .resolvers import graphql


def create_app():
    app = FastAPI()
    app.mount("/", graphql)
    app.add_event_handler("startup", graphql.startup)

    return app


app = create_app()