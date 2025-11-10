from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="API para gestión de averías industriales",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.get("/")
async def root():
    return {
        "message": "Maintenance App API",
        "version": settings.VERSION,
        "docs": "/api/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Importar y registrar routers aquí cuando estén listos
# from app.api import auth, failures, machines, production_lines, solutions, manuals, kpi, ai
# app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
# app.include_router(failures.router, prefix="/api/failures", tags=["failures"])
# app.include_router(machines.router, prefix="/api/machines", tags=["machines"])
# app.include_router(production_lines.router, prefix="/api/production-lines", tags=["production-lines"])
# app.include_router(solutions.router, prefix="/api/solutions", tags=["solutions"])
# app.include_router(manuals.router, prefix="/api/manuals", tags=["manuals"])
# app.include_router(kpi.router, prefix="/api/kpi", tags=["kpi"])
# app.include_router(ai.router, prefix="/api/ai", tags=["ai"])
