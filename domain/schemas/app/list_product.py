'''ListProduct schema'''
from domain.schemas.orm import (
    ListProductBase,
    ListBase,
    ProductBase
)


class ListProduct(ListProductBase):
    '''ListProduct schema'''
    products: ProductBase
    shopping_list: ListBase


class ListOutput(ListProductBase):
    '''ListProduct schema'''
    products: ProductBase
