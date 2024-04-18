# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import CollectionTypes, EntityState


class CreateCollection(BaseModel):
    create_collection: Optional["CreateCollectionCreateCollection"] = Field(
        alias="createCollection"
    )


class CreateCollectionCreateCollection(BaseModel):
    id: str
    name: str
    state: EntityState
    type: Optional[CollectionTypes]


CreateCollection.model_rebuild()
