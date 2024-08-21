# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class CreateMedicalGuideline(BaseModel):
    create_medical_guideline: Optional[
        "CreateMedicalGuidelineCreateMedicalGuideline"
    ] = Field(alias="createMedicalGuideline")


class CreateMedicalGuidelineCreateMedicalGuideline(BaseModel):
    id: str
    name: str


CreateMedicalGuideline.model_rebuild()
