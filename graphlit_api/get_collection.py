# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import CollectionTypes, EntityState


class GetCollection(BaseModel):
    collection: Optional["GetCollectionCollection"]


class GetCollectionCollection(BaseModel):
    id: str
    name: str
    creation_date: Any = Field(alias="creationDate")
    owner: "GetCollectionCollectionOwner"
    state: EntityState
    type: Optional[CollectionTypes]
    contents: Optional[List[Optional["GetCollectionCollectionContents"]]]


class GetCollectionCollectionOwner(BaseModel):
    id: str


class GetCollectionCollectionContents(BaseModel):
    id: str
    name: str


GetCollection.model_rebuild()
GetCollectionCollection.model_rebuild()