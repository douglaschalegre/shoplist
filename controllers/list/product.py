'''List endpoints related to products'''
from uuid import UUID
from fastapi import Depends, Body, Path
from sqlalchemy.orm import Session
from config import get_session
from services.app import (
    list as list_service
)
from domain import (
    schemas,
    models
)
from .config import (
    LIST, router,
)

@router.post(
    path='/list/product',
    summary='Add a product to a list',
    tags=[LIST['name']],
    response_model=schemas.List
)
def add_product_to_list(
    list_product_input: schemas.ListProductInput = Body(
        description='Product to add'),
    session: Session = Depends(get_session)
) -> models.List:
    '''Add a product to a list'''
    return list_service.add_product_to_list(
        list_product_input=list_product_input,
        session=session
    )

@router.post(
        path='/list/{list_id}/products',
        summary='Add products to a list',
        tags=[LIST['name']],
        response_model=schemas.List
)
def add_products_to_list(
        list_id: UUID = Path(description='List ID'),
        list_products_input: list[schemas.ListProductInput] = Body(
            description='Products to add'),
        session: Session = Depends(get_session)
) -> models.List:
    '''Add products to a list'''
    return list_service.add_products_to_list(
        list_id=list_id,
        list_products_input=list_products_input,
        session=session
    )

@router.patch(
    path='/list/{list_id}/product/{product_id}',
    summary='Update a list',
    tags=[LIST['name']],
    response_model=schemas.ListProduct
)
def update_product_in_list(
    product_id: UUID = Path(description='Product ID'),
    list_id: UUID = Path(description='List ID'),
    list_product_edit: schemas.ListProductEdit = Body(
        description='Product to update'),
    session: Session = Depends(get_session)
) -> models.ListProduct:
    '''Update a list'''
    return list_service.update_product_in_list(
        list_id=list_id,
        product_id=product_id,
        list_product_edit=list_product_edit,
        session=session
    )

@router.delete(
    path='/list/{list_id}/product/{product_id}',
    summary='Delete a product from a list',
    tags=[LIST['name']],
    response_model=schemas.List
)
def delete_product_from_list(
    product_id: UUID = Path(description='Product ID'),
    list_id: UUID = Path(description='List ID'),
    session: Session = Depends(get_session)
) -> models.List:
    '''Delete a product from a list'''
    return list_service.delete_product_from_list(
        list_id=list_id,
        product_id=product_id,
        session=session
    )