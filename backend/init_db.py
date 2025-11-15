"""
Script para inicializar la base de datos
Crea todas las tablas y datos de prueba
"""
from app.core.database import engine, Base
from app.models import user, production_line, machine, failure
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.services.auth_service import AuthService
from datetime import datetime, timedelta

def init_db():
    """Crear todas las tablas"""
    print("🔧 Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas exitosamente")

def create_sample_data():
    """Crear datos de ejemplo para testing"""
    db = SessionLocal()

    try:
        print("\n📦 Creando datos de ejemplo...")

        # Verificar si ya existen datos
        existing_users = db.query(user.User).count()
        if existing_users > 0:
            print("⚠️  Ya existen datos en la base de datos, saltando creación de datos de ejemplo")
            return

        # Crear usuarios de prueba
        print("👤 Creando usuarios...")
        admin = user.User(
            email="admin@maintenance.com",
            hashed_password=AuthService.hash_password("admin123"),
            full_name="Administrador",
            role="admin",
            subscription_tier="enterprise",
            is_active=True
        )

        manager = user.User(
            email="manager@maintenance.com",
            hashed_password=AuthService.hash_password("manager123"),
            full_name="Manager",
            role="manager",
            subscription_tier="pro",
            is_active=True
        )

        technician = user.User(
            email="tech@maintenance.com",
            hashed_password=AuthService.hash_password("tech123"),
            full_name="Técnico",
            role="technician",
            subscription_tier="free",
            is_active=True
        )

        db.add_all([admin, manager, technician])
        db.commit()
        print("✅ Usuarios creados")

        # Crear líneas de producción
        print("🏭 Creando líneas de producción...")
        line_l16 = production_line.ProductionLine(
            name="L16",
            description="Línea de producción L16 - Envasado",
            is_active=True
        )

        line_l20 = production_line.ProductionLine(
            name="L20",
            description="Línea de producción L20 - Etiquetado",
            is_active=True
        )

        line_l33 = production_line.ProductionLine(
            name="L33",
            description="Línea de producción L33 - Empaquetado",
            is_active=True
        )

        db.add_all([line_l16, line_l20, line_l33])
        db.commit()
        print("✅ Líneas de producción creadas")

        # Crear máquinas
        print("⚙️  Creando máquinas...")
        machines_data = [
            # L16
            {"code": "L16-ENV-01", "name": "Envasadora Principal L16", "machine_type": "envasadora",
             "manufacturer": "ACME Industries", "model": "ENV-2000", "production_line_id": line_l16.id},
            {"code": "L16-ETQ-01", "name": "Etiquetadora L16", "machine_type": "etiquetadora",
             "manufacturer": "LabelTech", "model": "LT-500", "production_line_id": line_l16.id},
            {"code": "L16-ENC-01", "name": "Encajadora L16", "machine_type": "encajadora",
             "manufacturer": "PackMaster", "model": "PM-300", "production_line_id": line_l16.id},

            # L20
            {"code": "L20-ETQ-01", "name": "Etiquetadora Principal L20", "machine_type": "etiquetadora",
             "manufacturer": "LabelTech", "model": "LT-600", "production_line_id": line_l20.id},
            {"code": "L20-INS-01", "name": "Inspector L20", "machine_type": "inspector",
             "manufacturer": "QualityVision", "model": "QV-100", "production_line_id": line_l20.id},

            # L33
            {"code": "L33-EMP-01", "name": "Empaquetadora L33", "machine_type": "empaquetadora",
             "manufacturer": "PackMaster", "model": "PM-500", "production_line_id": line_l33.id},
            {"code": "L33-PAL-01", "name": "Paletizadora L33", "machine_type": "paletizadora",
             "manufacturer": "PalletPro", "model": "PP-200", "production_line_id": line_l33.id},
        ]

        machines_list = []
        for m_data in machines_data:
            m = machine.Machine(**m_data)
            machines_list.append(m)

        db.add_all(machines_list)
        db.commit()
        print("✅ Máquinas creadas")

        # Crear algunas averías de ejemplo
        print("🔧 Creando averías de ejemplo...")
        failures_data = [
            {
                "title": "Fallo en motor principal",
                "description": "El motor principal no arranca correctamente. Se escuchan ruidos extraños.",
                "machine_id": machines_list[0].id,
                "reported_by": technician.id,
                "severity": "high",
                "status": "open",
                "reported_at": datetime.utcnow() - timedelta(hours=2)
            },
            {
                "title": "Atasco en cinta transportadora",
                "description": "La cinta se detiene cada 5 minutos aproximadamente.",
                "machine_id": machines_list[1].id,
                "reported_by": technician.id,
                "severity": "medium",
                "status": "in_progress",
                "reported_at": datetime.utcnow() - timedelta(days=1)
            },
            {
                "title": "Error en sensor de llenado",
                "description": "El sensor no detecta correctamente el nivel de llenado.",
                "machine_id": machines_list[2].id,
                "reported_by": technician.id,
                "severity": "critical",
                "status": "resolved",
                "reported_at": datetime.utcnow() - timedelta(days=3),
                "resolved_at": datetime.utcnow() - timedelta(days=2),
                "downtime_minutes": 120
            }
        ]

        for f_data in failures_data:
            f = failure.Failure(**f_data)
            db.add(f)

        db.commit()
        print("✅ Averías creadas")

        print("\n✨ Datos de ejemplo creados exitosamente!")
        print("\n📝 Usuarios de prueba:")
        print("   Admin:      admin@maintenance.com / admin123")
        print("   Manager:    manager@maintenance.com / manager123")
        print("   Technician: tech@maintenance.com / tech123")

    except Exception as e:
        print(f"❌ Error creando datos de ejemplo: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("🚀 Inicializando base de datos...\n")
    init_db()
    create_sample_data()
    print("\n✅ Base de datos lista para usar!")
