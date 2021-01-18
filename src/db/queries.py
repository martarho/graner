from src.db.db import session
from src.db.schemas import AreaSchema, PlantSchema, PhaseSchema
from src.db.models import Area, Plant, Phase
from loguru import logger


def apply_schema(func):
    """Apply schema and return a json object"""

    def decorator(self, **args):
        result = func(self, **args)
        logger.info(result)
        json = [self.schema.dump(i) for i in result]
        logger.info(json)
        return json

    return decorator


class BaseQuery:
    @apply_schema
    def get_all(self):
        result = (
            session.query(self.model)
            .filter(Area.deleted == False)
            .filter(Plant.deleted == False)
            .filter(Phase.deleted == False)
            .all()
        )
        return result

    @apply_schema
    def get_by_id(self, table_id: int):
        result = (
            session.query(self.model)
            .filter(self.model.id == table_id)
            .filter(Area.deleted == False)
            .filter(Plant.deleted == False)
            .filter(Phase.deleted == False)
            .first()
        )
        return [result]

    @apply_schema
    def get_by_name(self, name: str):
        result = (
            session.query(self.model)
            .filter(self.model.name == name)
            .filter(Area.deleted == False)
            .filter(Plant.deleted == False)
            .filter(Phase.deleted == False)
            .first()
        )
        return [result]

    @apply_schema
    def update_table(self, table_id: int, fields: dict):
        query = session.query(self.model).filter(self.model.id == table_id).first()
        for key, value in fields.items():
            query.update({key: value})
        session.commit()
        return [query]


#
# Query class
#
class Areas(BaseQuery):
    def __init__(self):
        self.schema = AreaSchema()
        self.model = Area


class Plants(BaseQuery):
    def __init__(self):
        self.schema = PlantSchema()
        self.model = Plant


class Phases(BaseQuery):
    def __init__(self):
        self.schema = PhaseSchema()
        self.model = Phase
