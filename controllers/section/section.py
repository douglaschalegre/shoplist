'''Controllers for the section module'''
from fastapi import Depends
from sqlalchemy.orm import Session
from config import get_session
from services.app import (
    section as section_service
)
from domain import (
    schemas,
    models
)
from .config import (
    SECTION, router,
)


@router.get(
    path='/sections',
    summary='Get all sections',
    tags=[SECTION['name']],
    response_model=list[schemas.Section]
)
def get_sections(
    session: Session = Depends(get_session)
) -> list[models.Section]:
    '''Get all sections'''
    return section_service.get_sections(
        session=session
    )


@router.post(
    path='/section',
    summary='Create a section',
    tags=[SECTION['name']],
    response_model=schemas.Section
)
def create_section(
    section: schemas.SectionInput,
    session: Session = Depends(get_session)
) -> models.Section:
    '''Create a section'''
    return section_service.create_section(
        section=section,
        session=session
    )
