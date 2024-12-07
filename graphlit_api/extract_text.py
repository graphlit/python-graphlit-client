# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class ExtractText(BaseModel):
    extract_text: Optional[List[Optional["ExtractTextExtractText"]]] = Field(
        alias="extractText"
    )


class ExtractTextExtractText(BaseModel):
    specification: Optional["ExtractTextExtractTextSpecification"]
    content: Optional["ExtractTextExtractTextContent"]
    name: str
    value: str
    start_time: Optional[Any] = Field(alias="startTime")
    end_time: Optional[Any] = Field(alias="endTime")
    page_number: Optional[int] = Field(alias="pageNumber")
    error: Optional[str]


class ExtractTextExtractTextSpecification(BaseModel):
    id: str


class ExtractTextExtractTextContent(BaseModel):
    id: str


ExtractText.model_rebuild()
ExtractTextExtractText.model_rebuild()
