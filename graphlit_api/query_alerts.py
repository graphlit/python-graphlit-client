# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    AlertTypes,
    ContentPublishingServiceTypes,
    ContentTypes,
    ElevenLabsModels,
    EntityState,
    FileTypes,
    IntegrationServiceTypes,
    ObservableTypes,
)


class QueryAlerts(BaseModel):
    alerts: Optional["QueryAlertsAlerts"]


class QueryAlertsAlerts(BaseModel):
    results: Optional[List[Optional["QueryAlertsAlertsResults"]]]


class QueryAlertsAlertsResults(BaseModel):
    id: str
    name: str
    creation_date: Any = Field(alias="creationDate")
    owner: "QueryAlertsAlertsResultsOwner"
    state: EntityState
    correlation_id: Optional[str] = Field(alias="correlationId")
    type: AlertTypes
    summary_prompt: Optional[str] = Field(alias="summaryPrompt")
    publish_prompt: str = Field(alias="publishPrompt")
    filter: Optional["QueryAlertsAlertsResultsFilter"]
    integration: "QueryAlertsAlertsResultsIntegration"
    publishing: "QueryAlertsAlertsResultsPublishing"
    summary_specification: Optional["QueryAlertsAlertsResultsSummarySpecification"] = (
        Field(alias="summarySpecification")
    )
    publish_specification: Optional["QueryAlertsAlertsResultsPublishSpecification"] = (
        Field(alias="publishSpecification")
    )
    last_alert_date: Optional[Any] = Field(alias="lastAlertDate")


class QueryAlertsAlertsResultsOwner(BaseModel):
    id: str


class QueryAlertsAlertsResultsFilter(BaseModel):
    date_range: Optional["QueryAlertsAlertsResultsFilterDateRange"] = Field(
        alias="dateRange"
    )
    creation_date_range: Optional["QueryAlertsAlertsResultsFilterCreationDateRange"] = (
        Field(alias="creationDateRange")
    )
    types: Optional[List[ContentTypes]]
    file_types: Optional[List[Optional[FileTypes]]] = Field(alias="fileTypes")
    contents: Optional[List["QueryAlertsAlertsResultsFilterContents"]]
    feeds: Optional[List["QueryAlertsAlertsResultsFilterFeeds"]]
    workflows: Optional[List["QueryAlertsAlertsResultsFilterWorkflows"]]
    collections: Optional[List["QueryAlertsAlertsResultsFilterCollections"]]
    observations: Optional[List["QueryAlertsAlertsResultsFilterObservations"]]


class QueryAlertsAlertsResultsFilterDateRange(BaseModel):
    from_: Optional[Any] = Field(alias="from")
    to: Optional[Any]


class QueryAlertsAlertsResultsFilterCreationDateRange(BaseModel):
    from_: Optional[Any] = Field(alias="from")
    to: Optional[Any]


class QueryAlertsAlertsResultsFilterContents(BaseModel):
    id: str


class QueryAlertsAlertsResultsFilterFeeds(BaseModel):
    id: str


class QueryAlertsAlertsResultsFilterWorkflows(BaseModel):
    id: str


class QueryAlertsAlertsResultsFilterCollections(BaseModel):
    id: str


class QueryAlertsAlertsResultsFilterObservations(BaseModel):
    type: ObservableTypes
    observable: "QueryAlertsAlertsResultsFilterObservationsObservable"
    states: Optional[List[Optional[EntityState]]]


class QueryAlertsAlertsResultsFilterObservationsObservable(BaseModel):
    id: str


class QueryAlertsAlertsResultsIntegration(BaseModel):
    type: IntegrationServiceTypes
    uri: Optional[str]
    slack: Optional["QueryAlertsAlertsResultsIntegrationSlack"]


class QueryAlertsAlertsResultsIntegrationSlack(BaseModel):
    token: str
    channel: str


class QueryAlertsAlertsResultsPublishing(BaseModel):
    type: ContentPublishingServiceTypes
    eleven_labs: Optional["QueryAlertsAlertsResultsPublishingElevenLabs"] = Field(
        alias="elevenLabs"
    )


class QueryAlertsAlertsResultsPublishingElevenLabs(BaseModel):
    model: Optional[ElevenLabsModels]
    voice: Optional[str]


class QueryAlertsAlertsResultsSummarySpecification(BaseModel):
    id: str


class QueryAlertsAlertsResultsPublishSpecification(BaseModel):
    id: str


QueryAlerts.model_rebuild()
QueryAlertsAlerts.model_rebuild()
QueryAlertsAlertsResults.model_rebuild()
QueryAlertsAlertsResultsFilter.model_rebuild()
QueryAlertsAlertsResultsFilterObservations.model_rebuild()
QueryAlertsAlertsResultsIntegration.model_rebuild()
QueryAlertsAlertsResultsPublishing.model_rebuild()
