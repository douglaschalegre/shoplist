'''ORM schema for User sqlalchemy model'''
from datetime import datetime
from pydantic import Field
from domain.schemas.generic import TableSchema


class UserEdit(TableSchema):
    '''Edit User schema'''
    name: str = Field(title='User name')
    username: str = Field(title='User username')
    password: str = Field(title='User password')


class UserInput(UserEdit):
    '''Input User schema'''


class UserLite(UserInput):
    '''Lite User schema'''
    id: str = Field(title='UUID')
    created_at: datetime = Field(title='User creation datetime in UTC 0')
    updated_at: datetime = Field(title='User update datetime in UTC 0')


class UserBase(UserLite):
    '''Base User schema'''
    data: dict = Field(default=None, title='User data')
