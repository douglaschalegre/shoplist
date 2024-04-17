'''List schema'''
from domain.schemas.orm import (
    ListBase,
    ListProductBase,
    ListUserBase
)


class List(ListBase):
    '''List schema'''
    users: list[ListUserBase]
    products: list[ListProductBase]
