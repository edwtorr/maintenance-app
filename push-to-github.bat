@echo off
echo ========================================
echo   Push a GitHub - maintenance-app
echo ========================================
echo.
echo Usuario: edwtorr
echo Repositorio: maintenance-app
echo URL: https://github.com/edwtorr/maintenance-app
echo.
echo IMPORTANTE:
echo 1. Primero crea el repositorio en GitHub:
echo    https://github.com/new
echo.
echo 2. Nombre: maintenance-app
echo 3. NO marques "Add README" ni ".gitignore"
echo.
echo Presiona Enter cuando hayas creado el repositorio...
pause >nul
echo.
echo Haciendo push a GitHub...
echo.

git push -u origin main

echo.
echo ========================================
if %ERRORLEVEL% EQU 0 (
    echo   Push completado con exito!
    echo   Repositorio: https://github.com/edwtorr/maintenance-app
) else (
    echo   Hubo un error. Verifica:
    echo   - Repositorio creado en GitHub
    echo   - Credenciales correctas
    echo   - Conexion a internet
)
echo ========================================
echo.
pause
