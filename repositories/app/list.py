'''Repository layer for list module'''
from sqlalchemy.orm import Session

from domain import (
    models
)


def get_lists(
    session: Session
) -> list[models.List]:
    '''Get all lists'''
    query = session.query(models.List).all()
    return query


def get_list_by_id(
    list_id: str,
    session: Session
) -> models.List:
    '''Get a list by id'''
    query = session.query(models.List).filter(
        models.List.id == list_id
    ).first()
    if not query:
        raise ValueError('List not found')
    return query


def create_list(
    shopping_list: models.List,
    session: Session
) -> models.List:
    '''Create a list'''
    session.add(shopping_list)
    session.flush()

    return shopping_list
