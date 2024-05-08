# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class UpdateOrganization(BaseModel):
    update_organization: Optional["UpdateOrganizationUpdateOrganization"] = Field(
        alias="updateOrganization"
    )


class UpdateOrganizationUpdateOrganization(BaseModel):
    id: str
    name: str


UpdateOrganization.model_rebuild()