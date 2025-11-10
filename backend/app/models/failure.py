from sqlalchemy import Column, String, Integer, ForeignKey, Text, DateTime, Enum
from app.models.base import BaseModel
import enum


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

    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=False)
    reported_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    assigned_to = Column(Integer, ForeignKey("users.id"), nullable=True)
    status = Column(Enum(FailureStatus), default=FailureStatus.OPEN, nullable=False)
    severity = Column(Enum(FailureSeverity), default=FailureSeverity.MEDIUM, nullable=False)
    resolved_at = Column(DateTime, nullable=True)

    # Relaciones se agregarán en fases posteriores
    # machine = relationship("Machine", back_populates="failures")
    # reporter = relationship("User", foreign_keys=[reported_by])
    # assignee = relationship("User", foreign_keys=[assigned_to])
    # solutions = relationship("Solution", back_populates="failure")
