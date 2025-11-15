from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.core.dependencies import get_db, get_current_active_user, require_manager
from app.models.user import User
from app.models.machine import Machine
from app.models.production_line import ProductionLine
from app.schemas.machine import (
    Machine as MachineSchema,
    MachineCreate,
    MachineUpdate,
    MachineWithLine,
    MachineWithStats
)

router = APIRouter()


@router.get("/", response_model=List[MachineWithLine])
def list_machines(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    production_line_id: Optional[int] = None,
    is_active: Optional[bool] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Listar todas las máquinas con filtros opcionales
    """
    query = db.query(Machine)

    # Filtros
    if production_line_id:
        query = query.filter(Machine.production_line_id == production_line_id)

    if is_active is not None:
        query = query.filter(Machine.is_active == is_active)

    if search:
        query = query.filter(
            or_(
                Machine.code.ilike(f"%{search}%"),
                Machine.name.ilike(f"%{search}%"),
                Machine.machine_type.ilike(f"%{search}%")
            )
        )

    # Paginación
    machines = query.offset(skip).limit(limit).all()

    # Enriquecer con información de la línea
    result = []
    for machine in machines:
        machine_dict = MachineSchema.model_validate(machine).model_dump()

        # Agregar información de la línea
        line = db.query(ProductionLine).filter(ProductionLine.id == machine.production_line_id).first()
        if line:
            machine_dict['production_line_code'] = line.name
            machine_dict['production_line_name'] = line.description or line.name

        result.append(MachineWithLine(**machine_dict))

    return result


@router.get("/{machine_id}", response_model=MachineWithLine)
def get_machine(
    machine_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Obtener detalle de una máquina específica
    """
    machine = db.query(Machine).filter(Machine.id == machine_id).first()

    if not machine:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Máquina con ID {machine_id} no encontrada"
        )

    machine_dict = MachineSchema.model_validate(machine).model_dump()

    # Agregar información de la línea
    line = db.query(ProductionLine).filter(ProductionLine.id == machine.production_line_id).first()
    if line:
        machine_dict['production_line_code'] = line.name
        machine_dict['production_line_name'] = line.description or line.name

    return MachineWithLine(**machine_dict)


@router.post("/", response_model=MachineSchema, status_code=status.HTTP_201_CREATED)
def create_machine(
    machine_data: MachineCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_manager)  # Solo managers y admins
):
    """
    Crear una nueva máquina
    Requiere rol: manager o admin
    """
    # Verificar que la línea de producción existe
    line = db.query(ProductionLine).filter(
        ProductionLine.id == machine_data.production_line_id
    ).first()

    if not line:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Línea de producción con ID {machine_data.production_line_id} no encontrada"
        )

    # Verificar que el código no esté duplicado
    existing = db.query(Machine).filter(Machine.code == machine_data.code).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Ya existe una máquina con el código '{machine_data.code}'"
        )

    # Crear la máquina
    new_machine = Machine(**machine_data.model_dump())
    db.add(new_machine)
    db.commit()
    db.refresh(new_machine)

    return MachineSchema.model_validate(new_machine)


@router.put("/{machine_id}", response_model=MachineSchema)
def update_machine(
    machine_id: int,
    machine_data: MachineUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_manager)  # Solo managers y admins
):
    """
    Actualizar una máquina existente
    Requiere rol: manager o admin
    """
    machine = db.query(Machine).filter(Machine.id == machine_id).first()

    if not machine:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Máquina con ID {machine_id} no encontrada"
        )

    # Verificar línea de producción si se está actualizando
    if machine_data.production_line_id:
        line = db.query(ProductionLine).filter(
            ProductionLine.id == machine_data.production_line_id
        ).first()
        if not line:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Línea de producción con ID {machine_data.production_line_id} no encontrada"
            )

    # Verificar código único si se está actualizando
    if machine_data.code and machine_data.code != machine.code:
        existing = db.query(Machine).filter(Machine.code == machine_data.code).first()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Ya existe una máquina con el código '{machine_data.code}'"
            )

    # Actualizar campos
    update_data = machine_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(machine, field, value)

    db.commit()
    db.refresh(machine)

    return MachineSchema.model_validate(machine)


@router.delete("/{machine_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_machine(
    machine_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_manager)  # Solo managers y admins
):
    """
    Eliminar (soft delete) una máquina
    Requiere rol: manager o admin
    """
    machine = db.query(Machine).filter(Machine.id == machine_id).first()

    if not machine:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Máquina con ID {machine_id} no encontrada"
        )

    # Soft delete: marcar como inactiva
    machine.is_active = False
    db.commit()

    return None


@router.get("/{machine_id}/stats", response_model=MachineWithStats)
def get_machine_stats(
    machine_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Obtener estadísticas de una máquina (failures, MTTR, MTBF)
    """
    machine = db.query(Machine).filter(Machine.id == machine_id).first()

    if not machine:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Máquina con ID {machine_id} no encontrada"
        )

    machine_dict = MachineSchema.model_validate(machine).model_dump()

    # Agregar información de la línea
    line = db.query(ProductionLine).filter(ProductionLine.id == machine.production_line_id).first()
    if line:
        machine_dict['production_line_code'] = line.name
        machine_dict['production_line_name'] = line.description or line.name

    # TODO: Calcular estadísticas reales cuando exista el modelo Failure
    machine_dict['total_failures'] = 0
    machine_dict['active_failures'] = 0
    machine_dict['mttr'] = None
    machine_dict['mtbf'] = None

    return MachineWithStats(**machine_dict)
