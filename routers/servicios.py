from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Servicio
from schemas import Servicio as ServicioSchema, ServicioCreate
from typing import List

router = APIRouter(prefix="/api/servicios", tags=["servicios"])

@router.get("/", response_model=List[ServicioSchema])
def obtener_servicios(db: Session = Depends(get_db)):
    servicios = db.query(Servicio).filter(Servicio.activo == True).all()
    return servicios

@router.post("/", response_model=ServicioSchema)
def crear_servicio(servicio: ServicioCreate, db: Session = Depends(get_db)):
    db_servicio = Servicio(**servicio.dict())
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

@router.get("/{servicio_id}", response_model=ServicioSchema)
def obtener_servicio(servicio_id: int, db: Session = Depends(get_db)):
    servicio = db.query(Servicio).filter(Servicio.id == servicio_id).first()
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return servicio

@router.put("/{servicio_id}", response_model=ServicioSchema)
def actualizar_servicio(servicio_id: int, servicio: ServicioCreate, db: Session = Depends(get_db)):
    db_servicio = db.query(Servicio).filter(Servicio.id == servicio_id).first()
    if not db_servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")

    for key, value in servicio.dict().items():
        setattr(db_servicio, key, value)

    db.commit()
    db.refresh(db_servicio)
    return db_servicio

@router.delete("/{servicio_id}")
def eliminar_servicio(servicio_id: int, db: Session = Depends(get_db)):
    servicio = db.query(Servicio).filter(Servicio.id == servicio_id).first()
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")

    servicio.activo = False
    db.commit()
    return {"message": "Servicio eliminado"}
