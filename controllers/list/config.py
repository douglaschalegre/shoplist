'''Tags description to LIST API'''
from fastapi import APIRouter

LIST = dict(
    name='List',
    description='API to manage lists.'
)

LIST_USER = dict(
    name='List/user',
    description='API to manage users of a list.'
)

tags = [
    LIST,
    LIST_USER
]

router = APIRouter()
