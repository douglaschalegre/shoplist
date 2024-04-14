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


def get_user_from_username(
    username: str,
    session: Session
) -> models.User:
    '''Get a user by username'''
    query = session.query(models.User).filter(
        models.User.username == username
    ).first()
    if not query:
        raise ValueError('User not found')
    return query
