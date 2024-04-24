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

def get_section_by_id(
    section_id: str,
    session: Session
) -> models.Section:
    '''Get a section by id'''
    query = session.query(models.Section).filter(
        models.Section.id == section_id
    ).first()
    return query

def create_section(
    section: models.Section,
    session: Session
) -> models.Section:
    '''Create a section'''
    session.add(section)
    session.flush()

    return section
