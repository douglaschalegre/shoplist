'''Controllers for the product module'''
from fastapi import Depends
from sqlalchemy.orm import Session
from config import get_session
from services.app import (
    product as product_service
)
from domain import (
    schemas,
    models
)
from .config import (
    PRODUCT, router,
)


@router.get(
    path='/products',
    summary='Get all products',
    tags=[PRODUCT['name']],
    response_model=list[schemas.Product]
)
def get_products(
    session: Session = Depends(get_session)
) -> list[models.Product]:
    '''Get all products'''
    return product_service.get_products(
        session=session
    )


@router.post(
    path='/product',
    summary='Create a product',
    tags=[PRODUCT['name']],
    response_model=schemas.Product
)
def create_product(
    product: schemas.ProductInput,
    session: Session = Depends(get_session)
) -> models.Product:
    '''Create a product'''
    return product_service.create_product(
        product=product,
        session=session
    )
