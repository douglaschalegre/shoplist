'''ListUser schema'''
from domain.schemas.orm import (
    ListUserBase,
    ListBase,
    UserBase

)


class ListUser(ListUserBase):
    '''ListUser schema'''
    shopping_lists: ListBase
    users: UserBase
