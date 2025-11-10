# Web Gestión de Averías
Necesito crear una aplicación web de gestión de averías industriales con las siguientes especificaciones:

## STACK TECNOLÓGICO
- Frontend: Astro con componentes React para interactividad
- Backend: FastAPI (Python)
- Base de datos: PostgreSQL con SQLAlchemy ORM
- Autenticación: Sistema de suscripción con JWT
- IA: Integración con API de Claude (Anthropic)

## ARQUITECTURA DEL PROYECTO
Crea la estructura base del proyecto con:

maintenance-app/
├── frontend/                 # Aplicación Astro
│   ├── src/
│   │   ├── components/      # Componentes React reutilizables
│   │   ├── layouts/         # Layouts de Astro
│   │   ├── pages/           # Rutas de la aplicación
│   │   ├── styles/          # CSS/Tailwind
│   │   └── utils/           # Utilidades y helpers
│   ├── public/
│   └── astro.config.mjs
│
├── backend/                  # API FastAPI
│   ├── app/
│   │   ├── api/             # Endpoints
│   │   ├── core/            # Configuración y seguridad
│   │   ├── models/          # Modelos SQLAlchemy
│   │   ├── schemas/         # Schemas Pydantic
│   │   ├── services/        # Lógica de negocio
│   │   └── main.py
│   ├── alembic/             # Migraciones de BD
│   └── requirements.txt
│
└── docker-compose.yml        # PostgreSQL + servicios

## FASE 1: CONFIGURACIÓN BASE Y ESTRUCTURA

TAREAS:
1. Inicializar proyecto Astro con configuración para React
2. Configurar Tailwind CSS con diseño similar a Claude/ChatGPT
3. Crear estructura de carpetas del backend FastAPI
4. Configurar PostgreSQL con Docker Compose
5. Setup de variables de entorno (.env.example)
6. Configurar CORS entre frontend y backend
7. Crear archivo de configuración para colores y tema

CONFIGURACIÓN ESPECÍFICA:
- Astro: SSR habilitado para autenticación
- Tailwind: Tema oscuro/claro con paleta similar a Claude
- FastAPI: Estructura modular con blueprints
- PostgreSQL: Esquema inicial con tablas principales

MODELO DE DATOS INICIAL (solo estructura, sin implementar):
- Users (suscripciones y roles)
- ProductionLines (L16, L20, L33, etc.)
- Machines (por línea de producción)
- Failures (histórico de averías)
- Solutions (soluciones aplicadas)
- Manuals (documentación técnica)
- KPIs (métricas calculadas)

NO implementes todavía la lógica de negocio, solo la estructura base y configuración.

## FASE 2: DESARROLLO DEL FRONTEND

Usando la estructura creada en Fase 1, desarrolla la interfaz de usuario:

### DISEÑO GENERAL
Estilo visual similar a Claude.ai:
- Diseño limpio y minimalista
- Sidebar lateral colapsable con navegación
- Header con búsqueda global y perfil de usuario
- Tema claro/oscuro con toggle
- Animaciones suaves y transiciones
- Responsive design (mobile-first)

### COMPONENTES A CREAR

1. **Layout Principal** (`MainLayout.astro`)
   - Header con logo, búsqueda y menú usuario
   - Sidebar navegable con iconos
   - Área de contenido principal
   - Sistema de notificaciones

2. **Sidebar Navigation**
   Secciones:
   - 🏠 Dashboard (KPIs y resumen)
   - 🤖 Asistente IA (chat interface)
   - 📋 Registro de Averías
   - 📊 Visualización de KPIs
   - 📚 Manuales
   - 🗄️ Gestión de Históricos
   - ⚙️ Configuración de Líneas
   - 👤 Perfil y Suscripción

3. **Dashboard** (`pages/index.astro`)
   - Tarjetas de KPIs principales (MTTR, MTBF, disponibilidad)
   - Gráficos con Chart.js o Recharts
   - Lista de averías recientes
   - Estado de líneas de producción

