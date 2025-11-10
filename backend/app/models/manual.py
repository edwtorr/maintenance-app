from sqlalchemy import Column, String, Integer, ForeignKey, Text, Enum
from app.models.base import BaseModel
import enum


class ManualType(str, enum.Enum):
    MAINTENANCE = "maintenance"
    OPERATION = "operation"
    TROUBLESHOOTING = "troubleshooting"
    SAFETY = "safety"


class Manual(BaseModel):
    """Modelo de documentación técnica"""
    __tablename__ = "manuals"

    title = Column(String(200), nullable=False)
    description = Column(Text)
    content = Column(Text, nullable=False)
    manual_type = Column(Enum(ManualType), default=ManualType.MAINTENANCE, nullable=False)
    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=False)
    file_url = Column(String(500), nullable=True)  # URL a archivo PDF/documento
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relaciones se agregarán en fases posteriores
    # machine = relationship("Machine", back_populates="manuals")
    # user = relationship("User")
