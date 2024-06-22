# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class QueryOrganizations(BaseModel):
    organizations: Optional["QueryOrganizationsOrganizations"]


class QueryOrganizationsOrganizations(BaseModel):
    results: Optional[List[Optional["QueryOrganizationsOrganizationsResults"]]]


class QueryOrganizationsOrganizationsResults(BaseModel):
    id: str
    name: str
    alternate_names: Optional[List[Optional[str]]] = Field(alias="alternateNames")
    creation_date: Any = Field(alias="creationDate")
    thing: Optional[str]
    relevance: Optional[float]
    address: Optional["QueryOrganizationsOrganizationsResultsAddress"]
    founding_date: Optional[Any] = Field(alias="foundingDate")
    industries: Optional[List[Optional[str]]]
    revenue: Optional[Any]
    revenue_currency: Optional[str] = Field(alias="revenueCurrency")
    investment: Optional[Any]
    investment_currency: Optional[str] = Field(alias="investmentCurrency")


class QueryOrganizationsOrganizationsResultsAddress(BaseModel):
    street_address: Optional[str] = Field(alias="streetAddress")
    city: Optional[str]
    region: Optional[str]
    country: Optional[str]
    postal_code: Optional[str] = Field(alias="postalCode")


QueryOrganizations.model_rebuild()
QueryOrganizationsOrganizations.model_rebuild()
QueryOrganizationsOrganizationsResults.model_rebuild()
