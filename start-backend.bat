@echo off
echo ========================================
echo   Iniciando Backend - Gestion Averias
echo ========================================
echo.

cd backend

if not exist "venv" (
    echo Creando entorno virtual...
    python -m venv venv
    echo.
)

echo Activando entorno virtual...
call venv\Scripts\activate
echo.

if not exist ".env" (
    echo Creando archivo .env...
    copy .env.example .env
    echo.
    echo IMPORTANTE: Edita el archivo .env con tus configuraciones
    echo (DATABASE_URL, SECRET_KEY, ANTHROPIC_API_KEY)
    echo.
    pause
)

echo Instalando/actualizando dependencias...
pip install -r requirements.txt
echo.

echo Verificando estado de la base de datos...
alembic current
echo.

echo Iniciando servidor FastAPI...
echo.
echo La API estara disponible en:
echo   http://localhost:8000
echo   Docs: http://localhost:8000/api/docs
echo.
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
