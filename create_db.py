from src.db.db import *
from sqlalchemy_utils import database_exists, create_database
from src.db.models import Area, Plant, Phase
from src.db.schemas import AreaSchema, PlantSchema, PhaseSchema
from loguru import logger
import pretty_errors
import pprint as pp


def validate_database(engine):
    engine = create_engine("sqlite:///graner.db")
    if not database_exists(engine.url):  # Checks for the first time
        create_database(engine.url)  # Create new DB
        logger.info(
            "New Database Created" + str(database_exists(engine.url))
        )  # Verifies if database is there or not.
        Base.metadata.create_all(engine)
        return True
    else:
        logger.info("Database Already Exists")
        return False


def load_data(session):
    session.add(
        Area(
            name="Test",
            location="unknown",
            area_type="Raised bed",
        )
    )
    session.add(
        Plant(
            name="Tomato",
            area_id=1,
            variety="Money maker",
            seed_origin="unknown",
            plant_type="Fruiting crop",
        )
    )
    session.add(
        Plant(
            name="Broccoli",
            area_id=1,
            seed_origin="unknown",
            plant_type="Brassica",
        )
    )
    session.add(Phase(name="Seeding", plant_id=2))
    session.commit()


if __name__ == "__main__":
    val = validate_database(engine)
    if val:
        load_data(session)

    instances = (
        session.query(Area)
        .filter(Area.deleted == False)
        .filter(Plant.deleted == False)
        .filter(Phase.deleted == False)
        .all()
    )
    schema = AreaSchema()
    for i in instances:
        pp.pprint(schema.dump(i))
    schema.dump(instances)
