'''Repository layer for list module'''
from sqlalchemy.orm import Session

from domain import (
    models
)


def create_list_product(
    list_product: models.ListProduct,
    session: Session
) -> models.ListProduct:
    '''Create a list product'''
    session.add(list_product)
    session.flush()

    return list_product
