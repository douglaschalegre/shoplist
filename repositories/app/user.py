"""Repository layer for user module"""

from sqlalchemy.orm import Session

from domain import models, schemas

from utils import db_object as utils


def get_users(session: Session) -> list[models.User]:
    """Get all users"""
    query = session.query(models.User).all()
    return query


def get_user_by_id(user_id: str, session: Session) -> models.User:
    """Get a user by id"""
    query = session.query(models.User).filter(models.User.id == user_id).first()

    if not query:
        raise ValueError('User not found')

    return query


def create_user(user: models.User, session: Session) -> models.User:
    """Create a user"""
    session.add(user)
    session.flush()

    return user


def get_user_from_username(username: str, session: Session) -> models.User:
    """Get a user by username"""
    query = session.query(models.User).filter(models.User.username == username).first()
    if not query:
        raise ValueError('User not found')
    return query


def update_user(user_id: str, user_edit: schemas.UserEdit, session: Session) -> models.User:
    """Update a user"""
    user = get_user_by_id(user_id=user_id, session=session)
    updated_user = utils.replace_values(model=user, schema=user_edit)

    session.add(updated_user)
    session.flush()

    return user
