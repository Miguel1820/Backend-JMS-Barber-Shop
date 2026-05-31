# 🏪 JMS Barber Shop - Sistema de Gestión de Turnos (Backend)

> **Versión**: 1.0.0  
> **Última actualización**: 2026-05-31  

![Estado del proyecto](https://img.shields.io/badge/Estado-Final-brightgreen?logo=git)

---

## 📖 Descripción General
Backend del sistema de gestión de turnos para barbería **"JMS Barber Shop"**. Proporciona la API RESTful que permite a los clientes reservar turnos, gestionar servicios y barberos, y administrar el calendario de reservas. Implementado con **FastAPI**, **SQLAlchemy** y **PostgreSQL**.

---

## 👥 Integrantes
- **Miguel Ángel Cortázar Montoya**
- **Juan David Ojeda Díaz**
- **Juan Sebastián Padierna Manco**

---

## ⚙️ Tecnologías Utilizadas
- **FastAPI** - Framework web para APIs
- **SQLAlchemy** - ORM para PostgreSQL
- **PostgreSQL** - Base de datos relacional
- **Python 3.12** - Lenguaje principal
- **Uvicorn** - Servidor ASGI
- **Pydantic** - Validación de esquemas

---

## 🚀 Funcionalidades Implementadas
- 🔐 **Autenticación y autorización** con tokens JWT  
- 📅 **Gestión de turnos** (crear, listar, cancelar, actualizar estado)  
- 👥 **Gestión de usuarios** por rol (cliente, barbero, administrador)  
- 🛠️ **CRUD completo** de servicios y barberos  
- 📊 **Estatus de turnos** (pendiente, confirmado, completado, cancelado)  
- 🔎 **Filtrado avanzado** por cliente, barbero y estado  

---

## 📦 Requisitos de Instalación
1. **Python 3.12+**  
2. **Git**  
3. **Docker** (opcional)  
4. **PostgreSQL** (o usar la configuración local con Docker)  

### Instalación rápida (sin Docker)
```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/JMS-Barber-Shop.git

# Instalar dependencias del backend
cd Backend-JMS-Barber-Shop
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configurar base de datos (Local)
# Crear base de datos en PostgreSQL y actualizar DATABASE_URL en .env
```

---

## ▶️ Pasos para Ejecutar el Proyecto
### Desarrollo local (sin Docker)

```bash
# Activar entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Inicializar la base de datos
python init_db.py

# Correr el servidor de desarrollo
python main.py

# o tambien
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Cuentas de Demostración

```
Admin: admin@jms.com / admin123
Cliente: cliente@jms.com / cliente123
Barberos: juan@jms.com, miguel@jms.com, santiago@jms.com / barbero123
```

Accede a la documentación interactiva:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Con Docker (opcional)
```bash
# Construir y levantar contenedores
docker-compose up --build

# Acceder a la documentación
http://localhost:8000/docs
```

---

## 🌐 Enlace al Despliegue
- **Despliegue en producción**: *[Se conectará mediante despliegue en servidor asignado]*  
  (Actualmente en configuración local)

---

## 📜 Licencia
Esta aplicación está bajo licencia ITM. Puedes usarla, modificarla y distribuirla de acuerdo a los términos de la licencia.

---

## 🙏 Agradecimientos
- A **FastAPI** por facilitar la creación de APIs modernas y documentadas.  
- A **PostgreSQL** por su robustez como motor de base de datos.  
- A la comunidad de **Python** por sus increíbles paquetes y soporte.

---

*¡Gracias por usar y contribuir al proyecto!*
ATT: Proyecto JMS Barber Shop

**Versión**: 1.0.0