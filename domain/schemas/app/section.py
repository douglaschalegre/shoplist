'''Section schema'''
from domain.schemas.orm import (
    SectionBase,
    ProductLite
)


class Section(SectionBase):
    '''Section schema'''
    products = list[ProductLite]
