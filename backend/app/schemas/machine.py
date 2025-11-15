from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional, Dict, Any

# Base Schema
class MachineBase(BaseModel):
    production_line_id: int
    code: str = Field(..., min_length=1, max_length=50)
    name: str = Field(..., min_length=1, max_length=255)
    machine_type: str = Field(..., description="Tipo: etiquetadora, encajadora, llenadora, etc.")
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    installation_date: Optional[date] = None
    specifications: Optional[Dict[str, Any]] = Field(default_factory=dict)

# Schema para crear máquina
class MachineCreate(MachineBase):
    pass

# Schema para actualizar máquina
class MachineUpdate(BaseModel):
    production_line_id: Optional[int] = None
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    machine_type: Optional[str] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    installation_date: Optional[date] = None
    specifications: Optional[Dict[str, Any]] = None
    is_active: Optional[bool] = None

# Schema de respuesta
class Machine(MachineBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

# Schema con información de línea
class MachineWithLine(Machine):
    production_line_code: Optional[str] = None
    production_line_name: Optional[str] = None

# Schema con estadísticas
class MachineWithStats(MachineWithLine):
    total_failures: int = 0
    active_failures: int = 0
    mttr: Optional[float] = None  # Mean Time To Repair
    mtbf: Optional[float] = None  # Mean Time Between Failures
