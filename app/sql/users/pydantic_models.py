"""Users Pydantic models

The module defines the Pydantic models of users entities
"""

from pydantic import BaseModel
from pydantic import Extra
from pydantic import constr


class UserBase(BaseModel):
    """Base model

    Used for creating and reading users
    All other models inherit from it
    """
    first_name: str
    last_name: str

    class Config:
        extra = Extra.forbid


class UserCreate(UserBase):
    """Model for creating a user
    """
    first_name: constr(min_length=1)
    last_name: constr(min_length=1)

    class Config:
        extra = Extra.forbid


class User(UserBase):
    """Model for reading users
    """
    uuid: str
    id: str

    class Config:
        orm_mode = True
        extra = Extra.forbid


class UserUpdate(BaseModel):
    """Model for updating a user
    """
    first_name: constr(min_length=1) = None
    last_name: constr(min_length=1) = None

    class Config:
        extra = Extra.forbid