4. **Interfaz de Chat IA** (`components/AIAssistant.tsx`)
   - Diseño idéntico a Claude.ai
   - Input de texto con auto-resize
   - Historial de conversaciones
   - Markdown rendering para respuestas
   - Botones de acción (copiar, regenerar)
   - Sugerencias de prompts

5. **Registro de Averías** (`pages/failures/new.astro`)
   - Formulario multi-paso
   - Selector de línea de producción (dropdown)
   - Selector de máquina (filtrado por línea)
   - Descripción del problema
   - Nivel de urgencia (crítico, alto, medio, bajo)
   - Subida de imágenes/documentos
   - Timestamp automático

6. **Visualización de Históricos** (`pages/history.astro`)
   - Tabla con filtros avanzados
   - Búsqueda por línea, máquina, fecha, tipo
   - Exportar a Excel/PDF
   - Vista detallada de cada avería
   - Timeline visual de eventos

7. **Gestión de Manuales** (`pages/manuals.astro`)
   - Upload de archivos PDF
   - Organización por línea/máquina
   - Visor de PDFs integrado
   - Sistema de tags y búsqueda
   - Control de versiones

8. **Configuración de Líneas** (`pages/config/lines.astro`)
   - CRUD de líneas de producción
   - CRUD de máquinas por línea
   - Asignación de características
   - Vista de árbol jerárquico

### COMPONENTES REUTILIZABLES
- `Button.tsx` (variantes: primary, secondary, danger)
- `Card.tsx` (contenedor estilizado)
- `Modal.tsx` (diálogos y confirmaciones)
- `Table.tsx` (tablas con paginación)
- `Select.tsx` (dropdown personalizado)
- `DatePicker.tsx` (selector de fechas)
- `FileUpload.tsx` (drag & drop)
- `Chart.tsx` (wrapper para gráficos)
- `Badge.tsx` (etiquetas de estado)
- `Toast.tsx` (notificaciones)

### ESTADOS Y VALIDACIÓN
- Formularios con validación en tiempo real
- Manejo de estados de carga
- Mensajes de error user-friendly
- Confirmaciones antes de acciones críticas

### TECNOLOGÍAS FRONTEND
- React 18 con hooks
- Tailwind CSS para estilos
- Lucide React para iconos
- React Hook Form para formularios
- Zod para validación
- TanStack Query para estado del servidor
- Recharts para gráficos

Implementa primero el layout principal, dashboard y la interfaz del asistente IA. 
NO conectes todavía con el backend, usa datos mock por ahora.

¿Comenzamos con el frontend?

## FASE 3: DESARROLLO DEL BACKEND

Implementa la API REST completa con FastAPI:

### MODELOS DE BASE DE DATOS (SQLAlchemy)
```python
# models/user.py
class User:
    - id (UUID)
    - email (unique)
    - hashed_password
    - full_name
    - role (admin, manager, technician)
    - subscription_tier (free, pro, enterprise)
    - subscription_expires_at
    - created_at, updated_at
    - is_active

# models/production_line.py
class ProductionLine:
    - id (UUID)
    - code (L16, L20, L33, etc.)
    - name
    - description
    - is_active
    - created_at

# models/machine.py
class Machine:
    - id (UUID)
    - production_line_id (FK)
    - code
    - name
    - machine_type (etiquetadora, encajadora, llenadora...)
    - manufacturer
    - model
    - installation_date
    - specifications (JSON)
    - is_active

# models/failure.py
class Failure:
    - id (UUID)
    - machine_id (FK)
    - reported_by (FK User)
    - title
    - description
    - severity (critical, high, medium, low)
    - status (open, in_progress, resolved, closed)
    - reported_at
    - resolved_at
    - downtime_minutes
    - images (Array)

# models/solution.py
class Solution:
    - id (UUID)
    - failure_id (FK)
    - solved_by (FK User)
    - description
    - steps_taken (JSON)
    - parts_replaced (Array)
    - time_spent_minutes
    - created_at

# models/manual.py
class Manual:
    - id (UUID)
    - machine_id (FK, nullable)
    - production_line_id (FK, nullable)
    - title
    - file_path
    - file_type
    - version
    - uploaded_by (FK User)
    - tags (Array)
    - uploaded_at

# models/kpi.py
class KPI:
    - id (UUID)
    - production_line_id (FK, nullable)
    - machine_id (FK, nullable)
    - period_start
    - period_end
    - mttr (Mean Time To Repair)
    - mtbf (Mean Time Between Failures)
    - availability_percentage
    - total_failures
    - total_downtime_minutes
    - calculated_at
```

