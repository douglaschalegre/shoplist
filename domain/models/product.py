'''Model for product'''
from sqlalchemy import Column, DateTime, String, Float
from sqlalchemy.orm import relationship
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
    barcode = Column('prod_cd_barcode', String, nullable=False)
    created_at = Column('prod_df_created_at', DateTime,
                        server_default=text('NOW()'))

    section_id = Column('sect_cd_section', String(36))
    section = relationship('Section', backref='products')
