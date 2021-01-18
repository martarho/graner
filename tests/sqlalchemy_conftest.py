import pytest
from sqlalchemy import create_engine
from loguru import logger
from src.db.models import Base, Area, Plant, Phase
from sqlalchemy.orm import Session, sessionmaker


@pytest.fixture(scope="session")
def dbengine():
    return create_engine("sqlite://")


def populate(session):
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


@pytest.fixture(scope="session")
def dbsession(dbengine):
    sessionmaker_ = sessionmaker(bind=dbengine)
    session = sessionmaker_()
    Base.metadata.create_all(dbengine)
    populate(session)
    yield session
    session.close()
    Base.metadata.drop_all(dbengine)
