from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List

# Base Schema
class ManualBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    machine_id: Optional[int] = None
    production_line_id: Optional[int] = None
    file_type: str = Field(..., description="Tipo de archivo: pdf, doc, etc.")
    version: Optional[str] = None
    tags: Optional[List[str]] = Field(default_factory=list)

# Schema para crear manual
class ManualCreate(ManualBase):
    file_path: str  # Se establece después de subir el archivo

# Schema para actualizar manual
class ManualUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    machine_id: Optional[int] = None
    production_line_id: Optional[int] = None
    version: Optional[str] = None
    tags: Optional[List[str]] = None

# Schema de respuesta
class Manual(ManualBase):
    id: int
    file_path: str
    uploaded_by: int
    uploaded_at: datetime

    class Config:
        from_attributes = True

# Schema con información adicional
class ManualWithDetails(Manual):
    uploader_name: Optional[str] = None
    machine_code: Optional[str] = None
    machine_name: Optional[str] = None
    production_line_code: Optional[str] = None
    file_size_bytes: Optional[int] = None

# Schema para búsqueda
class ManualSearchFilter(BaseModel):
    search: Optional[str] = None
    machine_id: Optional[int] = None
    production_line_id: Optional[int] = None
    file_type: Optional[str] = None
    tags: Optional[List[str]] = None
    skip: int = Field(default=0, ge=0)
    limit: int = Field(default=100, ge=1, le=100)
