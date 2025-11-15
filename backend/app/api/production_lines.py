from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.core.dependencies import get_db, get_current_active_user, require_manager
from app.models.user import User
from app.models.production_line import ProductionLine as ProductionLineModel
from app.schemas import (
    ProductionLine, ProductionLineCreate, ProductionLineUpdate,
    ProductionLineWithStats
)

router = APIRouter(prefix="/lines", tags=["production-lines"])


@router.get("/", response_model=List[ProductionLine])
def get_production_lines(
    skip: int = 0,
    limit: int = 100,
    include_inactive: bool = False,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Obtener lista de líneas de producción
    """
    query = db.query(ProductionLineModel)

    if not include_inactive:
        query = query.filter(ProductionLineModel.is_active == True)

    lines = query.offset(skip).limit(limit).all()
    return lines


@router.get("/{line_id}", response_model=ProductionLine)
def get_production_line(
    line_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Obtener una línea de producción por ID
    """
    line = db.query(ProductionLineModel).filter(ProductionLineModel.id == line_id).first()

    if not line:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Línea de producción no encontrada"
        )

    return line


@router.post("/", response_model=ProductionLine, status_code=status.HTTP_201_CREATED)
def create_production_line(
    line_create: ProductionLineCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_manager)
):
    """
    Crear una nueva línea de producción
    Requiere rol de manager o admin
    """
    # Verificar si el código ya existe
    existing_line = db.query(ProductionLineModel).filter(
        ProductionLineModel.code == line_create.code
    ).first()

    if existing_line:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe una línea con este código"
        )

    db_line = ProductionLineModel(**line_create.model_dump())
    db.add(db_line)
    db.commit()
    db.refresh(db_line)

    return db_line


@router.put("/{line_id}", response_model=ProductionLine)
def update_production_line(
    line_id: UUID,
    line_update: ProductionLineUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_manager)
):
    """
    Actualizar una línea de producción
    Requiere rol de manager o admin
    """
    db_line = db.query(ProductionLineModel).filter(ProductionLineModel.id == line_id).first()

    if not db_line:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Línea de producción no encontrada"
        )

    # Actualizar solo los campos proporcionados
    update_data = line_update.model_dump(exclude_unset=True)

    # Si se actualiza el código, verificar que no exista
    if "code" in update_data and update_data["code"] != db_line.code:
        existing_line = db.query(ProductionLineModel).filter(
            ProductionLineModel.code == update_data["code"]
        ).first()

        if existing_line:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe una línea con este código"
            )

    for field, value in update_data.items():
        setattr(db_line, field, value)

    db.commit()
    db.refresh(db_line)

    return db_line


@router.delete("/{line_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_production_line(
    line_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_manager)
):
    """
    Eliminar (desactivar) una línea de producción
    Requiere rol de manager o admin
    """
    db_line = db.query(ProductionLineModel).filter(ProductionLineModel.id == line_id).first()

    if not db_line:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Línea de producción no encontrada"
        )

    # Soft delete - solo marcar como inactiva
    db_line.is_active = False
    db.commit()

    return None
