'''Decorators module'''
from functools import wraps
from sqlalchemy.orm import Session
from repositories.app import (
    list_user as lu_repository,
    user as user_repository
)


def verify_user_access_to_list():
    '''Decorator to update the timestamp of a project last update.'''
    def build_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            '''Wrapping function to decorator'''

            # Validate kwargs data
            session: Session = kwargs.get('session', kwargs.get('_session'))
            list_id = kwargs.get('list_id', kwargs.get('_list_id'))
            username = kwargs.get('username', kwargs.get('_username'))
            if not username:
                raise ValueError('No username was provided to request.')

            # Check if user has access to list
            user = user_repository.get_user_from_username(
                username=username,
                session=session
            )
            lu_repository.get_list_user(
                user_id=user.id,
                list_id=list_id,
                session=session
            )

            executed_func = func(*args, **kwargs)

            return executed_func
        return wrapper
    return build_decorator
