"""Tags description to LIST API"""
from fastapi import APIRouter

LIST = dict(
    name='LIST',
    description='API to manage lists.'
)

LIST_USER = dict(
    name='LIST_USER',
    description='API to manage users of a list.'
)

tags = [
    LIST,
    LIST_USER
]

router = APIRouter()
