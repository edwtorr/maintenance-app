from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List, Dict, Any
from uuid import UUID

# Base Schema
class SolutionBase(BaseModel):
    failure_id: UUID
    description: str
    steps_taken: Optional[Dict[str, Any]] = Field(default_factory=dict)
    parts_replaced: Optional[List[str]] = Field(default_factory=list)
    time_spent_minutes: Optional[int] = Field(None, ge=0)

# Schema para crear solución
class SolutionCreate(SolutionBase):
    pass

# Schema para actualizar solución
class SolutionUpdate(BaseModel):
    description: Optional[str] = None
    steps_taken: Optional[Dict[str, Any]] = None
    parts_replaced: Optional[List[str]] = None
    time_spent_minutes: Optional[int] = Field(None, ge=0)

# Schema de respuesta
class Solution(SolutionBase):
    id: UUID
    solved_by: UUID
    created_at: datetime

    class Config:
        from_attributes = True

# Schema con información adicional
class SolutionWithDetails(Solution):
    solver_name: Optional[str] = None
    failure_title: Optional[str] = None
    machine_code: Optional[str] = None
