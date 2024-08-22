# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class QueryMedicalIndications(BaseModel):
    medical_indications: Optional["QueryMedicalIndicationsMedicalIndications"] = Field(
        alias="medicalIndications"
    )


class QueryMedicalIndicationsMedicalIndications(BaseModel):
    results: Optional[
        List[Optional["QueryMedicalIndicationsMedicalIndicationsResults"]]
    ]


class QueryMedicalIndicationsMedicalIndicationsResults(BaseModel):
    id: str
    name: str
    alternate_names: Optional[List[Optional[str]]] = Field(alias="alternateNames")
    creation_date: Any = Field(alias="creationDate")
    thing: Optional[str]
    relevance: Optional[float]


QueryMedicalIndications.model_rebuild()
QueryMedicalIndicationsMedicalIndications.model_rebuild()