# Backend-JMS-Barber-Shop 🚀

## Descripción
Backend para la barbería con FastAPI, SQLAlchemy y soporte para archivos estáticos.

## Instalación
```bash
pip install fastapi uvicorn sqlalchemy
```

## Ejecutar
```bash
uvicorn app.main:app --reload
```

## Endpoints
- GET /appointments - Obtener todas las citas
- POST /appointments - Crear nueva cita
- GET /services - Obtener todos los servicios
- GET /static/{image_id} - Servir imágenes de galería

## Base de datos
Usa SQLite. Se crea automáticamente al iniciar el servidor.

## API Documentation
http://localhost:8000/docs
