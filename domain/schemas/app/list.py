'''List schema'''

from domain.schemas.app.list_product import ListOutput
from domain.schemas.app.list_user import ListUser
from domain.schemas.orm import (
    ListBase
)


class List(ListBase):
    '''List schema'''
    users: list[ListUser]
    products: list[ListOutput]
