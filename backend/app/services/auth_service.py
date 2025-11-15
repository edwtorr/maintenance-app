from datetime import datetime, timedelta
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from uuid import UUID

from app.models.user import User
from app.schemas import UserCreate, UserLogin, Token, TokenData
from app.core.security import (
    verify_password,
    get_password_hash,
    create_access_token,
    create_refresh_token,
    decode_token
)
from app.core.config import settings


class AuthService:
    """Servicio para manejo de autenticación y autorización"""

    @staticmethod
    def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
        """
        Autentica un usuario con email y contraseña
        Retorna el usuario si las credenciales son correctas, None si no
        """
        user = db.query(User).filter(User.email == email).first()

        if not user:
            return None

        if not verify_password(password, user.hashed_password):
            return None

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Usuario inactivo"
            )

        return user

    @staticmethod
    def create_user(db: Session, user_create: UserCreate) -> User:
        """
        Crea un nuevo usuario en la base de datos
        """
        # Verificar si el email ya existe
        existing_user = db.query(User).filter(User.email == user_create.email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El email ya está registrado"
            )

        # Crear nuevo usuario
        hashed_password = get_password_hash(user_create.password)

        db_user = User(
            email=user_create.email,
            full_name=user_create.full_name,
            hashed_password=hashed_password,
            role=user_create.role,
            subscription_tier="free",  # Por defecto tier free
            is_active=True
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    @staticmethod
    def create_tokens(user: User) -> Token:
        """
        Crea tokens de acceso y refresh para un usuario
        """
        access_token = create_access_token(
            data={"sub": str(user.id), "email": user.email, "role": user.role}
        )
        refresh_token = create_refresh_token(
            data={"sub": str(user.id), "email": user.email}
        )

        return Token(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer"
        )

    @staticmethod
    def refresh_access_token(db: Session, refresh_token: str) -> Token:
        """
        Genera un nuevo access token usando un refresh token válido
        """
        payload = decode_token(refresh_token)

        if not payload or payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token de refresh inválido"
            )

        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido"
            )

        # Buscar usuario
        user = db.query(User).filter(User.id == UUID(user_id)).first()
        if not user or not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuario no encontrado o inactivo"
            )

        # Crear nuevos tokens
        return AuthService.create_tokens(user)

    @staticmethod
    def get_current_user_from_token(db: Session, token: str) -> User:
        """
        Obtiene el usuario actual desde un token de acceso
        """
        payload = decode_token(token)

        if not payload or payload.get("type") != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token de acceso inválido",
                headers={"WWW-Authenticate": "Bearer"},
            )

        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido",
                headers={"WWW-Authenticate": "Bearer"},
            )

        user = db.query(User).filter(User.id == UUID(user_id)).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado"
            )

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Usuario inactivo"
            )

        return user

    @staticmethod
    def check_subscription(user: User, required_tier: str = "free") -> bool:
        """
        Verifica si el usuario tiene el nivel de suscripción requerido
        """
        tier_hierarchy = {"free": 0, "pro": 1, "enterprise": 2}

        user_tier_level = tier_hierarchy.get(user.subscription_tier, 0)
        required_tier_level = tier_hierarchy.get(required_tier, 0)

        if user_tier_level < required_tier_level:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Se requiere suscripción {required_tier} o superior"
            )

        # Verificar si la suscripción ha expirado
        if user.subscription_expires_at and user.subscription_expires_at < datetime.utcnow():
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Suscripción expirada"
            )

        return True

    @staticmethod
    def check_role(user: User, allowed_roles: list[str]) -> bool:
        """
        Verifica si el usuario tiene uno de los roles permitidos
        """
        if user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permisos para realizar esta acción"
            )

        return True
