from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, desc
from datetime import datetime

from app.core.dependencies import get_db, get_current_active_user
from app.models.user import User
from app.models.failure import Failure, FailureStatus, FailureSeverity
from app.models.machine import Machine
from app.models.production_line import ProductionLine
from app.schemas.failure import (
    Failure as FailureSchema,
    FailureCreate,
    FailureUpdate,
    FailureWithDetails
)

router = APIRouter()


@router.get("/", response_model=List[FailureWithDetails])
def list_failures(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    production_line_id: Optional[int] = None,
    machine_id: Optional[int] = None,
    status_filter: Optional[str] = Query(None, alias="status"),
    severity: Optional[str] = None,
    reported_after: Optional[datetime] = None,
    reported_before: Optional[datetime] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Listar todas las averías con filtros avanzados
    """
    query = db.query(Failure)

    # Filtro por línea de producción (join con machines)
    if production_line_id:
        query = query.join(Machine).filter(Machine.production_line_id == production_line_id)

    # Filtro por máquina
    if machine_id:
        query = query.filter(Failure.machine_id == machine_id)

    # Filtro por estado
    if status_filter:
        query = query.filter(Failure.status == status_filter)

    # Filtro por severidad
    if severity:
        query = query.filter(Failure.severity == severity)

    # Filtro por fecha de reporte
    if reported_after:
        query = query.filter(Failure.reported_at >= reported_after)

    if reported_before:
        query = query.filter(Failure.reported_at <= reported_before)

    # Búsqueda de texto
    if search:
        query = query.filter(
            or_(
                Failure.title.ilike(f"%{search}%"),
                Failure.description.ilike(f"%{search}%")
            )
        )

    # Ordenar por fecha más reciente primero
    query = query.order_by(desc(Failure.reported_at))

    # Paginación
    failures = query.offset(skip).limit(limit).all()

    # Enriquecer con información adicional
    result = []
    for failure in failures:
        failure_dict = FailureSchema.model_validate(failure).model_dump()

        # Información de la máquina
        machine = db.query(Machine).filter(Machine.id == failure.machine_id).first()
        if machine:
            failure_dict['machine_code'] = machine.code
            failure_dict['machine_name'] = machine.name

            # Información de la línea de producción
            line = db.query(ProductionLine).filter(ProductionLine.id == machine.production_line_id).first()
            if line:
                failure_dict['production_line_code'] = line.name

        # Información del reportero
        reporter = db.query(User).filter(User.id == failure.reported_by).first()
        if reporter:
            failure_dict['reporter_name'] = reporter.full_name

        # TODO: Verificar si tiene solución cuando exista el modelo Solution
        failure_dict['has_solution'] = False

        result.append(FailureWithDetails(**failure_dict))

    return result


@router.get("/{failure_id}", response_model=FailureWithDetails)
def get_failure(
    failure_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Obtener detalle completo de una avería
    """
    failure = db.query(Failure).filter(Failure.id == failure_id).first()

    if not failure:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Avería con ID {failure_id} no encontrada"
        )

    failure_dict = FailureSchema.model_validate(failure).model_dump()

    # Información de la máquina
    machine = db.query(Machine).filter(Machine.id == failure.machine_id).first()
    if machine:
        failure_dict['machine_code'] = machine.code
        failure_dict['machine_name'] = machine.name

        # Información de la línea de producción
        line = db.query(ProductionLine).filter(ProductionLine.id == machine.production_line_id).first()
        if line:
            failure_dict['production_line_code'] = line.name

    # Información del reportero
    reporter = db.query(User).filter(User.id == failure.reported_by).first()
    if reporter:
        failure_dict['reporter_name'] = reporter.full_name

    # TODO: Verificar si tiene solución
    failure_dict['has_solution'] = False

    return FailureWithDetails(**failure_dict)


@router.post("/", response_model=FailureSchema, status_code=status.HTTP_201_CREATED)
def create_failure(
    failure_data: FailureCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Registrar una nueva avería
    """
    # Verificar que la máquina existe
    machine = db.query(Machine).filter(Machine.id == failure_data.machine_id).first()
    if not machine:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Máquina con ID {failure_data.machine_id} no encontrada"
        )

    # Crear la avería
    new_failure = Failure(
        **failure_data.model_dump(),
        reported_by=current_user.id,
        reported_at=datetime.utcnow()
    )

    db.add(new_failure)
    db.commit()
    db.refresh(new_failure)

    return FailureSchema.model_validate(new_failure)


@router.put("/{failure_id}", response_model=FailureSchema)
def update_failure(
    failure_id: int,
    failure_data: FailureUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Actualizar una avería existente
    """
    failure = db.query(Failure).filter(Failure.id == failure_id).first()

    if not failure:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Avería con ID {failure_id} no encontrada"
        )

    # Actualizar campos
    update_data = failure_data.model_dump(exclude_unset=True)

    # Si se está resolviendo la avería, establecer la fecha
    if 'status' in update_data:
        if update_data['status'] in [FailureStatus.RESOLVED.value, FailureStatus.CLOSED.value]:
            if not failure.resolved_at:
                update_data['resolved_at'] = datetime.utcnow()

    for field, value in update_data.items():
        setattr(failure, field, value)

    db.commit()
    db.refresh(failure)

    return FailureSchema.model_validate(failure)


@router.delete("/{failure_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_failure(
    failure_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Eliminar una avería
    Solo admins pueden eliminar
    """
    # Verificar si es admin
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo los administradores pueden eliminar averías"
        )

    failure = db.query(Failure).filter(Failure.id == failure_id).first()

    if not failure:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Avería con ID {failure_id} no encontrada"
        )

    db.delete(failure)
    db.commit()

    return None


@router.get("/machine/{machine_id}/history", response_model=List[FailureSchema])
def get_machine_failure_history(
    machine_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Obtener histórico de averías de una máquina específica
    """
    # Verificar que la máquina existe
    machine = db.query(Machine).filter(Machine.id == machine_id).first()
    if not machine:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Máquina con ID {machine_id} no encontrada"
        )

    # Obtener averías ordenadas por fecha
    failures = db.query(Failure).filter(
        Failure.machine_id == machine_id
    ).order_by(desc(Failure.reported_at)).offset(skip).limit(limit).all()

    return [FailureSchema.model_validate(f) for f in failures]


@router.get("/stats/summary")
def get_failures_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Obtener resumen de estadísticas de averías
    """
    total = db.query(Failure).count()
    open_failures = db.query(Failure).filter(Failure.status == FailureStatus.OPEN).count()
    in_progress = db.query(Failure).filter(Failure.status == FailureStatus.IN_PROGRESS).count()
    resolved = db.query(Failure).filter(Failure.status == FailureStatus.RESOLVED).count()
    critical = db.query(Failure).filter(Failure.severity == FailureSeverity.CRITICAL).count()

    return {
        "total_failures": total,
        "open": open_failures,
        "in_progress": in_progress,
        "resolved": resolved,
        "critical_pending": critical
    }
