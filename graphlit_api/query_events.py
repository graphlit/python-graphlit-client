# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class QueryEvents(BaseModel):
    events: Optional["QueryEventsEvents"]


class QueryEventsEvents(BaseModel):
    results: Optional[List[Optional["QueryEventsEventsResults"]]]


class QueryEventsEventsResults(BaseModel):
    id: str
    name: str
    alternate_names: Optional[List[Optional[str]]] = Field(alias="alternateNames")
    creation_date: Any = Field(alias="creationDate")
    address: Optional["QueryEventsEventsResultsAddress"]
    start_date: Optional[Any] = Field(alias="startDate")
    end_date: Optional[Any] = Field(alias="endDate")
    availability_start_date: Optional[Any] = Field(alias="availabilityStartDate")
    availability_end_date: Optional[Any] = Field(alias="availabilityEndDate")
    price: Optional[Any]
    min_price: Optional[Any] = Field(alias="minPrice")
    max_price: Optional[Any] = Field(alias="maxPrice")
    price_currency: Optional[str] = Field(alias="priceCurrency")
    is_accessible_for_free: Optional[bool] = Field(alias="isAccessibleForFree")
    typical_age_range: Optional[str] = Field(alias="typicalAgeRange")


class QueryEventsEventsResultsAddress(BaseModel):
    street_address: Optional[str] = Field(alias="streetAddress")
    city: Optional[str]
    region: Optional[str]
    country: Optional[str]
    postal_code: Optional[str] = Field(alias="postalCode")


QueryEvents.model_rebuild()
QueryEventsEvents.model_rebuild()
QueryEventsEventsResults.model_rebuild()