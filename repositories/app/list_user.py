'''Repository layer for list module'''
from sqlalchemy.orm import Session

from domain import (
    models
)
from repositories.app import (
    list as list_repository
)

def get_list_users(
    list_id: str,
    session: Session
) -> list[models.ListUser]:
    '''Get all user_list'''
    query = session.query(models.ListUser).filter(
        models.ListUser.list_id == list_id).all()
    return query


def add_users_to_list(
    inputs: list[models.ListUser],
    session: Session
) -> list[models.ListUser]:
    '''Add a user to a list'''

    session.add_all(inputs)
    session.commit()
    return inputs


def get_list_user(
    list_id: str,
    user_id: str,
    session: Session
) -> models.ListUser:
    '''Get a list user by id'''
    query = session.query(models.ListUser).filter(
        models.ListUser.list_id == list_id,
        models.ListUser.user_id == user_id
    ).first()
    if not query:
        raise ValueError('ListUser not found')
    return query

def remove_users_from_list(
    list_id: str,
    users_to_remove: list[str],
    session: Session
) -> list[models.ListUser]:
    '''Remove users from a list'''
    list_users = get_list_users(
        list_id=list_id,
        session=session
    )
    for user in list_users:
        if user.user_id in users_to_remove:
            session.delete(user)
    session.flush()

    return list_repository.get_list_by_id(
        list_id=list_id,
        session=session
    ).users
    