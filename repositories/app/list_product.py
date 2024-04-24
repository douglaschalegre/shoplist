'''Repository layer for list module'''
from sqlalchemy.orm import Session

from domain import (
    models,
    errors
)

from repositories.app import (
    list as list_repository
)


def create_list_product(
    list_product: models.ListProduct,
    session: Session
) -> models.ListProduct:
    '''Create a list product'''
    session.add(list_product)
    session.flush()

    return list_product

def create_list_products(
    list_id: str,
    list_products: list[models.ListProduct],
    session: Session
) -> list[models.ListProduct]:
    '''Create a list of list products'''
    list_repository.get_list_by_id(list_id, session)
    
    session.add_all(list_products)
    session.flush()

    return list_products

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
