from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import Turno, User, Servicio, Barbero
from schemas import Turno as TurnoSchema, TurnoCreate
from typing import List

router = APIRouter(prefix="/api/turnos", tags=["turnos"])

@router.post("/", response_model=TurnoSchema)
def crear_turno(turno: TurnoCreate, cliente_id: int, db: Session = Depends(get_db)):
    db_turno = Turno(
        cliente_id=cliente_id,
        barbero_id=turno.barbero_id,
        servicio_id=turno.servicio_id,
        fecha=turno.fecha,
        hora_inicio=turno.hora_inicio,
        hora_fin=turno.hora_fin,
        estado="pendiente"
    )
    db.add(db_turno)
    db.commit()
    db.refresh(db_turno)
    return db_turno

@router.get("/cliente/{cliente_id}", response_model=List[TurnoSchema])
def obtener_turnos_cliente(cliente_id: int, db: Session = Depends(get_db)):
    turnos = db.query(Turno).filter(Turno.cliente_id == cliente_id).all()
    return turnos

@router.get("/barbero/{barbero_user_id}", response_model=List[TurnoSchema])
def obtener_turnos_barbero(barbero_user_id: int, db: Session = Depends(get_db)):
    turnos = db.query(Turno).filter(Turno.barbero_id == barbero_user_id).all()
    return turnos

@router.put("/{turno_id}/estado")
def actualizar_estado_turno(turno_id: int, nuevo_estado: str, db: Session = Depends(get_db)):
    turno = db.query(Turno).filter(Turno.id == turno_id).first()
    if not turno:
        raise HTTPException(status_code=404, detail="Turno no encontrado")

    turno.estado = nuevo_estado
    db.commit()
    db.refresh(turno)
    return turno

@router.delete("/{turno_id}")
def cancelar_turno(turno_id: int, db: Session = Depends(get_db)):
    turno = db.query(Turno).filter(Turno.id == turno_id).first()
    if not turno:
        raise HTTPException(status_code=404, detail="Turno no encontrado")

    turno.estado = "cancelado"
    db.commit()
    return {"message": "Turno cancelado"}
