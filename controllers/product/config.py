'''Tags description to Product API'''
from fastapi import APIRouter

PRODUCT = dict(
    name='Product',
    description='API to manage products.'
)

tags = [
    PRODUCT,
]

router = APIRouter()
