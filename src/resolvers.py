from tartiflette import Resolver
from tartiflette_asgi import TartifletteApp, GraphiQL
import os
from .db.queries import Areas, Plants, Phases
import pprint as pp
from loguru import logger
import pretty_errors


@Resolver("Query.areas")
async def resolve_all_areas(parent, args, ctx, info):
    return Areas().get_all()


@Resolver("Query.area")
async def resolve_one_area(parent, args, ctx, info):
    area = Areas().get_by_id(args["id"])
    return area


# Mutations
@Resolver("Mutation.updateArea")
async def resolve_mutation_update_area(parent, args, ctx, info):
    pass


# Loading GraphQL schemas
sdl = os.path.dirname(os.path.abspath(__file__)) + "/sdl"

graphiql = GraphiQL(path="/graphiql")

graphql = TartifletteApp(
    sdl=sdl,
    path="/",
    graphiql=graphiql,
    subscriptions=False,
)