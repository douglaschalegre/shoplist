'''Module for encrypting and decrypting passwords.'''
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
assert SECRET_KEY
FERNET = Fernet(SECRET_KEY)


def encrypt(password: str) -> str:
    '''Encrypts the given password.'''
    return FERNET.encrypt(password.encode()).decode()


def decrypt(password: str) -> str:
    '''Decrypts the given password.'''
    return FERNET.decrypt(password.encode()).decode()
