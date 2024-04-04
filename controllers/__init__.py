"""Creation of controller list"""

from . import health
from . import product

routes = [
    product.router,

    health.router,  # health route must be the last one!
]
tags = [
    *product.tags,
    *health.tags,  # health tag must be the last one!
]
