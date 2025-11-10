@echo off
echo ========================================
echo   Iniciando Frontend - Gestion Averias
echo ========================================
echo.

cd frontend

if not exist "node_modules" (
    echo Instalando dependencias...
    call npm install
    echo.
)

if not exist ".env" (
    echo Creando archivo .env...
    copy .env.example .env
    echo.
)

echo Iniciando servidor de desarrollo...
echo.
echo La aplicacion estara disponible en:
echo   http://localhost:4321
echo   o
echo   http://localhost:3000
echo.
call npm run dev
