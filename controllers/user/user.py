'''Controllers for the user module'''
from fastapi import Depends
from sqlalchemy.orm import Session
from config import get_session
from services.app import (
    user as user_service
)
from domain import (
    schemas,
    models
)
from .config import (
    USER, router,
)


@router.get(
    path='/users',
    summary='Get all users',
    tags=[USER['name']],
    response_model=list[schemas.User]
)
def get_users(
    session: Session = Depends(get_session)
) -> list[models.User]:
    '''Get all users'''
    return user_service.get_users(
        session=session
    )


@router.post(
    path='/user',
    summary='Create a user',
    tags=[USER['name']],
    response_model=schemas.User
)
def create_user(
    user: schemas.UserInput,
    session: Session = Depends(get_session)
) -> models.User:
    '''Create a user'''
    return user_service.create_user(
        user=user,
        session=session
    )
