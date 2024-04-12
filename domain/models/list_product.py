'''Model for ListProduct'''
from sqlalchemy import Column, DateTime, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
from .generic import GenericBase


class ListProduct(GenericBase):
    '''Listproduct model'''
    __tablename__ = 'list_product'

    id = Column('lipr_cd_list_product', String(36),
                primary_key=True)
    quantity = Column('lipr_nr_quantity', Numeric)
    created_at = Column('lipr_df_created_at', DateTime,
                        server_default=text('NOW()'))
    updated_at = Column('lipr_df_updated_at', DateTime,
                        server_default=text('NOW()'))

    product_id = Column('prod_cd_product', ForeignKey(
        'product.prod_cd_product'))
    list_id = Column('list_cd_list', ForeignKey('list.list_cd_list'))
    products = relationship('Product', back_populates='lists')
    lists = relationship('List', back_populates='products')
