# Generated by ariadne-codegen
# Source: ./documents

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteMedicalDrugs(BaseModel):
    delete_medical_drugs: Optional[
        List[Optional["DeleteMedicalDrugsDeleteMedicalDrugs"]]
    ] = Field(alias="deleteMedicalDrugs")


class DeleteMedicalDrugsDeleteMedicalDrugs(BaseModel):
    id: str
    state: EntityState


DeleteMedicalDrugs.model_rebuild()