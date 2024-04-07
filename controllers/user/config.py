"""Tags description to User API"""
from fastapi import APIRouter

USER = dict(
    name='User',
    description='API to manage users.'
)

tags = [
    USER,
]

router = APIRouter()
