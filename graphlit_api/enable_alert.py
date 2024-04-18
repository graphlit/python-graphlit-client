# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class EnableAlert(BaseModel):
    enable_alert: Optional["EnableAlertEnableAlert"] = Field(alias="enableAlert")


class EnableAlertEnableAlert(BaseModel):
    id: str
    state: EntityState


EnableAlert.model_rebuild()