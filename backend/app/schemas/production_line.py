from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# Base Schema
class ProductionLineBase(BaseModel):
    code: str = Field(..., min_length=1, max_length=50, description="Código de la línea (L16, L20, L33)")
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None

# Schema para crear línea
class ProductionLineCreate(ProductionLineBase):
    pass

# Schema para actualizar línea
class ProductionLineUpdate(BaseModel):
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    is_active: Optional[bool] = None

# Schema de respuesta
class ProductionLine(ProductionLineBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

# Schema con estadísticas adicionales
class ProductionLineWithStats(ProductionLine):
    total_machines: int = 0
    active_failures: int = 0
    availability: Optional[float] = None
