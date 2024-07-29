# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    AzureDocumentIntelligenceModels,
    AzureDocumentIntelligenceVersions,
    ContentIndexingServiceTypes,
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


class UpdateWorkflow(BaseModel):
    update_workflow: Optional["UpdateWorkflowUpdateWorkflow"] = Field(
        alias="updateWorkflow"
    )


class UpdateWorkflowUpdateWorkflow(BaseModel):
    id: str
    name: str
    state: EntityState
    ingestion: Optional["UpdateWorkflowUpdateWorkflowIngestion"]
    indexing: Optional["UpdateWorkflowUpdateWorkflowIndexing"]
    preparation: Optional["UpdateWorkflowUpdateWorkflowPreparation"]
    extraction: Optional["UpdateWorkflowUpdateWorkflowExtraction"]
    enrichment: Optional["UpdateWorkflowUpdateWorkflowEnrichment"]
    storage: Optional["UpdateWorkflowUpdateWorkflowStorage"]
    actions: Optional[List[Optional["UpdateWorkflowUpdateWorkflowActions"]]]


class UpdateWorkflowUpdateWorkflowIngestion(BaseModel):
    if_: Optional["UpdateWorkflowUpdateWorkflowIngestionIf"] = Field(alias="if")
    collections: Optional[
        List[Optional["UpdateWorkflowUpdateWorkflowIngestionCollections"]]
    ]


class UpdateWorkflowUpdateWorkflowIngestionIf(BaseModel):
    types: Optional[List[ContentTypes]]
    file_types: Optional[List[FileTypes]] = Field(alias="fileTypes")
    allowed_paths: Optional[List[str]] = Field(alias="allowedPaths")
    excluded_paths: Optional[List[str]] = Field(alias="excludedPaths")


class UpdateWorkflowUpdateWorkflowIngestionCollections(BaseModel):
    id: str


class UpdateWorkflowUpdateWorkflowIndexing(BaseModel):
    jobs: Optional[List[Optional["UpdateWorkflowUpdateWorkflowIndexingJobs"]]]


class UpdateWorkflowUpdateWorkflowIndexingJobs(BaseModel):
    connector: Optional["UpdateWorkflowUpdateWorkflowIndexingJobsConnector"]


class UpdateWorkflowUpdateWorkflowIndexingJobsConnector(BaseModel):
    type: Optional[ContentIndexingServiceTypes]
    content_type: Optional[ContentTypes] = Field(alias="contentType")
    file_type: Optional[FileTypes] = Field(alias="fileType")


class UpdateWorkflowUpdateWorkflowPreparation(BaseModel):
    disable_smart_capture: Optional[bool] = Field(alias="disableSmartCapture")
    summarizations: Optional[
        List[Optional["UpdateWorkflowUpdateWorkflowPreparationSummarizations"]]
    ]
    jobs: Optional[List[Optional["UpdateWorkflowUpdateWorkflowPreparationJobs"]]]


class UpdateWorkflowUpdateWorkflowPreparationSummarizations(BaseModel):
    type: SummarizationTypes
    specification: Optional[
        "UpdateWorkflowUpdateWorkflowPreparationSummarizationsSpecification"
    ]
    tokens: Optional[int]
    items: Optional[int]
    prompt: Optional[str]


class UpdateWorkflowUpdateWorkflowPreparationSummarizationsSpecification(BaseModel):
    id: str


class UpdateWorkflowUpdateWorkflowPreparationJobs(BaseModel):
    connector: Optional["UpdateWorkflowUpdateWorkflowPreparationJobsConnector"]


class UpdateWorkflowUpdateWorkflowPreparationJobsConnector(BaseModel):
    type: FilePreparationServiceTypes
    file_types: Optional[List[FileTypes]] = Field(alias="fileTypes")
    azure_document: Optional[
        "UpdateWorkflowUpdateWorkflowPreparationJobsConnectorAzureDocument"
    ] = Field(alias="azureDocument")
    deepgram: Optional["UpdateWorkflowUpdateWorkflowPreparationJobsConnectorDeepgram"]
    document: Optional["UpdateWorkflowUpdateWorkflowPreparationJobsConnectorDocument"]
    email: Optional["UpdateWorkflowUpdateWorkflowPreparationJobsConnectorEmail"]


