# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import SummarizationTypes


class SummarizeText(BaseModel):
    summarize_text: Optional["SummarizeTextSummarizeText"] = Field(
        alias="summarizeText"
    )


class SummarizeTextSummarizeText(BaseModel):
    specification: Optional["SummarizeTextSummarizeTextSpecification"]
    content: Optional["SummarizeTextSummarizeTextContent"]
    type: SummarizationTypes
    items: Optional[List["SummarizeTextSummarizeTextItems"]]
    error: Optional[str]


class SummarizeTextSummarizeTextSpecification(BaseModel):
    id: str


class SummarizeTextSummarizeTextContent(BaseModel):
    id: str


class SummarizeTextSummarizeTextItems(BaseModel):
    text: Optional[str]
    tokens: int
    summarization_time: Optional[Any] = Field(alias="summarizationTime")


SummarizeText.model_rebuild()
SummarizeTextSummarizeText.model_rebuild()
