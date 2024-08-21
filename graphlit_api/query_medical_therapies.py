# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class QueryMedicalTherapies(BaseModel):
    medical_therapies: Optional["QueryMedicalTherapiesMedicalTherapies"] = Field(
        alias="medicalTherapies"
    )


class QueryMedicalTherapiesMedicalTherapies(BaseModel):
    results: Optional[List[Optional["QueryMedicalTherapiesMedicalTherapiesResults"]]]


class QueryMedicalTherapiesMedicalTherapiesResults(BaseModel):
    id: str
    name: str
    alternate_names: Optional[List[Optional[str]]] = Field(alias="alternateNames")
    creation_date: Any = Field(alias="creationDate")
    thing: Optional[str]
    relevance: Optional[float]


QueryMedicalTherapies.model_rebuild()
QueryMedicalTherapiesMedicalTherapies.model_rebuild()
