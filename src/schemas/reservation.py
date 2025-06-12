from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class ReservationStatus(str, Enum):
    ACTIVE = "active"
    CANCELLED = "cancelled"
    COMPLETED = "completed"

class ReservationBase(BaseModel):
    date: datetime
    table_id: int
    customer_name: str
    number_of_people: int

class ReservationCreate(ReservationBase):
    pass

class ReservationUpdate(BaseModel):
    status: ReservationStatus

class Reservation(ReservationBase):
    id: int
    status: ReservationStatus
    created_by: int
    confirmed_by: int | None = None

    class Config:
        from_attributes = True