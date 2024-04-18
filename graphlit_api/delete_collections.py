# Generated by ariadne-codegen
# Source: ./documents

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteCollections(BaseModel):
    delete_collections: Optional[
        List[Optional["DeleteCollectionsDeleteCollections"]]
    ] = Field(alias="deleteCollections")


class DeleteCollectionsDeleteCollections(BaseModel):
    id: str
    state: EntityState


DeleteCollections.model_rebuild()
