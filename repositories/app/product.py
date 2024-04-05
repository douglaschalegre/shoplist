'''Repository layer for product module'''
from sqlalchemy.orm import Session

from domain import (
    models
)


def get_products(
    session: Session
) -> list[models.Product]:
    '''Get all products'''
    query = session.query(models.Product).all()
    return query


def create_product(
    product: models.Product,
    session: Session
) -> models.Product:
    '''Create a product'''
    session.add(product)
    session.flush()

    return product
