# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class SearchWeb(BaseModel):
    search_web: Optional["SearchWebSearchWeb"] = Field(alias="searchWeb")


class SearchWebSearchWeb(BaseModel):
    results: Optional[List["SearchWebSearchWebResults"]]


class SearchWebSearchWebResults(BaseModel):
    uri: Any
    text: Optional[str]
    title: Optional[str]
    score: Optional[float]


SearchWeb.model_rebuild()
SearchWebSearchWeb.model_rebuild()
