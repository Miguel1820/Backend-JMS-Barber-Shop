# Backend - JMS Barber Shop API

API REST desarrollada con FastAPI para el sistema de gestión de turnos de barbería.

## Características

- ✅ Autenticación con JWT
- ✅ Gestión de usuarios con roles (cliente, barbero, admin)
- ✅ API completa para turnos, servicios y barberos
- ✅ Validación con Pydantic
- ✅ ORM con SQLAlchemy
- ✅ Base de datos PostgreSQL
- ✅ CORS configurado

## Instalación

### 1. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno

Copia el archivo `.env.example` a `.env`:

```bash
cp .env.example .env
```

### 4. Inicializar la base de datos

```bash
python init_db.py
```

### 5. Ejecutar el servidor

```bash
python main.py
```

El servidor estará en: `http://localhost:8000`

## Cuentas de Demostración

```
Admin: admin@jms.com / admin123
Cliente: cliente@jms.com / cliente123
Barberos: juan@jms.com, miguel@jms.com, santiago@jms.com / barbero123
```

## Documentación

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

**Versión**: 1.0.0
