'''Repository layer for user module'''
from sqlalchemy.orm import Session

from domain import (
    models
)


def get_users(
    session: Session
) -> list[models.User]:
    '''Get all users'''
    query = session.query(models.User).all()
    return query


def create_user(
    user: models.User,
    session: Session
) -> models.User:
    '''Create a user'''
    session.add(user)
    session.flush()

    return user
