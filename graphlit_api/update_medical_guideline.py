# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class UpdateMedicalGuideline(BaseModel):
    update_medical_guideline: Optional[
        "UpdateMedicalGuidelineUpdateMedicalGuideline"
    ] = Field(alias="updateMedicalGuideline")


class UpdateMedicalGuidelineUpdateMedicalGuideline(BaseModel):
    id: str
    name: str


UpdateMedicalGuideline.model_rebuild()
