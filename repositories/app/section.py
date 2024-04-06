'''Repository layer for section module'''
from sqlalchemy.orm import Session

from domain import (
    models
)


def get_sections(
    session: Session
) -> list[models.Section]:
    '''Get all sections'''
    query = session.query(models.Section).all()
    return query


def create_section(
    section: models.Section,
    session: Session
) -> models.Section:
    '''Create a section'''
    session.add(section)
    session.flush()

    return section
