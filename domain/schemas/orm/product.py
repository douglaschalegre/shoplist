'''ORM schema for Product sqlalchemy model'''
from datetime import datetime
from uuid import UUID
from pydantic import Field
from domain.schemas.generic import TableSchema


class ProductEdit(TableSchema):
    '''Edit Product schema'''
    image_url: str | None = Field(default=None, title='Product image URL')
    price: float = Field(..., title='Product price')
    name: str = Field(..., title='Product name')


class ProductInput(ProductEdit):
    '''Input Product schema'''


class ProductLite(ProductInput):
    '''Lite Product schema'''
    id: UUID = Field(title='UUID')
    created_at: datetime = Field(title='Product creation datetime in UTC 0')


class ProductBase(ProductLite):
    '''Base Product schema'''
    data: dict = Field(default=None, title='Product data')
