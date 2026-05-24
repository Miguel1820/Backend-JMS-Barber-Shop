from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
import enum

class UserRole(str, enum.Enum):
    CLIENTE = "cliente"
    BARBERO = "barbero"
    ADMINISTRADOR = "administrador"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    nombre = Column(String)
    hashed_password = Column(String)
    role = Column(Enum(UserRole), default=UserRole.CLIENTE)
    activo = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Servicio(Base):
    __tablename__ = "servicios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String)
    precio = Column(Float)
    duracion_minutos = Column(Integer)
    activo = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Barbero(Base):
    __tablename__ = "barberos"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    horario_inicio = Column(String)
    horario_fin = Column(String)
    activo = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Turno(Base):
    __tablename__ = "turnos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("users.id"))
    barbero_user_id = Column(Integer, ForeignKey("users.id"))
    servicio_id = Column(Integer, ForeignKey("servicios.id"))
    fecha = Column(DateTime, index=True)
    hora_inicio = Column(String)
    hora_fin = Column(String)
    estado = Column(String, default="pendiente")
    notas = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
