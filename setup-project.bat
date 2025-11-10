@echo off
echo ================================================
echo   Setup Completo - Gestion de Averias
echo ================================================
echo.

echo [1/4] Iniciando PostgreSQL con Docker...
docker-compose up -d
echo.
echo Esperando que PostgreSQL este listo...
timeout /t 5 /nobreak >nul
echo.

echo [2/4] Configurando Backend...
cd backend
if not exist "venv" (
    echo Creando entorno virtual...
    python -m venv venv
)
call venv\Scripts\activate
if not exist ".env" (
    copy .env.example .env
    echo Archivo .env creado. Por favor, editalo con tus configuraciones.
)
pip install -r requirements.txt
echo Aplicando migraciones...
alembic upgrade head
cd ..
echo.

echo [3/4] Configurando Frontend...
cd frontend
if not exist ".env" (
    copy .env.example .env
)
echo Instalando dependencias del frontend...
call npm install
cd ..
echo.

echo [4/4] Setup completado!
echo.
echo ================================================
echo   Servicios disponibles:
echo ================================================
echo   Frontend:  http://localhost:3000
echo   Backend:   http://localhost:8000
echo   API Docs:  http://localhost:8000/api/docs
echo   pgAdmin:   http://localhost:5050
echo ================================================
echo.
echo Para iniciar los servicios:
echo   - Backend:  start-backend.bat
echo   - Frontend: start-frontend.bat
echo.
pause
