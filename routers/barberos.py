from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Barbero, User
from schemas import Barbero as BarberoSchema, BarberoCreate
from typing import List

router = APIRouter(prefix="/api/barberos", tags=["barberos"])

@router.get("/", response_model=List[BarberoSchema])
def obtener_barberos(db: Session = Depends(get_db)):
    barberos = db.query(Barbero).filter(Barbero.activo == True).all()
    return barberos

@router.post("/", response_model=BarberoSchema)
def crear_barbero(barbero: BarberoCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == barbero.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db_barbero = Barbero(**barbero.dict())
    db.add(db_barbero)
    db.commit()
    db.refresh(db_barbero)
    return db_barbero

@router.get("/{barbero_id}", response_model=BarberoSchema)
def obtener_barbero(barbero_id: int, db: Session = Depends(get_db)):
    barbero = db.query(Barbero).filter(Barbero.id == barbero_id).first()
    if not barbero:
        raise HTTPException(status_code=404, detail="Barbero no encontrado")
    return barbero

@router.put("/{barbero_id}", response_model=BarberoSchema)
def actualizar_barbero(barbero_id: int, barbero: BarberoCreate, db: Session = Depends(get_db)):
    db_barbero = db.query(Barbero).filter(Barbero.id == barbero_id).first()
    if not db_barbero:
        raise HTTPException(status_code=404, detail="Barbero no encontrado")

    for key, value in barbero.dict().items():
        setattr(db_barbero, key, value)

    db.commit()
    db.refresh(db_barbero)
    return db_barbero

@router.delete("/{barbero_id}")
def eliminar_barbero(barbero_id: int, db: Session = Depends(get_db)):
    barbero = db.query(Barbero).filter(Barbero.id == barbero_id).first()
    if not barbero:
        raise HTTPException(status_code=404, detail="Barbero no encontrado")

    barbero.activo = False
    db.commit()
    return {"message": "Barbero desactivado"}
