"""ListProduct schema"""

from domain.schemas.orm import ListProductBase, ListBase, ProductBase


class ListProduct(ListProductBase):
    """ListProduct schema"""

    product: ProductBase
    shopping_list: ListBase


class ListOutput(ListProductBase):
    """ListProduct schema"""

    product: ProductBase
