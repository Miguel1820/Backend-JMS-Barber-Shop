from database import SessionLocal, Base, engine
from models import User, Servicio, Barbero, UserRole
from auth import get_password_hash

def init_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # Verificar si ya existen datos
    existing_users = db.query(User).first()
    if existing_users:
        print("Base de datos ya inicializada")
        db.close()
        return

    # Crear usuarios
    admin = User(
        email="admin@jms.com",
        nombre="Administrador",
        hashed_password=get_password_hash("admin123"),
        role=UserRole.ADMINISTRADOR,
        activo=True
    )

    cliente = User(
        email="cliente@jms.com",
        nombre="Cliente Demo",
        hashed_password=get_password_hash("cliente123"),
        role=UserRole.CLIENTE,
        activo=True
    )

    barbero1 = User(
        email="juan@jms.com",
        nombre="Juan Martínez",
        hashed_password=get_password_hash("barbero123"),
        role=UserRole.BARBERO,
        activo=True
    )

    barbero2 = User(
        email="miguel@jms.com",
        nombre="Miguel Sánchez",
        hashed_password=get_password_hash("barbero123"),
        role=UserRole.BARBERO,
        activo=True
    )

    barbero3 = User(
        email="santiago@jms.com",
        nombre="Santiago López",
        hashed_password=get_password_hash("barbero123"),
        role=UserRole.BARBERO,
        activo=True
    )

    db.add_all([admin, cliente, barbero1, barbero2, barbero3])
    db.commit()

    # Crear servicios
    servicio1 = Servicio(
        nombre="Corte de cabello",
        descripcion="Corte clásico",
        precio=15000,
        duracion_minutos=30,
        activo=True
    )

    servicio2 = Servicio(
        nombre="Arreglo de barba",
        descripcion="Arreglo y perfilado de barba",
        precio=10000,
        duracion_minutos=20,
        activo=True
    )

    servicio3 = Servicio(
        nombre="Corte + Barba",
        descripcion="Corte completo con arreglo de barba",
        precio=22000,
        duracion_minutos=50,
        activo=True
    )

    servicio4 = Servicio(
        nombre="Afeitado clásico",
        descripcion="Afeitado con técnica clásica",
        precio=12000,
        duracion_minutos=25,
        activo=True
    )

    db.add_all([servicio1, servicio2, servicio3, servicio4])
    db.commit()

    # Crear registros de barberos
    barbero_record1 = Barbero(
        user_id=barbero1.id,
        horario_inicio="08:00",
        horario_fin="17:00",
        activo=True
    )

    barbero_record2 = Barbero(
        user_id=barbero2.id,
        horario_inicio="09:00",
        horario_fin="18:00",
        activo=True
    )

    barbero_record3 = Barbero(
        user_id=barbero3.id,
        horario_inicio="10:00",
        horario_fin="19:00",
        activo=True
    )

    db.add_all([barbero_record1, barbero_record2, barbero_record3])
    db.commit()

    print("Base de datos inicializada correctamente")
    print("\nCuentas de demostración creadas:")
    print("  Admin: admin@jms.com / admin123")
    print("  Cliente: cliente@jms.com / cliente123")
    print("  Barbero 1: juan@jms.com / barbero123")
    print("  Barbero 2: miguel@jms.com / barbero123")
    print("  Barbero 3: santiago@jms.com / barbero123")
    print("\nBase de datos lista para usar")

    db.close()

if __name__ == "__main__":
    init_db()
