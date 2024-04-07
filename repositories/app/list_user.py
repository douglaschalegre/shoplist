'''Repository layer for list module'''
from sqlalchemy.orm import Session

from domain import (
    models
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
