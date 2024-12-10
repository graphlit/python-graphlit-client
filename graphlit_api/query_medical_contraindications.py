# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class QueryMedicalContraindications(BaseModel):
    medical_contraindications: Optional[
        "QueryMedicalContraindicationsMedicalContraindications"
    ] = Field(alias="medicalContraindications")


class QueryMedicalContraindicationsMedicalContraindications(BaseModel):
    results: Optional[
        List[Optional["QueryMedicalContraindicationsMedicalContraindicationsResults"]]
    ]


class QueryMedicalContraindicationsMedicalContraindicationsResults(BaseModel):
    id: str
    name: str
    alternate_names: Optional[List[Optional[str]]] = Field(alias="alternateNames")
    creation_date: Any = Field(alias="creationDate")
    uri: Optional[Any]
    description: Optional[str]
    identifier: Optional[str]
    thing: Optional[str]
    relevance: Optional[float]


QueryMedicalContraindications.model_rebuild()
QueryMedicalContraindicationsMedicalContraindications.model_rebuild()
