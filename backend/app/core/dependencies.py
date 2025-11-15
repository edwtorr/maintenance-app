from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.user import User
from app.services.auth_service import AuthService

# Esquema de seguridad Bearer
security = HTTPBearer()


def get_db() -> Generator[Session, None, None]:
    """
    Dependency para obtener la sesión de base de datos
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """
    Dependency para obtener el usuario actual desde el token
    """
    token = credentials.credentials
    return AuthService.get_current_user_from_token(db, token)


def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """
    Dependency para obtener el usuario actual activo
    """
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuario inactivo"
        )
    return current_user


def require_role(allowed_roles: list[str]):
    """
    Dependency factory para requerir roles específicos
    Uso: current_user: User = Depends(require_role(["admin", "manager"]))
    """
    def role_checker(current_user: User = Depends(get_current_active_user)) -> User:
        AuthService.check_role(current_user, allowed_roles)
        return current_user

    return role_checker


def require_subscription(required_tier: str = "free"):
    """
    Dependency factory para requerir nivel de suscripción
    Uso: current_user: User = Depends(require_subscription("pro"))
    """
    def subscription_checker(current_user: User = Depends(get_current_active_user)) -> User:
        AuthService.check_subscription(current_user, required_tier)
        return current_user

    return subscription_checker


# Aliases comunes
require_admin = require_role(["admin"])
require_manager = require_role(["admin", "manager"])
require_pro = require_subscription("pro")
require_enterprise = require_subscription("enterprise")
