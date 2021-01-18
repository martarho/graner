from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import pretty_errors

import json

DeclarativeBase = declarative_base()


class Base(DeclarativeBase):
    __abstract__ = True

    def __repr__(self) -> str:
        items = []
        for key in self.__table__._columns._data.keys():
            val = self.__getattribute__(key)
            items.append(f"{key}={val}")
        key_vals = " ".join(items)
        name = self.__class__.__name__
        return f"<{name}({key_vals})>"

    def update(self, values):
        for k, v in values.items():
            setattr(self, k, v)


class Area(Base):
    __tablename__ = "area"
    id = Column(Integer, primary_key=True)
    plant = relationship("Plant", back_populates="areas", lazy="select")
    name = Column(String(50))
    location = Column(String(100), nullable=True)
    size = Column(String(100), nullable=True)
    area_type = Column(String(100), nullable=True)
    deleted = Column(Boolean, default=False)


class Plant(Base):
    __tablename__ = "plant"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    variety = Column(String(100), nullable=True)
    seed_origin = Column(String(100), nullable=True)
    plant_type = Column(String(100), nullable=True)
    deleted = Column(Boolean, default=False)
    area_id = Column(Integer, ForeignKey("area.id"), nullable=True)
    areas = relationship("Area", back_populates="plant")
    phases = relationship("Phase", back_populates="plants")


class Phase(Base):
    __tablename__ = "phase"
    id = Column(Integer, primary_key=True)
    plant_id = Column(Integer, ForeignKey("plant.id"), nullable=True)
    name = Column(String(100), nullable=True)
    phase_start = Column(String(100), nullable=True)
    phase_end = Column(String(100), nullable=True)
    phase_type = Column(String(100), nullable=True)
    temperature_min = Column(Integer, nullable=True)
    temperature_max = Column(Integer, nullable=True)
    sunlight = Column(String(100), nullable=True)
    deleted = Column(Boolean, default=False)
    plants = relationship("Plant", back_populates="phases")
