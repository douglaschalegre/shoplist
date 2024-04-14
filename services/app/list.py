'''Service layer for list module'''
from uuid import UUID, uuid4
from sqlalchemy.orm import Session

from domain import (
    models,
    schemas
)
from repositories.app import (
    list as list_repository,
    list_product as lp_repository
)


def get_lists(
    session: Session
) -> list[models.List]:
    '''Get all lists'''
    return list_repository.get_lists(
        session=session
    )


def get_list_by_id(
    list_id: UUID,
    session: Session
) -> models.List:
    '''Get a list by ID'''
    return list_repository.get_list_by_id(
        list_id=str(list_id),
        session=session
    )


def create_list(
    shopping_list: schemas.ListInput,
    session: Session
) -> models.List:
    '''Create a list'''
    list_model = models.List(
        id=str(uuid4()),  # type: ignore
        **shopping_list.model_dump()
    )
    return list_repository.create_list(
        shopping_list=list_model,
        session=session
    )


def add_product_to_list(
    list_product_input: schemas.ListProductInput,
    session: Session
) -> models.List:
    '''Add a product to a list'''
    list_product_model = models.ListProduct(
        id=str(uuid4()),  # type: ignore
        **list_product_input.model_dump()
    )

    created_list_product = lp_repository.create_list_product(
        list_product=list_product_model,
        session=session
    )
    return created_list_product.shopping_list
