from sqlalchemy import Column, String, Integer, ForeignKey, Float, Date
from app.models.base import BaseModel


class KPI(BaseModel):
    """Modelo de métricas calculadas"""
    __tablename__ = "kpis"

    date = Column(Date, nullable=False)
    production_line_id = Column(Integer, ForeignKey("production_lines.id"), nullable=True)
    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=True)

    # Métricas
    total_failures = Column(Integer, default=0)
    open_failures = Column(Integer, default=0)
    resolved_failures = Column(Integer, default=0)
    average_resolution_time_minutes = Column(Float, nullable=True)
    mtbf = Column(Float, nullable=True)  # Mean Time Between Failures
    mttr = Column(Float, nullable=True)  # Mean Time To Repair
    availability_percentage = Column(Float, nullable=True)

    # Relaciones se agregarán en fases posteriores
    # production_line = relationship("ProductionLine")
    # machine = relationship("Machine")
