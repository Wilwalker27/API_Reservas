from pydantic import BaseModel
from enum import Enum

class TableStatus(str, Enum):
    AVAILABLE = "available"
    RESERVED = "reserved"
    OCCUPIED = "occupied"

class TableBase(BaseModel):
    number: int
    capacity: int
    status: TableStatus = TableStatus.AVAILABLE

class TableCreate(TableBase):
    pass

class Table(TableBase):
    id: int

    class Config:
        from_attributes = True