'''User schema'''
from pydantic import Field
from domain.schemas.orm import (
    UserBase
)


class User(UserBase):
    '''User schema'''
    password: str = Field(exclude=True)
