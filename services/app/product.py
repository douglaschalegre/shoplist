'''Service layer for product module'''
from sqlalchemy.orm import Session

from domain import (
    models
)
from repositories.app import (
    product as product_repository
)


def get_products(
    session: Session
) -> list[models.Product]:
    '''Get all products'''
    return product_repository.get_products(
        session=session
    )
