from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_active_user
from app.schemas import (
    UserCreate, UserLogin, User, Token, TokenRefresh
)
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
def register(
    user_create: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Registrar un nuevo usuario
    """
    return AuthService.create_user(db, user_create)


@router.post("/login", response_model=Token)
def login(
    user_login: UserLogin,
    db: Session = Depends(get_db)
):
    """
    Login con email y contraseña
    Retorna access_token y refresh_token
    """
    user = AuthService.authenticate_user(
        db,
        email=user_login.email,
        password=user_login.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return AuthService.create_tokens(user)


@router.post("/refresh", response_model=Token)
def refresh_token(
    token_refresh: TokenRefresh,
    db: Session = Depends(get_db)
):
    """
    Renovar el access token usando el refresh token
    """
    return AuthService.refresh_access_token(db, token_refresh.refresh_token)


@router.get("/me", response_model=User)
def get_current_user_info(
    current_user: User = Depends(get_current_active_user)
):
    """
    Obtener información del usuario actual
    """
    return current_user


@router.post("/logout")
def logout(
    current_user: User = Depends(get_current_active_user)
):
    """
    Logout (en el cliente se debe eliminar el token)
    """
    return {"message": "Logout exitoso"}
