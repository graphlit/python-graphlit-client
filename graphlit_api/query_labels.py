# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class QueryLabels(BaseModel):
    labels: Optional["QueryLabelsLabels"]


class QueryLabelsLabels(BaseModel):
    results: Optional[List[Optional["QueryLabelsLabelsResults"]]]


class QueryLabelsLabelsResults(BaseModel):
    id: str
    name: str
    description: Optional[str]
    creation_date: Any = Field(alias="creationDate")


QueryLabels.model_rebuild()
QueryLabelsLabels.model_rebuild()
