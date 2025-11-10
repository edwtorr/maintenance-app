# 🚀 Inicio Rápido

Esta guía te ayudará a poner en marcha el proyecto en menos de 5 minutos.

## Requisitos Previos

Asegúrate de tener instalado:
- ✅ Node.js 18+ y npm
- ✅ Python 3.11+
- ✅ Docker Desktop (para Windows)

## Opción 1: Setup Automático (Recomendado)

### Windows

```batch
setup-project.bat
```

Este script:
1. Inicia PostgreSQL con Docker
2. Configura el backend (entorno virtual, dependencias, migraciones)
3. Configura el frontend (dependencias de npm)
4. Muestra las URLs de acceso

## Opción 2: Setup Manual

### 1. Base de Datos

```bash
# Iniciar PostgreSQL
docker-compose up -d

# Verificar estado
docker-compose ps
```

### 2. Backend

```bash
cd backend

# Crear entorno virtual
python -m venv venv

# Activar (Windows)
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar .env
copy .env.example .env
# Editar .env con tus configuraciones

# Aplicar migraciones
alembic upgrade head

# Iniciar servidor
uvicorn app.main:app --reload
```

### 3. Frontend

```bash
cd frontend

# Instalar dependencias
npm install

# Configurar .env
copy .env.example .env

# Iniciar servidor de desarrollo
npm run dev
```

## Iniciar Servicios

Una vez configurado, usa estos scripts para iniciar:

```batch
# Backend
start-backend.bat

# Frontend (en otra terminal)
start-frontend.bat
```

## URLs de Acceso

| Servicio | URL | Credenciales |
|----------|-----|--------------|
| Frontend | http://localhost:4321 | - |
| Backend API | http://localhost:8000 | - |
| API Docs (Swagger) | http://localhost:8000/api/docs | - |
| pgAdmin | http://localhost:5050 | admin@maintenance.local / admin |

## Verificación

### Backend
Visita: http://localhost:8000/health

Deberías ver:
```json
{"status": "healthy"}
```

### Frontend
Visita: http://localhost:4321

Deberías ver la página de bienvenida con el checklist de Fase 1.

## Próximos Pasos

1. ✅ Verifica que la interfaz se vea correctamente
2. ✅ Prueba el cambio de tema (claro/oscuro)
3. ✅ Revisa la documentación de la API en /api/docs
4. ✅ Continúa con la Fase 2 (Autenticación)

## Problemas Comunes

### Puerto 5432 ya en uso
PostgreSQL ya está corriendo. Detén la instancia existente o cambia el puerto en docker-compose.yml

### Error al importar módulos en Python
Asegúrate de estar en el entorno virtual activado: `venv\Scripts\activate`

### npm install falla
Borra node_modules y package-lock.json, luego ejecuta `npm install` de nuevo

### Base de datos no conecta
Verifica que Docker Desktop esté corriendo y que PostgreSQL esté iniciado: `docker-compose ps`

## Ayuda

Si encuentras algún problema, revisa:
- README.md principal
- frontend/README.md
- backend/README.md

O abre un issue en el repositorio.
