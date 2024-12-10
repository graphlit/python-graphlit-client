# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class QueryMedicalStudies(BaseModel):
    medical_studies: Optional["QueryMedicalStudiesMedicalStudies"] = Field(
        alias="medicalStudies"
    )


class QueryMedicalStudiesMedicalStudies(BaseModel):
    results: Optional[List[Optional["QueryMedicalStudiesMedicalStudiesResults"]]]


class QueryMedicalStudiesMedicalStudiesResults(BaseModel):
    id: str
    name: str
    alternate_names: Optional[List[Optional[str]]] = Field(alias="alternateNames")
    creation_date: Any = Field(alias="creationDate")
    uri: Optional[Any]
    description: Optional[str]
    identifier: Optional[str]
    thing: Optional[str]
    relevance: Optional[float]
    address: Optional["QueryMedicalStudiesMedicalStudiesResultsAddress"]


class QueryMedicalStudiesMedicalStudiesResultsAddress(BaseModel):
    street_address: Optional[str] = Field(alias="streetAddress")
    city: Optional[str]
    region: Optional[str]
    country: Optional[str]
    postal_code: Optional[str] = Field(alias="postalCode")


QueryMedicalStudies.model_rebuild()
QueryMedicalStudiesMedicalStudies.model_rebuild()
QueryMedicalStudiesMedicalStudiesResults.model_rebuild()
