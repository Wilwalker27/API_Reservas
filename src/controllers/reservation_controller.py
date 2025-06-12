from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from ..database import get_db
from ..models import Reservation, Table, User
from ..schemas.reservation import ReservationCreate, Reservation as ReservationSchema

router = APIRouter()

@router.post("/", response_model=ReservationSchema)
async def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    # Verificar se a mesa está disponível
    table = db.query(Table).filter(Table.id == reservation.table_id).first()
    if not table or table.status != "available":
        raise HTTPException(status_code=400, detail="Mesa não disponível")
    
    # Criar a reserva
    db_reservation = Reservation(
        **reservation.dict(),
        status="active"
    )
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    
    # Atualizar status da mesa
    table.status = "reserved"
    db.commit()
    
    return db_reservation