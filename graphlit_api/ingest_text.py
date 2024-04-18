# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import ContentTypes, EntityState, FileTypes


class IngestText(BaseModel):
    ingest_text: Optional["IngestTextIngestText"] = Field(alias="ingestText")


class IngestTextIngestText(BaseModel):
    id: str
    name: str
    state: EntityState
    type: Optional[ContentTypes]
    file_type: Optional[FileTypes] = Field(alias="fileType")
    mime_type: Optional[str] = Field(alias="mimeType")
    uri: Optional[Any]


IngestText.model_rebuild()
