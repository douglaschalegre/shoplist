'''Service layer for user module'''
from uuid import uuid4
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
