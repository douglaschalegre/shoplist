"""Model for product"""

from sqlalchemy import Column, DateTime, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text, functions
from .generic import GenericBase


class Product(GenericBase):
    """Product model"""

    __tablename__ = 'product'

    id = Column('prod_cd_product', String(36), primary_key=True)
    name = Column('prod_nm_name', String, nullable=False)
    price = Column('prod_vl_price', Float, nullable=False)
    image_url = Column('prod_tx_image_url', String, nullable=True)
    barcode = Column('prod_cd_barcode', String, nullable=False)
    checked = Column('prod_bl_checked', String, nullable=False)
    created_at = Column('prod_df_created_at', DateTime, server_default=text('NOW()'))
    updated_at = Column(
        'prod_df_updated_at', DateTime, server_default=text('NOW()'), onupdate=functions.now()
    )

    section_id = Column('sect_cd_section', ForeignKey('section.sect_cd_section'))

    section = relationship('Section', back_populates='products')
    shopping_lists = relationship('ListProduct', back_populates='product')
