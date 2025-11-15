from sqlalchemy import Column, String, Integer, ForeignKey, Text, DateTime, Enum, JSON
from sqlalchemy.orm import relationship
from app.models.base import BaseModel
import enum
from datetime import datetime


class FailureStatus(str, enum.Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"


class FailureSeverity(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Failure(BaseModel):
    """Modelo de histórico de averías"""
    __tablename__ = "failures"

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=False, index=True)
    reported_by = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    assigned_to = Column(Integer, ForeignKey("users.id"), nullable=True)
    status = Column(Enum(FailureStatus), default=FailureStatus.OPEN, nullable=False, index=True)
    severity = Column(Enum(FailureSeverity), default=FailureSeverity.MEDIUM, nullable=False, index=True)
    reported_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    resolved_at = Column(DateTime, nullable=True)
    downtime_minutes = Column(Integer, nullable=True, comment="Tiempo de inactividad en minutos")
    images = Column(JSON, nullable=True, default=list, comment="Rutas de imágenes asociadas")

    # Relaciones (se activarán cuando se necesiten)
    # machine = relationship("Machine", back_populates="failures")
    # reporter = relationship("User", foreign_keys=[reported_by])
    # assignee = relationship("User", foreign_keys=[assigned_to])
    # solutions = relationship("Solution", back_populates="failure", cascade="all, delete-orphan")
