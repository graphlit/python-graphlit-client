# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import BillableMetrics, ContentTypes, EntityTypes, FileTypes


class Usage(BaseModel):
    usage: Optional[List[Optional["UsageUsage"]]]


class UsageUsage(BaseModel):
    correlation_id: Optional[str] = Field(alias="correlationId")
    date: Any
    credits: Optional[Any]
    name: str
    metric: Optional[BillableMetrics]
    workflow: Optional[str]
    entity_type: Optional[EntityTypes] = Field(alias="entityType")
    entity_id: Optional[str] = Field(alias="entityId")
    project_id: str = Field(alias="projectId")
    owner_id: str = Field(alias="ownerId")
    uri: Optional[str]
    duration: Optional[Any]
    throughput: Optional[float]
    content_type: Optional[ContentTypes] = Field(alias="contentType")
    file_type: Optional[FileTypes] = Field(alias="fileType")
    model_service: Optional[str] = Field(alias="modelService")
    model_name: Optional[str] = Field(alias="modelName")
    processor_name: Optional[str] = Field(alias="processorName")
    prompt: Optional[str]
    prompt_tokens: Optional[int] = Field(alias="promptTokens")
    completion: Optional[str]
    completion_tokens: Optional[int] = Field(alias="completionTokens")
    tokens: Optional[int]
    count: Optional[int]
    request: Optional[str]
    variables: Optional[str]
    response: Optional[str]


Usage.model_rebuild()
