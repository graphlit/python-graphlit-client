# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import ContentTypes, EntityState, FileTypes


class PublishContents(BaseModel):
    publish_contents: Optional["PublishContentsPublishContents"] = Field(
        alias="publishContents"
    )


class PublishContentsPublishContents(BaseModel):
    id: str
    name: str
    state: EntityState
    type: Optional[ContentTypes]
    file_type: Optional[FileTypes] = Field(alias="fileType")
    mime_type: Optional[str] = Field(alias="mimeType")
    uri: Optional[Any]
    text_uri: Optional[Any] = Field(alias="textUri")
    audio_uri: Optional[Any] = Field(alias="audioUri")
    markdown: Optional[str]


PublishContents.model_rebuild()