### ENDPOINTS DE LA API

**Autenticación** (`/api/auth`)
- POST /register - Registro de usuario
- POST /login - Login con JWT
- POST /refresh - Renovar token
- GET /me - Usuario actual
- POST /logout

**Líneas de Producción** (`/api/lines`)
- GET / - Listar todas las líneas
- POST / - Crear línea (admin)
- GET /{id} - Detalle de línea
- PUT /{id} - Actualizar línea
- DELETE /{id} - Eliminar línea
- GET /{id}/machines - Máquinas de la línea
- GET /{id}/kpis - KPIs de la línea

**Máquinas** (`/api/machines`)
- GET / - Listar todas (con filtros)
- POST / - Crear máquina
- GET /{id} - Detalle de máquina
- PUT /{id} - Actualizar máquina
- DELETE /{id} - Eliminar máquina
- GET /{id}/failures - Histórico de averías
- GET /{id}/kpis - KPIs de la máquina

**Averías** (`/api/failures`)
- GET / - Listar con filtros avanzados
- POST / - Registrar nueva avería
- GET /{id} - Detalle completo
- PUT /{id} - Actualizar avería
- DELETE /{id} - Eliminar avería
- POST /{id}/solution - Añadir solución
- GET /{id}/similar - Averías similares (para IA)
- POST /{id}/images - Subir imágenes

**Manuales** (`/api/manuals`)
- GET / - Listar con filtros
- POST / - Subir manual
- GET /{id} - Descargar manual
- PUT /{id} - Actualizar metadata
- DELETE /{id} - Eliminar manual
- GET /search - Búsqueda avanzada

**KPIs** (`/api/kpis`)
- GET /dashboard - KPIs principales
- GET /calculate - Calcular KPIs (job programado)
- GET /line/{id} - KPIs por línea
- GET /machine/{id} - KPIs por máquina
- GET /trends - Tendencias temporales

**Suscripciones** (`/api/subscriptions`)
- GET /plans - Planes disponibles
- POST /subscribe - Crear suscripción
- GET /current - Suscripción actual
- POST /cancel - Cancelar suscripción
- POST /upgrade - Mejorar plan

### SERVICIOS DE LÓGICA DE NEGOCIO

- `AuthService`: Manejo de JWT, roles, permisos
- `FailureService`: Lógica de averías y búsqueda
- `KPIService`: Cálculo de métricas (MTTR, MTBF)
- `FileService`: Upload/download de archivos
- `NotificationService`: Emails y alertas
- `SubscriptionService`: Validación de planes

### CARACTERÍSTICAS TÉCNICAS

- Paginación en todos los listados
- Filtros avanzados con query params
- Validación con Pydantic schemas
- Manejo de errores HTTP consistente
- Logging estructurado
- Rate limiting por endpoint
- Middleware de autenticación JWT
- CORS configurado correctamente
- Documentación automática con Swagger
- Tests unitarios básicos

### MIGRACIONES ALEMBIC
Crea las migraciones iniciales para todas las tablas.

### SEEDS DE DATOS
Script para poblar BD con datos de ejemplo:
- 3 líneas de producción (L16, L20, L33)
- 15 máquinas distribuidas
- 50 averías históricas
- 30 soluciones
- Usuario admin y usuarios de prueba

Implementa primero los modelos, luego los endpoints básicos de CRUD, 
y finalmente la lógica de negocio más compleja.

¿Procedemos con el backend?

## FASE 4: INTEGRACIÓN FRONTEND-BACKEND Y ASISTENTE IA

