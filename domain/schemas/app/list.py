"""List schema"""

from domain.schemas.app.list_product import ListOutput as ListProductOutput
from domain.schemas.app.list_user import ListOutput as ListUserOutput
from domain.schemas.orm import ListBase


class List(ListBase):
    """List schema"""

    users: list[ListUserOutput]
    products: list[ListProductOutput]
