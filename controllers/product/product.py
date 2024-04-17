'''Controllers for the product module'''
from uuid import UUID
from fastapi import Depends, Path, Body
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


@router.patch(
    path='/product/{product_id}',
    summary='Update a product',
    tags=[PRODUCT['name']],
    response_model=schemas.Product
)
def update_product(
    product_id: UUID = Path(description='Product ID'),
    product_edit: schemas.ProductEdit = Body(
        description='Product data to update'),
    session: Session = Depends(get_session)
) -> models.Product:
    '''Update a product'''
    return product_service.update_product(
        product_id=product_id,
        product_edit=product_edit,
        session=session
    )