### PARTE A: INTEGRACIÓN DE SERVICIOS

1. **Conectar Frontend con Backend**
   - Configurar cliente API con fetch/axios
   - Implementar interceptores para JWT
   - Manejo de errores global
   - Estado de autenticación con context
   - Conectar todos los componentes a endpoints reales
   - Eliminar datos mock

2. **Sistema de Autenticación Completo**
   - Página de login/registro
   - Protección de rutas
   - Refresh token automático
   - Logout y sesión expirada
   - Recuperación de contraseña (opcional)

3. **Upload de Archivos**
   - Implementar subida de imágenes en averías
   - Upload de PDFs en manuales
   - Validación de tipos y tamaños
   - Almacenamiento en filesystem o S3

### PARTE B: ASISTENTE IA CON CLAUDE

**Endpoint del Asistente** (`/api/assistant`)
```python
# backend/app/api/assistant.py

POST /api/assistant/chat
Request:
{
  "message": "¿Qué averías ha tenido la llenadora de L16?",
  "conversation_id": "uuid-opcional",
  "context": {
    "production_line": "L16",
    "machine_id": "uuid-opcional"
  }
}

Response:
{
  "response": "Mensaje de Claude",
  "conversation_id": "uuid",
  "sources": ["failure_ids", "manual_ids"],
  "suggested_actions": []
}
```

**Servicio de IA** (`services/ai_service.py`)

Implementar:

1. **Preparación del Contexto**
```python
def prepare_context(user_query, filters):
    """
    Recopila información relevante:
    - Averías históricas similares
    - Soluciones previas exitosas
    - Manuales relacionados
    - Especificaciones de máquinas
    - KPIs actuales
    """
    # Búsqueda vectorial o keyword en BD
    # Extraer texto de PDFs relevantes
    # Formatear para Claude
```

2. **Construcción del Prompt**
```python
system_prompt = """
Eres un asistente especializado en mantenimiento industrial.
Tienes acceso a:
- Histórico completo de averías y soluciones
- Manuales técnicos de las máquinas
- KPIs y métricas de rendimiento
- Especificaciones de equipos

Tu objetivo: ayudar al personal de mantenimiento a resolver averías 
rápidamente proporcionando:
1. Diagnóstico basado en histórico
2. Soluciones probadas anteriormente
3. Referencias a manuales específicos
4. Recomendaciones preventivas

CONTEXTO DEL SISTEMA:
{context}

Responde en español, de forma clara y accionable.
"""

user_prompt = """
CONSULTA: {user_query}

DATOS RELEVANTES:
{relevant_data}

Por favor, proporciona una respuesta estructurada.
"""
```

3. **Llamada a la API de Claude**
```python
async def get_ai_response(message, context):
    client = anthropic.Anthropic(api_key=settings.CLAUDE_API_KEY)
    
    # Preparar contexto enriquecido
    enriched_context = await prepare_context(message, context)
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        system=system_prompt.format(context=enriched_context),
        messages=[
            {"role": "user", "content": user_prompt.format(
                user_query=message,
                relevant_data=enriched_context
            )}
        ]
    )
    
    return response.content[0].text
```

4. **Funcionalidades Avanzadas**
   - Historial de conversaciones persistente
   - Streaming de respuestas (SSE)
   - Extracción de entidades (líneas, máquinas mencionadas)
   - Sugerencias de acciones (crear avería, ver manual)
   - Feedback de utilidad (thumbs up/down)
   - Citas a fuentes (links a averías/manuales)

5. **Búsqueda Semántica** (opcional pero recomendado)
   - Embeddings de averías con Claude API
   - Vector database (pgvector o Pinecone)
   - Búsqueda por similitud para contexto

**Componente Frontend del Chat**

Actualizar `AIAssistant.tsx`:
- Integrar con endpoint real
- Streaming de respuestas con SSE
- Mostrar "Claude está escribiendo..."
- Renderizar markdown con syntax highlighting
- Botones para acciones sugeridas
- Referencias clicables a documentos
- Sistema de rating de respuestas

