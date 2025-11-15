from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Crear engine de SQLAlchemy con configuración condicional
if settings.DATABASE_URL.startswith("sqlite"):
    # SQLite config
    engine = create_engine(
        settings.DATABASE_URL,
        connect_args={"check_same_thread": False},
        echo=False,  # Cambiar a True para debug SQL
    )
else:
    # PostgreSQL config
    engine = create_engine(
        settings.DATABASE_URL,
        pool_pre_ping=True,
        echo=False,
    )

# SessionLocal class para crear sesiones de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class para los modelos
Base = declarative_base()


# Dependency para obtener la sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
