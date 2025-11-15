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

# Importar y registrar routers
from app.api import auth, production_lines

app.include_router(auth.router, prefix=settings.API_V1_STR)
app.include_router(production_lines.router, prefix=settings.API_V1_STR)
