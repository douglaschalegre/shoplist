"""Model for section"""

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
from .generic import GenericBase


class Section(GenericBase):
    """Section model"""

    __tablename__ = 'section'

    id = Column('sect_cd_section', String(36), primary_key=True)
    name = Column('sect_nm_name', String, nullable=False)
    created_at = Column('sect_df_created_at', DateTime, server_default=text('NOW()'))

    products = relationship('Product', back_populates='section')
