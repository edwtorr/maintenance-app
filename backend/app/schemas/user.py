from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

# Enums
class UserRole(str):
    ADMIN = "admin"
    MANAGER = "manager"
    TECHNICIAN = "technician"

class SubscriptionTier(str):
    FREE = "free"
    PRO = "pro"
    ENTERPRISE = "enterprise"

# Base Schema
class UserBase(BaseModel):
    email: EmailStr
    full_name: str = Field(..., min_length=1, max_length=255)
    role: str = Field(default=UserRole.TECHNICIAN)

# Schema para crear usuario
class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=100)

# Schema para login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Schema para actualizar usuario
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(None, min_length=1, max_length=255)
    role: Optional[str] = None
    is_active: Optional[bool] = None

# Schema de respuesta (sin password)
class User(UserBase):
    id: int
    role: str
    subscription_tier: str
    subscription_expires_at: Optional[datetime] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# Schema para respuesta con token
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    user_id: Optional[str] = None
    email: Optional[str] = None

# Schema para refresh token
class TokenRefresh(BaseModel):
    refresh_token: str
