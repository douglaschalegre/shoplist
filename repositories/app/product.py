"""Repository layer for product module"""

from sqlalchemy.orm import Session

from domain import models, schemas
import utils


def get_products(session: Session) -> list[models.Product]:
    """Get all products"""
    query = session.query(models.Product).all()
    return query


def get_product_by_id(product_id: str, session: Session) -> models.Product:
    """Get a product by ID"""
    query = session.query(models.Product).filter(models.Product.id == product_id).first()

    return query


def create_product(product: models.Product, session: Session) -> models.Product:
    """Create a product"""
    session.add(product)
    session.flush()

    return product


def update_product(
    product_id: str, product_edit: schemas.ProductEdit, session: Session
) -> models.Product:
    """Update a product"""
    product = get_product_by_id(product_id=product_id, session=session)

    updated_product = utils.replace_values(model=product, schema=product_edit)

    session.add(updated_product)
    session.flush()

    return product
