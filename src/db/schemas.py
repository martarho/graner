from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from src.db.models import Plant, Phase, Area


class PhaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Phase
        include_relationships = True
        load_instance = True


class PlantSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Plant
        include_relationships = True
        load_instance = True

    phases = Nested(PhaseSchema, many=True, exclude=())


class AreaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Area
        include_relationships = True
        load_instance = True

    plant = Nested(PlantSchema, many=True, exclude=())
