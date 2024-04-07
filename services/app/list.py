'''Service layer for list module'''
from uuid import uuid4
from sqlalchemy.orm import Session

from domain import (
    models,
    schemas
)
from repositories.app import (
    list as list_repository
)


def get_lists(
    session: Session
) -> list[models.List]:
    '''Get all lists'''
    return list_repository.get_lists(
        session=session
    )


def create_list(
    shopping_list: schemas.ListInput,
    session: Session
) -> models.List:
    '''Create a list'''
    list_model = models.List(
        **shopping_list.model_dump()
    )
    list_model.id = str(uuid4())  # type: ignore
    return list_repository.create_list(
        shopping_list=list_model,
        session=session
    )
