from sqlalchemy import Column, String, Integer, ForeignKey, Text, Boolean
from app.models.base import BaseModel


class Solution(BaseModel):
    """Modelo de soluciones aplicadas a averías"""
    __tablename__ = "solutions"

    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    failure_id = Column(Integer, ForeignKey("failures.id"), nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    time_spent_minutes = Column(Integer, nullable=True)  # Tiempo en minutos
    was_successful = Column(Boolean, default=True)
    ai_suggested = Column(Boolean, default=False)  # Si fue sugerida por IA

    # Relaciones se agregarán en fases posteriores
    # failure = relationship("Failure", back_populates="solutions")
    # user = relationship("User")
