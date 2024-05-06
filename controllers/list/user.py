"""Controllers for the list module"""

from uuid import UUID
from fastapi import Depends, Path, Body
from sqlalchemy.orm import Session
from config import get_session
from services.app import list_user as list_user_service
from domain import schemas, models
from .config import (
    LIST_USER,
    router,
)


@router.get(
    path='/list/{list_id}/users',
    summary='Get all users of a list',
    tags=[LIST_USER['name']],
    response_model=list[schemas.List],
)
def get_user_list(
    list_id: UUID = Path(title='UUID of the list'), session: Session = Depends(get_session)
) -> list[models.ListUser]:
    """Get all user_list"""
    return list_user_service.get_list_users(list_id=list_id, session=session)


@router.post(
    path='/list/users',
    summary='Add users to a list',
    tags=[LIST_USER['name']],
    response_model=schemas.ListUser,
)
def add_users_to_list(
    list_user_input: schemas.ListUserInput = Body(
        title='Input for list user', description='Necessary data to add users to a list'
    ),
    session: Session = Depends(get_session),
) -> list[models.ListUser]:
    """Add users to a list"""
    return list_user_service.add_users_to_list(list_user_input=list_user_input, session=session)


@router.patch(
    path='/list/{list_id}/user',
    summary='Remove users from a list',
    tags=[LIST_USER['name']],
    response_model=list[schemas.ListUser],
)
def remove_users_from_list(
    list_id: UUID = Path(description='UUID of the list'),
    users_to_remove: list[str] = Body(description='Necessary data to remove users from a list'),
    session: Session = Depends(get_session),
) -> list[models.ListUser]:
    """Remove users from a list"""
    return list_user_service.remove_users_from_list(
        list_id=list_id, users_to_remove=users_to_remove, session=session
    )
