# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    ContentTypes,
    EntityState,
    FileTypes,
    ObservableTypes,
    OccurrenceTypes,
)


class UpdateContent(BaseModel):
    update_content: Optional["UpdateContentUpdateContent"] = Field(
        alias="updateContent"
    )


class UpdateContentUpdateContent(BaseModel):
    id: str
    name: str
    state: EntityState
    type: Optional[ContentTypes]
    file_type: Optional[FileTypes] = Field(alias="fileType")
    mime_type: Optional[str] = Field(alias="mimeType")
    uri: Optional[Any]
    collections: Optional[List[Optional["UpdateContentUpdateContentCollections"]]]
    observations: Optional[List[Optional["UpdateContentUpdateContentObservations"]]]


class UpdateContentUpdateContentCollections(BaseModel):
    id: str
    name: str


class UpdateContentUpdateContentObservations(BaseModel):
    id: str
    type: ObservableTypes
    observable: "UpdateContentUpdateContentObservationsObservable"
    related: Optional["UpdateContentUpdateContentObservationsRelated"]
    related_type: Optional[ObservableTypes] = Field(alias="relatedType")
    relation: Optional[str]
    occurrences: Optional[
        List[Optional["UpdateContentUpdateContentObservationsOccurrences"]]
    ]
    state: EntityState


class UpdateContentUpdateContentObservationsObservable(BaseModel):
    id: str
    name: Optional[str]


class UpdateContentUpdateContentObservationsRelated(BaseModel):
    id: str
    name: Optional[str]


class UpdateContentUpdateContentObservationsOccurrences(BaseModel):
    type: Optional[OccurrenceTypes]
    confidence: Optional[float]
    start_time: Optional[Any] = Field(alias="startTime")
    end_time: Optional[Any] = Field(alias="endTime")
    page_index: Optional[int] = Field(alias="pageIndex")
    bounding_box: Optional[
        "UpdateContentUpdateContentObservationsOccurrencesBoundingBox"
    ] = Field(alias="boundingBox")


class UpdateContentUpdateContentObservationsOccurrencesBoundingBox(BaseModel):
    left: Optional[float]
    top: Optional[float]
    width: Optional[float]
    height: Optional[float]


UpdateContent.model_rebuild()
UpdateContentUpdateContent.model_rebuild()
UpdateContentUpdateContentObservations.model_rebuild()
UpdateContentUpdateContentObservationsOccurrences.model_rebuild()
