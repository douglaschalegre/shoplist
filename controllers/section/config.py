"""Tags description to Section API"""
from fastapi import APIRouter

SECTION = dict(
    name='Section',
    description='API to manage sections.'
)

tags = [
    SECTION,
]

router = APIRouter()
