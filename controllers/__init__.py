'''Creation of controller list'''

from . import (
    health,
    user,
    list as shopping_list,
    section,
    product,
)

routes = [
    user.router,
    shopping_list.router,
    section.router,
    product.router,

    health.router,  # health route must be the last one!
]
tags = [
    *user.tags,
    *shopping_list.tags,
    *section.tags,
    *product.tags,

    *health.tags,  # health tag must be the last one!
]
