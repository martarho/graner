from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from loguru import logger
import pretty_errors


engine = create_engine("sqlite:///graner.db")
Session = sessionmaker(bind=engine)
session = Session()
