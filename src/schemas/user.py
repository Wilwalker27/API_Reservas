from pydantic import BaseModel, EmailStr
from enum import Enum

class UserType(str, Enum):
    ATTENDANT = "attendant"
    WAITER = "waiter"
    MANAGER = "manager"

class UserBase(BaseModel):
    name: str
    email: EmailStr
    user_type: UserType

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True