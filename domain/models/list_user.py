'''Model for listuser'''
from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
from .generic import GenericBase


class ListUser(GenericBase):
    '''ListUser model'''
    __tablename__ = 'list_user'

    id = Column('lius_cd_list_user', String(36),
                primary_key=True)
    created_at = Column('lius_df_created_at', DateTime,
                        server_default=text('NOW()'))

    user_id = Column('user_cd_user', String(36))
    list_id = Column('list_cd_list', String(36))
    users = relationship('User', backref='lists')
    lists = relationship('List', backref='users')
