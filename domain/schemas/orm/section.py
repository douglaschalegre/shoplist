"""ORM schema for Section sqlalchemy model"""

from datetime import datetime
from pydantic import Field
from domain.schemas.generic import TableSchema


class SectionEdit(TableSchema):
    """Edit Section schema"""

    name: str = Field(title='Section name', examples=['Fruits', 'Vegetables', 'Meat'])


class SectionInput(SectionEdit):
    """Input Section schema"""


class SectionLite(SectionInput):
    """Lite Section schema"""

    id: str = Field(title='UUID')
    created_at: datetime = Field(title='Section creation datetime in UTC 0')


class SectionBase(SectionLite):
    """Base Section schema"""

    data: dict = Field(default=None, title='Section data')
