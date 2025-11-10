# Backend - Gestión de Averías API

API REST construida con FastAPI para la gestión de averías industriales.

## Características

- FastAPI con validación automática de datos (Pydantic)
- SQLAlchemy ORM para PostgreSQL
- Autenticación JWT
- Migraciones con Alembic
- Integración con Anthropic Claude API
- CORS configurado

## Estructura

```
backend/
├── app/
│   ├── api/           # Endpoints (próximas fases)
│   ├── core/          # Configuración, seguridad y BD
│   ├── models/        # Modelos SQLAlchemy
│   ├── schemas/       # Schemas Pydantic (próximas fases)
│   ├── services/      # Lógica de negocio (próximas fases)
│   └── main.py        # Aplicación principal
├── alembic/           # Migraciones de base de datos
└── requirements.txt   # Dependencias Python
```

## Modelos de Base de Datos

### User
- Gestión de usuarios con roles y suscripciones
- Roles: admin, technician, operator, viewer
- Tiers: free, basic, premium, enterprise

### ProductionLine
- Líneas de producción (L16, L20, L33, etc.)

### Machine
- Máquinas asociadas a líneas de producción

### Failure
- Histórico de averías
- Estados: open, in_progress, resolved, closed
- Severidad: low, medium, high, critical

### Solution
- Soluciones aplicadas a averías
- Tiempo de resolución
- Indicador de sugerencia por IA

### Manual
- Documentación técnica
- Tipos: maintenance, operation, troubleshooting, safety

### KPI
- Métricas calculadas (MTBF, MTTR, disponibilidad)

## Scripts Disponibles

```bash
# Iniciar servidor de desarrollo
uvicorn app.main:app --reload

# Crear migración
alembic revision --autogenerate -m "descripcion"

# Aplicar migraciones
alembic upgrade head

# Revertir migración
alembic downgrade -1
```

## Variables de Entorno

Ver `.env.example` para configuración completa.

Variables críticas:
- `DATABASE_URL`: Conexión a PostgreSQL
- `SECRET_KEY`: Clave para JWT (cambiar en producción)
- `ANTHROPIC_API_KEY`: API key de Claude

## Endpoints (Fase 1 - Base)

- `GET /`: Información de la API
- `GET /health`: Health check
- `GET /api/docs`: Documentación interactiva (Swagger)
- `GET /api/redoc`: Documentación alternativa (ReDoc)

## Próximos Endpoints (Fase 2+)

- `/api/auth/*`: Autenticación y registro
- `/api/failures/*`: Gestión de averías
- `/api/machines/*`: Gestión de máquinas
- `/api/production-lines/*`: Líneas de producción
- `/api/solutions/*`: Soluciones
- `/api/manuals/*`: Manuales técnicos
- `/api/kpi/*`: Métricas y KPIs
- `/api/ai/*`: Integración con IA

## Seguridad

El módulo `app/core/security.py` incluye:
- Hashing de contraseñas con bcrypt
- Generación y validación de tokens JWT
- Tokens de acceso (30 min) y refresh (7 días)

## Base de Datos

Conexión configurada en `app/core/database.py`:
- Engine SQLAlchemy
- SessionLocal para crear sesiones
- Dependency `get_db()` para FastAPI
