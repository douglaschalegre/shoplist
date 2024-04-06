'''Model for product'''
from sqlalchemy import Column, DateTime, String, Float
from sqlalchemy.sql import text
from .generic import GenericBase


class Product(GenericBase):
    '''Product model'''
    __tablename__ = 'product'

    id = Column('prod_cd_product', String(36),
                primary_key=True)
    name = Column('prod_nm_name', String, nullable=False)
    price = Column('prod_vl_price', Float, nullable=False)
    image_url = Column('prod_tx_image_url', String, nullable=True)
    created_at = Column('prod_df_created_at', DateTime,
                        server_default=text('NOW()'))
