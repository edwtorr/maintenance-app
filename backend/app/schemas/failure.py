from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from uuid import UUID

# Enums
class FailureSeverity(str):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class FailureStatus(str):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

# Base Schema
class FailureBase(BaseModel):
    machine_id: UUID
    title: str = Field(..., min_length=1, max_length=255)
    description: str
    severity: str = Field(default=FailureSeverity.MEDIUM)

# Schema para crear avería
class FailureCreate(FailureBase):
    images: Optional[List[str]] = Field(default_factory=list)

# Schema para actualizar avería
class FailureUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    severity: Optional[str] = None
    status: Optional[str] = None
    resolved_at: Optional[datetime] = None
    downtime_minutes: Optional[int] = None
    images: Optional[List[str]] = None

# Schema de respuesta
class Failure(FailureBase):
    id: UUID
    reported_by: UUID
    status: str
    reported_at: datetime
    resolved_at: Optional[datetime] = None
    downtime_minutes: Optional[int] = None
    images: List[str]

    class Config:
        from_attributes = True

# Schema con información adicional
class FailureWithDetails(Failure):
    machine_code: Optional[str] = None
    machine_name: Optional[str] = None
    production_line_code: Optional[str] = None
    reporter_name: Optional[str] = None
    has_solution: bool = False

# Schema para lista con filtros
class FailureListFilter(BaseModel):
    production_line_id: Optional[UUID] = None
    machine_id: Optional[UUID] = None
    status: Optional[str] = None
    severity: Optional[str] = None
    reported_after: Optional[datetime] = None
    reported_before: Optional[datetime] = None
    search: Optional[str] = None
    skip: int = Field(default=0, ge=0)
    limit: int = Field(default=100, ge=1, le=100)
