'''ORM schema for List sqlalchemy model'''
from datetime import datetime
from pydantic import Field
from domain.schemas.generic import TableSchema


class ListEdit(TableSchema):
    '''Edit List schema'''
    name: str = Field(title='List name')


class ListInput(ListEdit):
    '''Input List schema'''


class ListLite(ListInput):
    '''Lite List schema'''
    id: str = Field(title='UUID')
    created_at: datetime = Field(title='List creation datetime in UTC 0')
    updated_at: datetime = Field(title='List update datetime in UTC 0')


class ListBase(ListLite):
    '''Base List schema'''
    data: dict = Field(default=None, title='List data')
