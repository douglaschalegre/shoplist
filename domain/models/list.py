"""Model for list"""

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text, functions
from .generic import GenericBase


class List(GenericBase):
    """List model"""

    __tablename__ = 'list'

    id = Column('list_cd_list', String(36), primary_key=True)
    name = Column('list_nm_name', String, nullable=False)
    code = Column('list_cd_code', String, nullable=False, unique=True)
    created_at = Column('list_df_created_at', DateTime, server_default=text('NOW()'))
    updated_at = Column(
        'list_df_updated_at', DateTime, server_default=text('NOW()'), onupdate=functions.now()
    )

    users = relationship('ListUser', back_populates='shopping_list')
    products = relationship('ListProduct', back_populates='shopping_list')
