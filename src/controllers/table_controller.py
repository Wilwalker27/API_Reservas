from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models import Table
from ..schemas.table import TableCreate, Table as TableSchema

router = APIRouter()

@router.post("/", response_model=TableSchema)
async def create_table(table: TableCreate, db: Session = Depends(get_db)):
    db_table = Table(**table.dict())
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table

@router.get("/", response_model=List[TableSchema])
async def list_tables(db: Session = Depends(get_db)):
    return db.query(Table).all()