# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    AzureDocumentIntelligenceModels,
    ContentTypes,
    DeepgramModels,
    EntityEnrichmentServiceTypes,
    EntityExtractionServiceTypes,
    EntityState,
    FilePreparationServiceTypes,
    FileTypes,
    IntegrationServiceTypes,
    LinkTypes,
    ObservableTypes,
    OpenAIVisionDetailLevels,
    SummarizationTypes,
)


class GetWorkflow(BaseModel):
    workflow: Optional["GetWorkflowWorkflow"]


class GetWorkflowWorkflow(BaseModel):
    id: str
    name: str
    creation_date: Any = Field(alias="creationDate")
    owner: "GetWorkflowWorkflowOwner"
    state: EntityState
    ingestion: Optional["GetWorkflowWorkflowIngestion"]
    preparation: Optional["GetWorkflowWorkflowPreparation"]
    extraction: Optional["GetWorkflowWorkflowExtraction"]
    enrichment: Optional["GetWorkflowWorkflowEnrichment"]
    actions: Optional[List[Optional["GetWorkflowWorkflowActions"]]]


class GetWorkflowWorkflowOwner(BaseModel):
    id: str


class GetWorkflowWorkflowIngestion(BaseModel):
    if_: Optional["GetWorkflowWorkflowIngestionIf"] = Field(alias="if")
    collections: Optional[List[Optional["GetWorkflowWorkflowIngestionCollections"]]]


class GetWorkflowWorkflowIngestionIf(BaseModel):
    types: Optional[List[ContentTypes]]
    file_types: Optional[List[FileTypes]] = Field(alias="fileTypes")


class GetWorkflowWorkflowIngestionCollections(BaseModel):
    id: str


class GetWorkflowWorkflowPreparation(BaseModel):
    disable_smart_capture: Optional[bool] = Field(alias="disableSmartCapture")
    summarizations: Optional[
        List[Optional["GetWorkflowWorkflowPreparationSummarizations"]]
    ]
    jobs: Optional[List[Optional["GetWorkflowWorkflowPreparationJobs"]]]


class GetWorkflowWorkflowPreparationSummarizations(BaseModel):
    type: SummarizationTypes
    specification: Optional["GetWorkflowWorkflowPreparationSummarizationsSpecification"]
    tokens: Optional[int]
    items: Optional[int]


class GetWorkflowWorkflowPreparationSummarizationsSpecification(BaseModel):
    id: str


class GetWorkflowWorkflowPreparationJobs(BaseModel):
    connector: Optional["GetWorkflowWorkflowPreparationJobsConnector"]


class GetWorkflowWorkflowPreparationJobsConnector(BaseModel):
    type: FilePreparationServiceTypes
    file_types: Optional[List[FileTypes]] = Field(alias="fileTypes")
    azure_document: Optional[
        "GetWorkflowWorkflowPreparationJobsConnectorAzureDocument"
    ] = Field(alias="azureDocument")
    deepgram: Optional["GetWorkflowWorkflowPreparationJobsConnectorDeepgram"]
    document: Optional["GetWorkflowWorkflowPreparationJobsConnectorDocument"]
    email: Optional["GetWorkflowWorkflowPreparationJobsConnectorEmail"]


class GetWorkflowWorkflowPreparationJobsConnectorAzureDocument(BaseModel):
    model: Optional[AzureDocumentIntelligenceModels]


class GetWorkflowWorkflowPreparationJobsConnectorDeepgram(BaseModel):
    model: Optional[DeepgramModels]
    key: Optional[str]
    enable_redaction: Optional[bool] = Field(alias="enableRedaction")
    enable_speaker_diarization: Optional[bool] = Field(alias="enableSpeakerDiarization")


class GetWorkflowWorkflowPreparationJobsConnectorDocument(BaseModel):
    include_images: Optional[bool] = Field(alias="includeImages")


class GetWorkflowWorkflowPreparationJobsConnectorEmail(BaseModel):
    include_attachments: Optional[bool] = Field(alias="includeAttachments")


class GetWorkflowWorkflowExtraction(BaseModel):
    jobs: Optional[List[Optional["GetWorkflowWorkflowExtractionJobs"]]]


class GetWorkflowWorkflowExtractionJobs(BaseModel):
    connector: Optional["GetWorkflowWorkflowExtractionJobsConnector"]


