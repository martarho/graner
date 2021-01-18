import pytest
from tests.sqlalchemy_conftest import dbsession, dbengine
from src.db.queries import Areas, Plants

# Areas
def test_get_areas(dbsession):
    areaobj = Areas()
    areas = areaobj.get_all()
    assert type(areas) == list
    assert type(areas[0]) == dict
    assert len(areas) == 1


def test_get_area_by_id(dbsession):
    area = Areas().get_by_id(table_id=1)
    assert type(area) == list
    assert type(area[0]) == dict
    assert area[0]["id"] == 1


def test_get_area_by_name(dbsession):
    areaobj = Areas()
    area = areaobj.get_by_name(name="Test")
    assert type(area) == list
    assert type(area[0]) == dict
    assert area[0]["name"] == "Test"


# Plants class
def test_get_plants(dbsession):
    obj = Plants()
    res = obj.get_all()
    assert type(res) == list
    assert type(res[0]) == dict
    assert len(res) == 2


def test_get_plant_by_id(dbsession):
    obj = Plants()
    res = obj.get_by_id(table_id=1)
    assert type(res) == list
    assert type(res[0]) == dict
    assert res[0]["name"] == "Tomato"


def test_get_plant_by_name(dbsession):
    obj = Plants()
    res = obj.get_by_name(name="Broccoli")
    assert type(res) == list
    assert type(res[0]) == dict
    assert res[0]["name"] == "Broccoli"


def test_update_plant(dbsession):
    obj = Plants()
    res = obj.update_table(
        table_id=1, fields={"variety": "black russian", "seed_origin": "russia"}
    )
    assert type(res) == list
    assert type(res[0]) == dict
    assert res[0]["name"] == "Tomato"
    assert res[0]["variety"] == "black russian"
    res = obj.get_by_id(table_id=1)
    assert type(res) == list
    assert type(res[0]) == dict
    assert res[0]["variety"] == "black russian"