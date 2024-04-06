"""Informações genéricas para os modelos"""
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from config.database import db

metadata_obj = MetaData(schema=db["name"])
# Base is empty because SQLITE does not require a declarative_base
Base = declarative_base(metadata='')

ALL_DELETE = 'all, delete'


class GenericBase(Base):
    """Base class to build schemas."""
    __abstract__ = True
