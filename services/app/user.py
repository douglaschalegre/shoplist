'''Service layer for user module'''
from uuid import uuid4, UUID
from sqlalchemy.orm import Session
from config import (
    cryptography
)
from domain import (
    models,
    schemas
)
from repositories.app import (
    user as user_repository
)


def get_users(
    session: Session
) -> list[models.User]:
    '''Get all users'''
    return user_repository.get_users(
        session=session
    )

def get_user_by_id(
    user_id: UUID,
    session: Session
) -> models.User:
    '''Get a user by id'''
    return user_repository.get_user_by_id(
        user_id=str(user_id),
        session=session
    
)


def create_user(
    user: schemas.UserInput,
    session: Session
) -> models.User:
    '''Create a user'''
    user.password = cryptography.encrypt(user.password)
    user_model = models.User(
        id=str(uuid4()),  # type: ignore
        **user.model_dump(exclude=None)
    )
    return user_repository.create_user(
        user=user_model,
        session=session
    )


def update_user(
    user_id: UUID,
    user_edit: schemas.UserEdit,
    session: Session
) -> models.User:
    '''Update a user'''
    user_edit.password = cryptography.encrypt(user_edit.password)
    return user_repository.update_user(
        user_id=str(user_id),
        user_edit=user_edit,
        session=session
)
