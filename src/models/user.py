from sqlalchemy import Column, Integer, String, Enum
from ..database import Base
import enum

class UserType(enum.Enum):
    ATTENDANT = "attendant"  # Atendente
    WAITER = "waiter"      # Garçom
    MANAGER = "manager"    # Gerente

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    user_type = Column(Enum(UserType))