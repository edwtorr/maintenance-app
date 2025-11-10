# Gestión de Averías Industriales

Aplicación web para la gestión de averías en líneas de producción industrial con integración de IA para sugerencias de soluciones.

## Stack Tecnológico

- **Frontend**: Astro + React + Tailwind CSS
- **Backend**: FastAPI (Python)
- **Base de datos**: PostgreSQL
- **Autenticación**: JWT
- **IA**: Anthropic Claude API

## Estructura del Proyecto

```
maintenance-app/
├── frontend/          # Aplicación Astro
├── backend/           # API FastAPI
└── docker-compose.yml # PostgreSQL
```

## Requisitos Previos

- Node.js 18+ y npm
- Python 3.11+
- Docker y Docker Compose
- API Key de Anthropic Claude

## Instalación

### 1. Clonar el repositorio

```bash
git clone <repository-url>
cd maintenance-app
```

### 2. Configurar Base de Datos

```bash
# Iniciar PostgreSQL con Docker
docker-compose up -d

# Verificar que PostgreSQL está corriendo
docker-compose ps
```

### 3. Configurar Backend

```bash
cd backend

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Copiar y configurar variables de entorno
cp .env.example .env
# Editar .env con tus configuraciones

# Ejecutar migraciones
alembic upgrade head

# Iniciar servidor de desarrollo
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Configurar Frontend

```bash
cd frontend

# Instalar dependencias
npm install

# Copiar y configurar variables de entorno
cp .env.example .env
# Editar .env con tus configuraciones

# Iniciar servidor de desarrollo
npm run dev
```

## Acceso a la Aplicación

- **Frontend**: http://localhost:3000 o http://localhost:4321
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/api/docs
- **pgAdmin**: http://localhost:5050 (admin@maintenance.local / admin)

## Modelo de Datos

### Tablas Principales

- **Users**: Usuarios con roles y suscripciones
- **ProductionLines**: Líneas de producción (L16, L20, L33)
- **Machines**: Máquinas por línea
- **Failures**: Histórico de averías
- **Solutions**: Soluciones aplicadas
- **Manuals**: Documentación técnica
- **KPIs**: Métricas calculadas

## Comandos Útiles

### Backend

```bash
# Crear nueva migración
alembic revision --autogenerate -m "descripcion"

# Aplicar migraciones
alembic upgrade head

# Revertir última migración
alembic downgrade -1

# Ver estado de migraciones
alembic current
```

### Frontend

```bash
# Desarrollo
npm run dev

# Build para producción
npm run build

# Preview de producción
npm run preview
```

### Docker

```bash
# Iniciar servicios
docker-compose up -d

# Detener servicios
docker-compose down

# Ver logs
docker-compose logs -f

# Reiniciar servicios
docker-compose restart
```

## Desarrollo

Esta es la Fase 1: Configuración Base. Las siguientes fases incluirán:

- Fase 2: Autenticación y gestión de usuarios
- Fase 3: CRUD de líneas, máquinas y averías
- Fase 4: Integración de IA con Claude
- Fase 5: Dashboard y KPIs
- Fase 6: Testing y optimización

## Licencia

Privado - Todos los derechos reservados
