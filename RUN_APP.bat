@echo off
echo ========================================
echo   Ejecutando App - Gestion Averias
echo ========================================
echo.

echo [Paso 1/2] Verificando dependencias...
cd frontend

if not exist "node_modules" (
    echo.
    echo Instalando dependencias de npm...
    echo Esto puede tardar unos minutos...
    echo.
    call npm install
    echo.
)

echo.
echo [Paso 2/2] Iniciando servidor de desarrollo...
echo.
echo ========================================
echo   La aplicacion estara disponible en:
echo   http://localhost:4321
echo   o
echo   http://localhost:3000
echo ========================================
echo.
echo Presiona Ctrl+C para detener el servidor
echo.

call npm run dev
