'''Service layer for section module'''
from uuid import uuid4, UUID
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

def get_section_by_id(
    section_id: UUID,
    session: Session
) -> models.Section:
    '''Get a section by ID'''
    return section_repository.get_section_by_id(
        section_id=str(section_id),
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
