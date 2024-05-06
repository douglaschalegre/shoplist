"""Service layer for list module"""

from uuid import UUID, uuid4
from sqlalchemy.orm import Session

from domain import models, schemas
from repositories.app import list_user as list_user_repository, list as list_repository


def get_list_users(list_id: UUID, session: Session) -> list[models.ListUser]:
    """Get all user_list"""
    return list_user_repository.get_list_users(list_id=str(list_id), session=session)


def add_users_to_list(
    list_user_input: schemas.ListUserInput, session: Session
) -> list[models.ListUser]:
    """Add a user to a list"""
    # Check if list exists
    existing_list = list_repository.get_list_by_id(list_id=list_user_input.list_id, session=session)

    # Check if user is already in the list
    users_to_add = list_user_input.users_ids
    for user in existing_list.users:
        for user_input_id in list_user_input.users_ids:
            if user.id == user_input_id:
                users_to_add.remove(user_input_id)

    list_user_models: list[models.ListUser] = []
    for user_id in users_to_add:
        list_user = models.ListUser(id=uuid4(), list_id=list_user_input.list_id, user_id=user_id)
        list_user_models.append(list_user)

    return list_user_repository.add_users_to_list(inputs=list_user_models, session=session)


def remove_users_from_list(
    list_id: UUID, users_to_remove: list[str], session: Session
) -> list[models.ListUser]:
    """Remove users from a list"""

    return list_user_repository.remove_users_from_list(
        list_id=str(list_id), users_to_remove=users_to_remove, session=session
    )
