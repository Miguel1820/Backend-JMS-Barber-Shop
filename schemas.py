from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from enum import Enum

class UserRole(str, Enum):
    CLIENTE = "cliente"
    BARBERO = "barbero"
    ADMINISTRADOR = "administrador"

class UserBase(BaseModel):
    email: EmailStr
    nombre: str
    role: UserRole = UserRole.CLIENTE

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(UserBase):
    id: int
    activo: bool
    created_at: datetime

    class Config:
        from_attributes = True

class ServicioBase(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    duracion_minutos: int

class ServicioCreate(ServicioBase):
    pass

class Servicio(ServicioBase):
    id: int
    activo: bool
    created_at: datetime

    class Config:
        from_attributes = True

class BarberoBase(BaseModel):
    horario_inicio: str
    horario_fin: str

class BarberoCreate(BarberoBase):
    user_id: int

class Barbero(BarberoBase):
    id: int
    user_id: int
    activo: bool
    created_at: datetime

    class Config:
        from_attributes = True

class TurnoBase(BaseModel):
    servicio_id: int
    barbero_id: int
    fecha: datetime
    hora_inicio: str
    hora_fin: str

class TurnoCreate(TurnoBase):
    pass

class Turno(TurnoBase):
    id: int
    cliente_id: int
    estado: str
    notas: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: int
    role: UserRole
