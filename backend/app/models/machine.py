from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Date, JSON
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class Machine(BaseModel):
    """Modelo de máquinas por línea de producción"""
    __tablename__ = "machines"

    code = Column(String(50), unique=True, nullable=False, index=True)
    name = Column(String(255), nullable=False)
    machine_type = Column(String(100), nullable=False, comment="Tipo: etiquetadora, encajadora, llenadora, etc.")
    manufacturer = Column(String(255), nullable=True)
    model = Column(String(100), nullable=True)
    installation_date = Column(Date, nullable=True)
    specifications = Column(JSON, nullable=True, default=dict, comment="Especificaciones técnicas en formato JSON")
    production_line_id = Column(Integer, ForeignKey("production_lines.id"), nullable=False, index=True)
    is_active = Column(Boolean, default=True)

    # Relaciones (se activarán cuando se necesiten)
    # production_line = relationship("ProductionLine", back_populates="machines")
    # failures = relationship("Failure", back_populates="machine", cascade="all, delete-orphan")
    # manuals = relationship("Manual", back_populates="machine")