### PARTE C: FUNCIONALIDADES FINALES

1. **Búsqueda Global**
   - Endpoint /api/search
   - Buscar en averías, soluciones, manuales
   - Resultados rankeados

2. **Notificaciones**
   - Alertas de averías críticas
   - Recordatorios de mantenimiento
   - Websockets o polling

3. **Exportaciones**
   - Excel de históricos
   - PDF de reportes
   - Librería openpyxl o pandas

4. **Análisis Predictivo** (bonus)
   - Claude analiza patrones
   - Sugerencias de mantenimiento preventivo
   - Predicción de fallos recurrentes

### TESTING E2E
- Playwright para frontend
- Pytest para backend
- Test de flujo completo: login → crear avería → consultar IA

¿Implementamos la integración y el asistente IA?

## FASE 5: OPTIMIZACIÓN Y DESPLIEGUE

### OPTIMIZACIONES

1. **Performance Frontend**
   - Code splitting por rutas
   - Lazy loading de componentes pesados
   - Optimización de imágenes
   - Caché de queries con TanStack Query
   - Virtualización de listas largas

2. **Performance Backend**
   - Índices en BD para queries frecuentes
   - Caché con Redis (opcional)
   - Paginación eficiente
   - Query optimization
   - Background jobs con Celery (para KPIs)

3. **Seguridad**
   - Rate limiting por IP
   - Sanitización de inputs
   - HTTPS obligatorio
   - Secrets en variables de entorno
   - Validación de suscripción en middleware
   - CSP headers

### CONFIGURACIÓN DE DEPLOYMENT

**Docker Compose Completo**
```yaml
services:
  postgres:
    image: postgres:16
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: maintenance_db
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
  
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://...
      CLAUDE_API_KEY: ${CLAUDE_API_KEY}
      JWT_SECRET: ${JWT_SECRET}
    depends_on:
      - postgres
  
  frontend:
    build: ./frontend
    ports:
      - "4321:4321"
    environment:
      API_URL: http://backend:8000
```

**Variables de Entorno**
```env
# Backend
DATABASE_URL=
JWT_SECRET=
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
CLAUDE_API_KEY=
FILE_UPLOAD_PATH=/app/uploads
MAX_FILE_SIZE_MB=10

# Frontend
PUBLIC_API_URL=http://localhost:8000
```

### DOCUMENTACIÓN

1. README.md con:
   - Descripción del proyecto
   - Stack tecnológico
   - Instalación y setup
   - Variables de entorno
   - Scripts disponibles

2. API Documentation
   - Swagger automático en /docs
   - Ejemplos de requests
   - Códigos de error

3. Manual de Usuario
   - Guía de uso de cada módulo
   - Flujos de trabajo típicos
   - FAQs

### DEPLOYMENT OPTIONS

**Opción 1: VPS (DigitalOcean, Linode)**
- Docker Compose en producción
- Nginx como reverse proxy
- Certbot para SSL
- Backups automáticos de BD

**Opción 2: Cloud (Railway, Render)**
- Backend en Render/Railway
- Frontend en Vercel
- BD PostgreSQL gestionada

**Opción 3: AWS**
- ECS para containers
- RDS para PostgreSQL
- S3 para archivos estáticos
- CloudFront para CDN

### MONITORING

- Logging con estructurado (JSON)
- Sentry para error tracking
- Métricas básicas de uso
- Health checks para servicios

### PRÓXIMOS PASOS

Después del MVP:
- App móvil con React Native
- Notificaciones push
- Integración con CMMS existente
- Dashboard ejecutivo con más métricas
- Modelo ML propio para predicciones
- Multi-idioma

¿Procedemos con optimización y deployment?


## NOTAS PARA CLAUDE CODE

Cada fase debe completarse antes de avanzar
Pedir confirmación antes de generar código extenso
Priorizar funcionalidad sobre perfección en MVP
Código limpio y comentado
Seguir convenciones de cada framework
Tests básicos en componentes críticos