from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from ..database import Base

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, index=True)
    table_id = Column(Integer, ForeignKey("tables.id"))
    customer_name = Column(String, index=True)
    number_of_people = Column(Integer)
    status = Column(String)  # 'active', 'cancelled', 'completed'
    created_by = Column(Integer, ForeignKey("users.id"))  # ID do atendente
    confirmed_by = Column(Integer, ForeignKey("users.id"), nullable=True)  # ID do garçom
    
    table = relationship("Table", back_populates="reservations")
    attendant = relationship("User", foreign_keys=[created_by])
    waiter = relationship("User", foreign_keys=[confirmed_by])