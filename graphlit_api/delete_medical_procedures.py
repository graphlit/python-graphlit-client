# Generated by ariadne-codegen
# Source: ./documents

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteMedicalProcedures(BaseModel):
    delete_medical_procedures: Optional[
        List[Optional["DeleteMedicalProceduresDeleteMedicalProcedures"]]
    ] = Field(alias="deleteMedicalProcedures")


class DeleteMedicalProceduresDeleteMedicalProcedures(BaseModel):
    id: str
    state: EntityState


DeleteMedicalProcedures.model_rebuild()
