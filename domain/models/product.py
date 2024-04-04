'''Model for product'''
from uuid import uuid4
from sqlalchemy import Column, DateTime, String
from sqlalchemy.sql import text
from .generic import GenericBase


class Product(GenericBase):
    '''Product model'''
    __tablename__ = 'product'

    id = Column('prod_cd_product', String(36),
                default=uuid4, primary_key=True)
    created_at = Column('prod_df_created_ats', DateTime,
                        server_default=text('NOW()'))