class UpdateWorkflowUpdateWorkflowPreparationJobsConnectorAzureDocument(BaseModel):
    version: Optional[AzureDocumentIntelligenceVersions]
    model: Optional[AzureDocumentIntelligenceModels]
    endpoint: Optional[Any]
    key: Optional[str]


class UpdateWorkflowUpdateWorkflowPreparationJobsConnectorDeepgram(BaseModel):
    model: Optional[DeepgramModels]
    key: Optional[str]
    enable_redaction: Optional[bool] = Field(alias="enableRedaction")
    enable_speaker_diarization: Optional[bool] = Field(alias="enableSpeakerDiarization")


class UpdateWorkflowUpdateWorkflowPreparationJobsConnectorDocument(BaseModel):
    include_images: Optional[bool] = Field(alias="includeImages")


class UpdateWorkflowUpdateWorkflowPreparationJobsConnectorEmail(BaseModel):
    include_attachments: Optional[bool] = Field(alias="includeAttachments")


class UpdateWorkflowUpdateWorkflowExtraction(BaseModel):
    jobs: Optional[List[Optional["UpdateWorkflowUpdateWorkflowExtractionJobs"]]]


class UpdateWorkflowUpdateWorkflowExtractionJobs(BaseModel):
    connector: Optional["UpdateWorkflowUpdateWorkflowExtractionJobsConnector"]


class UpdateWorkflowUpdateWorkflowExtractionJobsConnector(BaseModel):
    type: EntityExtractionServiceTypes
    content_types: Optional[List[ContentTypes]] = Field(alias="contentTypes")
    file_types: Optional[List[FileTypes]] = Field(alias="fileTypes")
    extracted_types: Optional[List[ObservableTypes]] = Field(alias="extractedTypes")
    extracted_count: Optional[int] = Field(alias="extractedCount")
    azure_text: Optional[
        "UpdateWorkflowUpdateWorkflowExtractionJobsConnectorAzureText"
    ] = Field(alias="azureText")
    azure_image: Optional[
        "UpdateWorkflowUpdateWorkflowExtractionJobsConnectorAzureImage"
    ] = Field(alias="azureImage")
    open_ai_image: Optional[
        "UpdateWorkflowUpdateWorkflowExtractionJobsConnectorOpenAiImage"
    ] = Field(alias="openAIImage")
    model_image: Optional[
        "UpdateWorkflowUpdateWorkflowExtractionJobsConnectorModelImage"
    ] = Field(alias="modelImage")
    model_text: Optional[
        "UpdateWorkflowUpdateWorkflowExtractionJobsConnectorModelText"
    ] = Field(alias="modelText")


class UpdateWorkflowUpdateWorkflowExtractionJobsConnectorAzureText(BaseModel):
    confidence_threshold: Optional[float] = Field(alias="confidenceThreshold")
    enable_pii: Optional[bool] = Field(alias="enablePII")


class UpdateWorkflowUpdateWorkflowExtractionJobsConnectorAzureImage(BaseModel):
    confidence_threshold: Optional[float] = Field(alias="confidenceThreshold")


class UpdateWorkflowUpdateWorkflowExtractionJobsConnectorOpenAiImage(BaseModel):
    confidence_threshold: Optional[float] = Field(alias="confidenceThreshold")
    detail_level: Optional[OpenAIVisionDetailLevels] = Field(alias="detailLevel")
    custom_instructions: Optional[str] = Field(alias="customInstructions")


class UpdateWorkflowUpdateWorkflowExtractionJobsConnectorModelImage(BaseModel):
    specification: Optional[
        "UpdateWorkflowUpdateWorkflowExtractionJobsConnectorModelImageSpecification"
    ]


class UpdateWorkflowUpdateWorkflowExtractionJobsConnectorModelImageSpecification(
    BaseModel
):
    id: str


class UpdateWorkflowUpdateWorkflowExtractionJobsConnectorModelText(BaseModel):
    specification: Optional[
        "UpdateWorkflowUpdateWorkflowExtractionJobsConnectorModelTextSpecification"
    ]


class UpdateWorkflowUpdateWorkflowExtractionJobsConnectorModelTextSpecification(
    BaseModel
):
    id: str


