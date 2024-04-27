# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class QueryPlaces(BaseModel):
    places: Optional["QueryPlacesPlaces"]


class QueryPlacesPlaces(BaseModel):
    results: Optional[List[Optional["QueryPlacesPlacesResults"]]]


class QueryPlacesPlacesResults(BaseModel):
    id: str
    name: str
    alternate_names: Optional[List[Optional[str]]] = Field(alias="alternateNames")
    creation_date: Any = Field(alias="creationDate")
    address: Optional["QueryPlacesPlacesResultsAddress"]


class QueryPlacesPlacesResultsAddress(BaseModel):
    street_address: Optional[str] = Field(alias="streetAddress")
    city: Optional[str]
    region: Optional[str]
    country: Optional[str]
    postal_code: Optional[str] = Field(alias="postalCode")


QueryPlaces.model_rebuild()
QueryPlacesPlaces.model_rebuild()
QueryPlacesPlacesResults.model_rebuild()
