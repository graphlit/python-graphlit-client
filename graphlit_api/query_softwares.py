# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class QuerySoftwares(BaseModel):
    softwares: Optional["QuerySoftwaresSoftwares"]


class QuerySoftwaresSoftwares(BaseModel):
    results: Optional[List[Optional["QuerySoftwaresSoftwaresResults"]]]


class QuerySoftwaresSoftwaresResults(BaseModel):
    id: str
    name: str
    alternate_names: Optional[List[Optional[str]]] = Field(alias="alternateNames")
    creation_date: Any = Field(alias="creationDate")
    thing: Optional[str]
    release_date: Optional[Any] = Field(alias="releaseDate")
    developer: Optional[str]


QuerySoftwares.model_rebuild()
QuerySoftwaresSoftwares.model_rebuild()
