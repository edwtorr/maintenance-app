from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Text
from app.models.base import BaseModel


class Machine(BaseModel):
    """Modelo de máquinas por línea de producción"""
    __tablename__ = "machines"

    name = Column(String(100), nullable=False)
    code = Column(String(50), unique=True, nullable=False)
    description = Column(Text)
    production_line_id = Column(Integer, ForeignKey("production_lines.id"), nullable=False)
    is_active = Column(Boolean, default=True)

    # Relaciones se agregarán en fases posteriores
    # production_line = relationship("ProductionLine", back_populates="machines")
    # failures = relationship("Failure", back_populates="machine")
    # manuals = relationship("Manual", back_populates="machine")
