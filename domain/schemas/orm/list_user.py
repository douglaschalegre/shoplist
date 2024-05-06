"""ORM schema for ListUser sqlalchemy model"""

from datetime import datetime
from uuid import uuid4
from pydantic import Field
from domain.schemas.generic import TableSchema


class ListUserEdit(TableSchema):
    """Edit ListUser schema"""


class ListUserInput(ListUserEdit):
    """Input ListUser schema"""

    list_id: str = Field(title='List UUID', examples=[str(uuid4())])
    users_ids: list[str] = Field(title='Users UUID', examples=[[str(uuid4())]])


class ListUserLite(ListUserInput):
    """Lite ListUser schema"""

    id: str = Field(title='UUID')
    created_at: datetime = Field(title='ListUser creation datetime in UTC 0')


class ListUserBase(ListUserLite):
    """Base ListUser schema"""

    data: dict = Field(default=None, title='ListUser data')
