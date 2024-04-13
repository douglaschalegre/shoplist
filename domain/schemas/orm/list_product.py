'''ORM schema for ListProduct sqlalchemy model'''
from datetime import datetime
from uuid import uuid4
from pydantic import Field
from domain.schemas.generic import TableSchema


class ListProductEdit(TableSchema):
    '''Edit ListProduct schema'''
    quantity: int = Field(title='Product quantity', examples=[1])


class ListProductInput(ListProductEdit):
    '''Input ListProduct schema'''
    list_id: str = Field(title='List UUID', examples=[str(uuid4())])
    product_id: str = Field(title='Product UUID', examples=[str(uuid4())])


class ListProductLite(ListProductInput):
    '''Lite ListProduct schema'''
    id: str = Field(title='UUID')
    created_at: datetime = Field(
        title='ListProduct creation datetime in UTC 0')
    updated_at: datetime = Field(
        title='ListProduct updated datetime in UTC 0')


class ListProductBase(ListProductLite):
    '''Base ListProduct schema'''
    data: dict = Field(default=None, title='ListProduct data')
