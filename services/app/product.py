'''Service layer for product module'''
from uuid import uuid4
from sqlalchemy.orm import Session

from domain import (
    models,
    schemas
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


def create_product(
    product: schemas.ProductInput,
    session: Session
) -> models.Product:
    '''Create a product'''
    product.section_id = str(product.section_id)
    product_model = models.Product(
        **product.model_dump()
    )
    product_model.id = str(uuid4())  # type: ignore
    return product_repository.create_product(
        product=product_model,
        session=session
    )
