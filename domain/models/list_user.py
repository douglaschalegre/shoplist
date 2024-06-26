"""Model for listuser"""

from sqlalchemy import Column, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
from .generic import ALL_DELETE, GenericBase


class ListUser(GenericBase):
    """ListUser model"""

    __tablename__ = 'list_user'

    id = Column('lius_cd_list_user', String(36), primary_key=True)
    created_at = Column('lius_df_created_at', DateTime, server_default=text('NOW()'))

    user_id = Column('user_cd_user', ForeignKey('user.user_cd_user'))
    list_id = Column('list_cd_list', ForeignKey('list.list_cd_list'))
    user = relationship(
        'User', back_populates='shopping_lists', cascade=ALL_DELETE, passive_deletes=True
    )
    shopping_list = relationship(
        'List', back_populates='users', cascade=ALL_DELETE, passive_deletes=True
    )
