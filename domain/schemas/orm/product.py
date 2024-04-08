'''ORM schema for Product sqlalchemy model'''
from datetime import datetime
from uuid import uuid4
from pydantic import Field
from domain.schemas.generic import TableSchema


class ProductEdit(TableSchema):
    '''Edit Product schema'''
    image_url: str | None = Field(default=None, title='Product image URL')
    barcode: str | None = Field(default=None, title='Product barcode')
    price: float = Field(title='Product price')
    name: str = Field(title='Product name',
                      examples=[uuid4()])
    section_id: str = Field(title='Section UUID of the product',
                            examples=[uuid4()])


class ProductInput(ProductEdit):
    '''Input Product schema'''


class ProductLite(ProductInput):
    '''Lite Product schema'''
    id: str = Field(title='UUID')
    created_at: datetime = Field(title='Product creation datetime in UTC 0')
    updated_at: datetime = Field(title='Product update datetime in UTC 0')


class ProductBase(ProductLite):
    '''Base Product schema'''
    data: dict = Field(default=None, title='Product data')
