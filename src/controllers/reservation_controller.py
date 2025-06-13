from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from ..database import get_db
from ..models import Reservation, Table, User
from ..schemas.reservation import ReservationCreate, Reservation as ReservationSchema, ReservationUpdate

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

@router.delete("/{reservation_id}", response_model=ReservationSchema)
async def cancel_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")
    
    # Atualizar status da reserva
    reservation.status = "cancelled"
    
    # Liberar a mesa
    table = db.query(Table).filter(Table.id == reservation.table_id).first()
    if table:
        table.status = "available"
    
    db.commit()
    db.refresh(reservation)
    return reservation

@router.put("/{reservation_id}/confirm", response_model=ReservationSchema)
async def confirm_reservation(reservation_id: int, waiter_id: int, db: Session = Depends(get_db)):
    reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")
    
    # Verificar se o garçom existe
    waiter = db.query(User).filter(User.id == waiter_id, User.user_type == "waiter").first()
    if not waiter:
        raise HTTPException(status_code=400, detail="Garçom não encontrado")
    
    # Atualizar status da reserva
    reservation.status = "completed"
    reservation.confirmed_by = waiter_id
    
    # Atualizar status da mesa
    table = db.query(Table).filter(Table.id == reservation.table_id).first()
    if table:
        table.status = "occupied"
    
    db.commit()
    db.refresh(reservation)
    return reservation

@router.get("/reports/by-period", response_model=List[ReservationSchema])
async def get_reservations_by_period(start_date: datetime, end_date: datetime, db: Session = Depends(get_db)):
    reservations = db.query(Reservation).filter(
        Reservation.date >= start_date,
        Reservation.date <= end_date
    ).all()
    return reservations

@router.get("/reports/by-table/{table_id}", response_model=List[ReservationSchema])
async def get_reservations_by_table(table_id: int, db: Session = Depends(get_db)):
    reservations = db.query(Reservation).filter(Reservation.table_id == table_id).all()
    return reservations

@router.get("/reports/by-waiter/{waiter_id}", response_model=List[ReservationSchema])
async def get_reservations_by_waiter(waiter_id: int, db: Session = Depends(get_db)):
    reservations = db.query(Reservation).filter(Reservation.confirmed_by == waiter_id).all()
    return reservations