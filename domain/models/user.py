"""Model for user"""

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text, functions
from .generic import GenericBase


class User(GenericBase):
    """User model"""

    __tablename__ = 'user'

    id = Column('user_cd_user', String(36), primary_key=True)
    name = Column('user_nm_name', String, nullable=False)
    username = Column('user_tx_username', String, nullable=False)
    password = Column('user_tx_password', String)
    created_at = Column('user_df_created_at', DateTime, server_default=text('NOW()'))
    updated_at = Column(
        'user_df_updated_at', DateTime, server_default=text('NOW()'), onupdate=functions.now()
    )

    shopping_lists = relationship('ListUser', back_populates='user')
