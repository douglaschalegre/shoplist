'''Repository layer for list module'''
from sqlalchemy.orm import Session

from domain import (
    models,
    errors
)


def create_list_product(
    list_product: models.ListProduct,
    session: Session
) -> models.ListProduct:
    '''Create a list product'''
    session.add(list_product)
    session.flush()

    return list_product


def get_list_product(
    list_id: str,
    product_id: str,
    session: Session
) -> models.ListProduct:
    '''Get a list product by id'''
    query = session.query(models.ListProduct).filter(
        models.ListProduct.list_id == list_id,
        models.ListProduct.product_id == product_id
    ).first()
    if not query:
        raise errors.ResourceNotFoundError(
            f'ListProduct with list_id {list_id} and product_id {product_id}.')
    return query


def delete_list_product(
    list_id: str,
    product_id: str,
    session: Session
) -> models.ListProduct:
    '''Delete a list product'''
    list_product = get_list_product(list_id, product_id, session)
    session.delete(list_product)
    session.flush()
    return list_product


def update_list_product(
    list_id: str,
    product_id: str,
    quantity: int,
    session: Session
) -> models.ListProduct:
    '''Update a list product'''
    list_product = get_list_product(list_id, product_id, session)
    list_product.quantity = float(quantity)  # type: ignore
    session.flush()
    return list_product