class GetWorkflowWorkflowExtractionJobsConnector(BaseModel):
    type: EntityExtractionServiceTypes
    content_types: Optional[List[ContentTypes]] = Field(alias="contentTypes")
    file_types: Optional[List[FileTypes]] = Field(alias="fileTypes")
    extracted_types: Optional[List[ObservableTypes]] = Field(alias="extractedTypes")
    extracted_count: Optional[int] = Field(alias="extractedCount")
    azure_text: Optional["GetWorkflowWorkflowExtractionJobsConnectorAzureText"] = Field(
        alias="azureText"
    )
    azure_image: Optional["GetWorkflowWorkflowExtractionJobsConnectorAzureImage"] = (
        Field(alias="azureImage")
    )
    open_ai_image: Optional["GetWorkflowWorkflowExtractionJobsConnectorOpenAiImage"] = (
        Field(alias="openAIImage")
    )
    model_text: Optional["GetWorkflowWorkflowExtractionJobsConnectorModelText"] = Field(
        alias="modelText"
    )


class GetWorkflowWorkflowExtractionJobsConnectorAzureText(BaseModel):
    confidence_threshold: Optional[float] = Field(alias="confidenceThreshold")
    enable_pii: Optional[bool] = Field(alias="enablePII")


class GetWorkflowWorkflowExtractionJobsConnectorAzureImage(BaseModel):
    confidence_threshold: Optional[float] = Field(alias="confidenceThreshold")


class GetWorkflowWorkflowExtractionJobsConnectorOpenAiImage(BaseModel):
    confidence_threshold: Optional[float] = Field(alias="confidenceThreshold")
    detail_level: Optional[OpenAIVisionDetailLevels] = Field(alias="detailLevel")
    custom_instructions: Optional[str] = Field(alias="customInstructions")


class GetWorkflowWorkflowExtractionJobsConnectorModelText(BaseModel):
    specification: Optional[
        "GetWorkflowWorkflowExtractionJobsConnectorModelTextSpecification"
    ]


class GetWorkflowWorkflowExtractionJobsConnectorModelTextSpecification(BaseModel):
    id: str


class GetWorkflowWorkflowEnrichment(BaseModel):
    link: Optional["GetWorkflowWorkflowEnrichmentLink"]
    jobs: Optional[List[Optional["GetWorkflowWorkflowEnrichmentJobs"]]]


class GetWorkflowWorkflowEnrichmentLink(BaseModel):
    enable_crawling: Optional[bool] = Field(alias="enableCrawling")
    allowed_domains: Optional[List[str]] = Field(alias="allowedDomains")
    excluded_domains: Optional[List[str]] = Field(alias="excludedDomains")
    allowed_links: Optional[List[LinkTypes]] = Field(alias="allowedLinks")
    excluded_links: Optional[List[LinkTypes]] = Field(alias="excludedLinks")
    allowed_files: Optional[List[FileTypes]] = Field(alias="allowedFiles")
    excluded_files: Optional[List[FileTypes]] = Field(alias="excludedFiles")
    allow_content_domain: Optional[bool] = Field(alias="allowContentDomain")
    maximum_links: Optional[int] = Field(alias="maximumLinks")


class GetWorkflowWorkflowEnrichmentJobs(BaseModel):
    connector: Optional["GetWorkflowWorkflowEnrichmentJobsConnector"]


class GetWorkflowWorkflowEnrichmentJobsConnector(BaseModel):
    type: Optional[EntityEnrichmentServiceTypes]
    enriched_types: Optional[List[Optional[ObservableTypes]]] = Field(
        alias="enrichedTypes"
    )


class GetWorkflowWorkflowActions(BaseModel):
    connector: Optional["GetWorkflowWorkflowActionsConnector"]


class GetWorkflowWorkflowActionsConnector(BaseModel):
    type: IntegrationServiceTypes
    uri: Optional[str]
    slack: Optional["GetWorkflowWorkflowActionsConnectorSlack"]


class GetWorkflowWorkflowActionsConnectorSlack(BaseModel):
    token: str
    channel: str


GetWorkflow.model_rebuild()
GetWorkflowWorkflow.model_rebuild()
GetWorkflowWorkflowIngestion.model_rebuild()
GetWorkflowWorkflowPreparation.model_rebuild()
GetWorkflowWorkflowPreparationSummarizations.model_rebuild()
GetWorkflowWorkflowPreparationJobs.model_rebuild()
GetWorkflowWorkflowPreparationJobsConnector.model_rebuild()
GetWorkflowWorkflowExtraction.model_rebuild()
GetWorkflowWorkflowExtractionJobs.model_rebuild()
GetWorkflowWorkflowExtractionJobsConnector.model_rebuild()
GetWorkflowWorkflowExtractionJobsConnectorModelText.model_rebuild()
GetWorkflowWorkflowEnrichment.model_rebuild()
GetWorkflowWorkflowEnrichmentJobs.model_rebuild()
GetWorkflowWorkflowActions.model_rebuild()
GetWorkflowWorkflowActionsConnector.model_rebuild()
