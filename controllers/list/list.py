'''Controllers for the list module'''
from fastapi import Depends
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


@router.get(
    path='/lists',
    summary='Get all lists',
    tags=[LIST['name']],
    response_model=list[schemas.List]
)
def get_lists(
    session: Session = Depends(get_session)
) -> list[models.List]:
    '''Get all lists'''
    return list_service.get_lists(
        session=session
    )


@router.post(
    path='/list',
    summary='Create a list',
    tags=[LIST['name']],
    response_model=schemas.List
)
def create_list(
    shopping_list: schemas.ListInput,
    session: Session = Depends(get_session)
) -> models.List:
    '''Create a list'''
    return list_service.create_list(
        shopping_list=shopping_list,
        session=session
    )
