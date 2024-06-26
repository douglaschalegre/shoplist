"""Service layer for list module"""

from uuid import UUID, uuid4
from sqlalchemy.orm import Session

from domain import models, schemas
from repositories.app import list as list_repository, list_product as lp_repository


def get_lists(session: Session) -> list[models.List]:
    """Get all lists"""
    return list_repository.get_lists(session=session)


def get_list_by_id(list_id: UUID, session: Session) -> models.List:
    """Get a list by ID"""
    return list_repository.get_list_by_id(list_id=str(list_id), session=session)


def create_list(shopping_list: schemas.ListInput, session: Session) -> models.List:
    """Create a list"""
    list_model = models.List(
        id=str(uuid4()),  # type: ignore
        **shopping_list.model_dump(),
    )
    return list_repository.create_list(shopping_list=list_model, session=session)


def add_product_to_list(
    list_product_input: schemas.ListProductInput, session: Session
) -> models.List:
    """Add a product to a list"""
    list_product_model = models.ListProduct(
        id=str(uuid4()),  # type: ignore
        **list_product_input.model_dump(),
    )

    created_list_product = lp_repository.create_list_product(
        list_product=list_product_model, session=session
    )
    return created_list_product.shopping_list


def add_products_to_list(
    list_id: UUID, list_products_input: list[schemas.ListProductInput], session: Session
) -> models.List:
    """Add products to a list"""
    list_products = [
        models.ListProduct(
            id=str(uuid4()),  # type: ignore
            **list_product_input.model_dump(),
        )
        for list_product_input in list_products_input
    ]

    created_list_products = lp_repository.create_list_products(
        list_id=str(list_id), list_products=list_products, session=session
    )

    return created_list_products[0].shopping_list


def update_product_in_list(
    list_id: UUID, product_id: UUID, list_product_edit: schemas.ListProductEdit, session: Session
) -> models.ListProduct:
    """Update a product in a list"""
    return lp_repository.update_list_product(
        list_id=str(list_id),
        product_id=str(product_id),
        quantity=list_product_edit.quantity,
        session=session,
    )


def delete_list(list_id: UUID, session: Session) -> models.List:
    """Delete a list"""
    return list_repository.delete_list(list_id=str(list_id), session=session)


def delete_product_from_list(list_id: UUID, product_id: UUID, session: Session) -> models.List:
    """Delete a product from a list"""
    list_product = lp_repository.delete_list_product(
        list_id=str(list_id), product_id=str(product_id), session=session
    )
    return list_product.shopping_list
