'''ListUser schema'''
from domain.schemas.orm import (
    ListUserBase,
    ListBase,
    UserBase

)


class ListUser(ListUserBase):
    '''ListUser schema'''
    shopping_lists: ListBase
    user: UserBase


class ListOutput(ListUserBase):
    '''ListUser schema'''
    user: UserBase
