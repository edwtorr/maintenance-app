from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# Base Schema
class KPIBase(BaseModel):
    production_line_id: Optional[int] = None
    machine_id: Optional[int] = None
    period_start: datetime
    period_end: datetime
    mttr: Optional[float] = Field(None, description="Mean Time To Repair (horas)")
    mtbf: Optional[float] = Field(None, description="Mean Time Between Failures (horas)")
    availability_percentage: Optional[float] = Field(None, ge=0, le=100)
    total_failures: int = Field(default=0, ge=0)
    total_downtime_minutes: int = Field(default=0, ge=0)

# Schema para crear KPI
class KPICreate(KPIBase):
    pass

# Schema de respuesta
class KPI(KPIBase):
    id: int
    calculated_at: datetime

    class Config:
        from_attributes = True

# Schema con información adicional
class KPIWithDetails(KPI):
    production_line_code: Optional[str] = None
    production_line_name: Optional[str] = None
    machine_code: Optional[str] = None
    machine_name: Optional[str] = None

# Schema para dashboard
class DashboardKPIs(BaseModel):
    global_mttr: Optional[float] = None
    global_mtbf: Optional[float] = None
    global_availability: Optional[float] = None
    total_open_failures: int = 0
    total_failures_this_month: int = 0
    most_affected_line: Optional[str] = None
    most_affected_machine: Optional[str] = None

# Schema para filtros de KPI
class KPIFilter(BaseModel):
    production_line_id: Optional[int] = None
    machine_id: Optional[int] = None
    period_start: Optional[datetime] = None
    period_end: Optional[datetime] = None
