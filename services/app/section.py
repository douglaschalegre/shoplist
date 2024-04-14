'''Service layer for section module'''
from uuid import uuid4
from sqlalchemy.orm import Session

from domain import (
    models,
    schemas
)
from repositories.app import (
    section as section_repository
)


def get_sections(
    session: Session
) -> list[models.Section]:
    '''Get all sections'''
    return section_repository.get_sections(
        session=session
    )


def create_section(
    section: schemas.SectionInput,
    session: Session
) -> models.Section:
    '''Create a section'''
    section_model = models.Section(
        id=str(uuid4()),  # type: ignore
        **section.model_dump()
    )
    return section_repository.create_section(
        section=section_model,
        session=session
    )
