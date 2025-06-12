from sqlalchemy import Column, Integer, String
from ..database import Base

class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True, index=True)
    capacity = Column(Integer)
    status = Column(String)  # 'available', 'reserved', 'occupied'