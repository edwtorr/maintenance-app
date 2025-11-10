from sqlalchemy import Column, String, Boolean, Text
from app.models.base import BaseModel


class ProductionLine(BaseModel):
    """Modelo de líneas de producción (L16, L20, L33, etc.)"""
    __tablename__ = "production_lines"

    name = Column(String(50), unique=True, nullable=False)  # L16, L20, L33
    description = Column(Text)
    is_active = Column(Boolean, default=True)

    # Relaciones se agregarán en fases posteriores
    # machines = relationship("Machine", back_populates="production_line")