class UpdateWorkflowUpdateWorkflowEnrichment(BaseModel):
    link: Optional["UpdateWorkflowUpdateWorkflowEnrichmentLink"]
    jobs: Optional[List[Optional["UpdateWorkflowUpdateWorkflowEnrichmentJobs"]]]


class UpdateWorkflowUpdateWorkflowEnrichmentLink(BaseModel):
    enable_crawling: Optional[bool] = Field(alias="enableCrawling")
    allowed_domains: Optional[List[str]] = Field(alias="allowedDomains")
    excluded_domains: Optional[List[str]] = Field(alias="excludedDomains")
    allowed_paths: Optional[List[str]] = Field(alias="allowedPaths")
    excluded_paths: Optional[List[str]] = Field(alias="excludedPaths")
    allowed_links: Optional[List[LinkTypes]] = Field(alias="allowedLinks")
    excluded_links: Optional[List[LinkTypes]] = Field(alias="excludedLinks")
    allowed_files: Optional[List[FileTypes]] = Field(alias="allowedFiles")
    excluded_files: Optional[List[FileTypes]] = Field(alias="excludedFiles")
    allow_content_domain: Optional[bool] = Field(alias="allowContentDomain")
    maximum_links: Optional[int] = Field(alias="maximumLinks")


class UpdateWorkflowUpdateWorkflowEnrichmentJobs(BaseModel):
    connector: Optional["UpdateWorkflowUpdateWorkflowEnrichmentJobsConnector"]


class UpdateWorkflowUpdateWorkflowEnrichmentJobsConnector(BaseModel):
    type: Optional[EntityEnrichmentServiceTypes]
    enriched_types: Optional[List[Optional[ObservableTypes]]] = Field(
        alias="enrichedTypes"
    )


class UpdateWorkflowUpdateWorkflowStorage(BaseModel):
    embeddings: Optional["UpdateWorkflowUpdateWorkflowStorageEmbeddings"]


class UpdateWorkflowUpdateWorkflowStorageEmbeddings(BaseModel):
    chunk_token_limit: Optional[int] = Field(alias="chunkTokenLimit")


class UpdateWorkflowUpdateWorkflowActions(BaseModel):
    connector: Optional["UpdateWorkflowUpdateWorkflowActionsConnector"]


class UpdateWorkflowUpdateWorkflowActionsConnector(BaseModel):
    type: IntegrationServiceTypes
    uri: Optional[str]
    slack: Optional["UpdateWorkflowUpdateWorkflowActionsConnectorSlack"]


class UpdateWorkflowUpdateWorkflowActionsConnectorSlack(BaseModel):
    token: str
    channel: str


UpdateWorkflow.model_rebuild()
UpdateWorkflowUpdateWorkflow.model_rebuild()
UpdateWorkflowUpdateWorkflowIngestion.model_rebuild()
UpdateWorkflowUpdateWorkflowIndexing.model_rebuild()
UpdateWorkflowUpdateWorkflowIndexingJobs.model_rebuild()
UpdateWorkflowUpdateWorkflowPreparation.model_rebuild()
UpdateWorkflowUpdateWorkflowPreparationSummarizations.model_rebuild()
UpdateWorkflowUpdateWorkflowPreparationJobs.model_rebuild()
UpdateWorkflowUpdateWorkflowPreparationJobsConnector.model_rebuild()
UpdateWorkflowUpdateWorkflowExtraction.model_rebuild()
UpdateWorkflowUpdateWorkflowExtractionJobs.model_rebuild()
UpdateWorkflowUpdateWorkflowExtractionJobsConnector.model_rebuild()
UpdateWorkflowUpdateWorkflowExtractionJobsConnectorModelImage.model_rebuild()
UpdateWorkflowUpdateWorkflowExtractionJobsConnectorModelText.model_rebuild()
UpdateWorkflowUpdateWorkflowEnrichment.model_rebuild()
UpdateWorkflowUpdateWorkflowEnrichmentJobs.model_rebuild()
UpdateWorkflowUpdateWorkflowStorage.model_rebuild()
UpdateWorkflowUpdateWorkflowActions.model_rebuild()
UpdateWorkflowUpdateWorkflowActionsConnector.model_rebuild()
