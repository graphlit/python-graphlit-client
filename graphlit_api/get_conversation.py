# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    ContentTypes,
    ConversationRoleTypes,
    ConversationTypes,
    EntityState,
    FileTypes,
    ImageProjectionTypes,
    ModelServiceTypes,
    ObservableTypes,
    OrientationTypes,
)


class GetConversation(BaseModel):
    conversation: Optional["GetConversationConversation"]


class GetConversationConversation(BaseModel):
    id: str
    name: str
    creation_date: Any = Field(alias="creationDate")
    relevance: Optional[float]
    owner: "GetConversationConversationOwner"
    state: EntityState
    correlation_id: Optional[str] = Field(alias="correlationId")
    type: Optional[ConversationTypes]
    messages: Optional[List[Optional["GetConversationConversationMessages"]]]
    specification: Optional["GetConversationConversationSpecification"]
    fallbacks: Optional[List[Optional["GetConversationConversationFallbacks"]]]
    filter: Optional["GetConversationConversationFilter"]
    augmented_filter: Optional["GetConversationConversationAugmentedFilter"] = Field(
        alias="augmentedFilter"
    )


class GetConversationConversationOwner(BaseModel):
    id: str


class GetConversationConversationMessages(BaseModel):
    role: ConversationRoleTypes
    author: Optional[str]
    message: Optional[str]
    citations: Optional[List[Optional["GetConversationConversationMessagesCitations"]]]
    tool_calls: Optional[
        List[Optional["GetConversationConversationMessagesToolCalls"]]
    ] = Field(alias="toolCalls")
    tokens: Optional[int]
    throughput: Optional[float]
    completion_time: Optional[Any] = Field(alias="completionTime")
    timestamp: Optional[Any]
    model_service: Optional[ModelServiceTypes] = Field(alias="modelService")
    model: Optional[str]
    data: Optional[str]
    mime_type: Optional[str] = Field(alias="mimeType")


class GetConversationConversationMessagesCitations(BaseModel):
    content: Optional["GetConversationConversationMessagesCitationsContent"]
    index: Optional[int]
    text: str
    start_time: Optional[Any] = Field(alias="startTime")
    end_time: Optional[Any] = Field(alias="endTime")
    page_number: Optional[int] = Field(alias="pageNumber")
    frame_number: Optional[int] = Field(alias="frameNumber")


class GetConversationConversationMessagesCitationsContent(BaseModel):
    id: str
    name: str
    state: EntityState
    original_date: Optional[Any] = Field(alias="originalDate")
    identifier: Optional[str]
    uri: Optional[Any]
    type: Optional[ContentTypes]
    file_type: Optional[FileTypes] = Field(alias="fileType")
    mime_type: Optional[str] = Field(alias="mimeType")
    format: Optional[str]
    format_name: Optional[str] = Field(alias="formatName")
    file_extension: Optional[str] = Field(alias="fileExtension")
    file_name: Optional[str] = Field(alias="fileName")
    file_size: Optional[Any] = Field(alias="fileSize")
    master_uri: Optional[Any] = Field(alias="masterUri")
    image_uri: Optional[Any] = Field(alias="imageUri")
    text_uri: Optional[Any] = Field(alias="textUri")
    audio_uri: Optional[Any] = Field(alias="audioUri")
    transcript_uri: Optional[Any] = Field(alias="transcriptUri")
    summary: Optional[str]
    custom_summary: Optional[str] = Field(alias="customSummary")
    keywords: Optional[List[str]]
    bullets: Optional[List[str]]
    headlines: Optional[List[str]]
    posts: Optional[List[str]]
    chapters: Optional[List[str]]
    questions: Optional[List[str]]
    video: Optional["GetConversationConversationMessagesCitationsContentVideo"]
    audio: Optional["GetConversationConversationMessagesCitationsContentAudio"]
    image: Optional["GetConversationConversationMessagesCitationsContentImage"]
    document: Optional["GetConversationConversationMessagesCitationsContentDocument"]


class GetConversationConversationMessagesCitationsContentVideo(BaseModel):
    width: Optional[int]
    height: Optional[int]
    duration: Optional[Any]
    make: Optional[str]
    model: Optional[str]
    software: Optional[str]
    title: Optional[str]
    description: Optional[str]
    keywords: Optional[List[Optional[str]]]
    author: Optional[str]


class GetConversationConversationMessagesCitationsContentAudio(BaseModel):
    keywords: Optional[List[Optional[str]]]
    author: Optional[str]
    series: Optional[str]
    episode: Optional[str]
    episode_type: Optional[str] = Field(alias="episodeType")
    season: Optional[str]
    publisher: Optional[str]
    copyright: Optional[str]
    genre: Optional[str]
    title: Optional[str]
    description: Optional[str]
    bitrate: Optional[int]
    channels: Optional[int]
    sample_rate: Optional[int] = Field(alias="sampleRate")
    bits_per_sample: Optional[int] = Field(alias="bitsPerSample")
    duration: Optional[Any]


class GetConversationConversationMessagesCitationsContentImage(BaseModel):
    width: Optional[int]
    height: Optional[int]
    resolution_x: Optional[int] = Field(alias="resolutionX")
    resolution_y: Optional[int] = Field(alias="resolutionY")
    bits_per_component: Optional[int] = Field(alias="bitsPerComponent")
    components: Optional[int]
    projection_type: Optional[ImageProjectionTypes] = Field(alias="projectionType")
    orientation: Optional[OrientationTypes]
    description: Optional[str]
    make: Optional[str]
    model: Optional[str]
    software: Optional[str]
    lens: Optional[str]
    focal_length: Optional[float] = Field(alias="focalLength")
    exposure_time: Optional[str] = Field(alias="exposureTime")
    f_number: Optional[str] = Field(alias="fNumber")
    iso: Optional[str]
    heading: Optional[float]
    pitch: Optional[float]


class GetConversationConversationMessagesCitationsContentDocument(BaseModel):
    title: Optional[str]
    subject: Optional[str]
    summary: Optional[str]
    author: Optional[str]
    publisher: Optional[str]
    description: Optional[str]
    keywords: Optional[List[Optional[str]]]
    page_count: Optional[int] = Field(alias="pageCount")
    worksheet_count: Optional[int] = Field(alias="worksheetCount")
    slide_count: Optional[int] = Field(alias="slideCount")
    word_count: Optional[int] = Field(alias="wordCount")
    line_count: Optional[int] = Field(alias="lineCount")
    paragraph_count: Optional[int] = Field(alias="paragraphCount")
    is_encrypted: Optional[bool] = Field(alias="isEncrypted")
    has_digital_signature: Optional[bool] = Field(alias="hasDigitalSignature")


class GetConversationConversationMessagesToolCalls(BaseModel):
    id: str
    name: str
    arguments: str


class GetConversationConversationSpecification(BaseModel):
    id: str
    name: str


class GetConversationConversationFallbacks(BaseModel):
    id: str
    name: str


class GetConversationConversationFilter(BaseModel):
    date_range: Optional["GetConversationConversationFilterDateRange"] = Field(
        alias="dateRange"
    )
    in_last: Optional[Any] = Field(alias="inLast")
    creation_date_range: Optional[
        "GetConversationConversationFilterCreationDateRange"
    ] = Field(alias="creationDateRange")
    created_in_last: Optional[Any] = Field(alias="createdInLast")
    types: Optional[List[ContentTypes]]
    file_types: Optional[List[Optional[FileTypes]]] = Field(alias="fileTypes")
    contents: Optional[List["GetConversationConversationFilterContents"]]
    feeds: Optional[List["GetConversationConversationFilterFeeds"]]
    workflows: Optional[List["GetConversationConversationFilterWorkflows"]]
    collections: Optional[List["GetConversationConversationFilterCollections"]]
    users: Optional[List["GetConversationConversationFilterUsers"]]
    observations: Optional[List["GetConversationConversationFilterObservations"]]
    or_: Optional[List["GetConversationConversationFilterOr"]] = Field(alias="or")
    and_: Optional[List["GetConversationConversationFilterAnd"]] = Field(alias="and")


class GetConversationConversationFilterDateRange(BaseModel):
    from_: Optional[Any] = Field(alias="from")
    to: Optional[Any]


class GetConversationConversationFilterCreationDateRange(BaseModel):
    from_: Optional[Any] = Field(alias="from")
    to: Optional[Any]


class GetConversationConversationFilterContents(BaseModel):
    id: str


class GetConversationConversationFilterFeeds(BaseModel):
    id: str


class GetConversationConversationFilterWorkflows(BaseModel):
    id: str


class GetConversationConversationFilterCollections(BaseModel):
    id: str


class GetConversationConversationFilterUsers(BaseModel):
    id: str


class GetConversationConversationFilterObservations(BaseModel):
    type: ObservableTypes
    observable: "GetConversationConversationFilterObservationsObservable"
    states: Optional[List[Optional[EntityState]]]


class GetConversationConversationFilterObservationsObservable(BaseModel):
    id: str


class GetConversationConversationFilterOr(BaseModel):
    feeds: Optional[List["GetConversationConversationFilterOrFeeds"]]
    workflows: Optional[List["GetConversationConversationFilterOrWorkflows"]]
    collections: Optional[List["GetConversationConversationFilterOrCollections"]]
    users: Optional[List["GetConversationConversationFilterOrUsers"]]
    observations: Optional[List["GetConversationConversationFilterOrObservations"]]


class GetConversationConversationFilterOrFeeds(BaseModel):
    id: str


class GetConversationConversationFilterOrWorkflows(BaseModel):
    id: str


class GetConversationConversationFilterOrCollections(BaseModel):
    id: str


class GetConversationConversationFilterOrUsers(BaseModel):
    id: str


class GetConversationConversationFilterOrObservations(BaseModel):
    type: ObservableTypes
    observable: "GetConversationConversationFilterOrObservationsObservable"
    states: Optional[List[Optional[EntityState]]]


class GetConversationConversationFilterOrObservationsObservable(BaseModel):
    id: str


class GetConversationConversationFilterAnd(BaseModel):
    feeds: Optional[List["GetConversationConversationFilterAndFeeds"]]
    workflows: Optional[List["GetConversationConversationFilterAndWorkflows"]]
    collections: Optional[List["GetConversationConversationFilterAndCollections"]]
    users: Optional[List["GetConversationConversationFilterAndUsers"]]
    observations: Optional[List["GetConversationConversationFilterAndObservations"]]


class GetConversationConversationFilterAndFeeds(BaseModel):
    id: str


class GetConversationConversationFilterAndWorkflows(BaseModel):
    id: str


class GetConversationConversationFilterAndCollections(BaseModel):
    id: str


class GetConversationConversationFilterAndUsers(BaseModel):
    id: str


class GetConversationConversationFilterAndObservations(BaseModel):
    type: ObservableTypes
    observable: "GetConversationConversationFilterAndObservationsObservable"
    states: Optional[List[Optional[EntityState]]]


class GetConversationConversationFilterAndObservationsObservable(BaseModel):
    id: str


class GetConversationConversationAugmentedFilter(BaseModel):
    date_range: Optional["GetConversationConversationAugmentedFilterDateRange"] = Field(
        alias="dateRange"
    )
    in_last: Optional[Any] = Field(alias="inLast")
    creation_date_range: Optional[
        "GetConversationConversationAugmentedFilterCreationDateRange"
    ] = Field(alias="creationDateRange")
    created_in_last: Optional[Any] = Field(alias="createdInLast")
    types: Optional[List[ContentTypes]]
    file_types: Optional[List[Optional[FileTypes]]] = Field(alias="fileTypes")
    contents: Optional[List["GetConversationConversationAugmentedFilterContents"]]
    feeds: Optional[List["GetConversationConversationAugmentedFilterFeeds"]]
    workflows: Optional[List["GetConversationConversationAugmentedFilterWorkflows"]]
    collections: Optional[List["GetConversationConversationAugmentedFilterCollections"]]
    users: Optional[List["GetConversationConversationAugmentedFilterUsers"]]
    observations: Optional[
        List["GetConversationConversationAugmentedFilterObservations"]
    ]
    or_: Optional[List["GetConversationConversationAugmentedFilterOr"]] = Field(
        alias="or"
    )
    and_: Optional[List["GetConversationConversationAugmentedFilterAnd"]] = Field(
        alias="and"
    )


class GetConversationConversationAugmentedFilterDateRange(BaseModel):
    from_: Optional[Any] = Field(alias="from")
    to: Optional[Any]


class GetConversationConversationAugmentedFilterCreationDateRange(BaseModel):
    from_: Optional[Any] = Field(alias="from")
    to: Optional[Any]


class GetConversationConversationAugmentedFilterContents(BaseModel):
    id: str


class GetConversationConversationAugmentedFilterFeeds(BaseModel):
    id: str


class GetConversationConversationAugmentedFilterWorkflows(BaseModel):
    id: str


class GetConversationConversationAugmentedFilterCollections(BaseModel):
    id: str


class GetConversationConversationAugmentedFilterUsers(BaseModel):
    id: str


class GetConversationConversationAugmentedFilterObservations(BaseModel):
    type: ObservableTypes
    observable: "GetConversationConversationAugmentedFilterObservationsObservable"
    states: Optional[List[Optional[EntityState]]]


class GetConversationConversationAugmentedFilterObservationsObservable(BaseModel):
    id: str


class GetConversationConversationAugmentedFilterOr(BaseModel):
    feeds: Optional[List["GetConversationConversationAugmentedFilterOrFeeds"]]
    workflows: Optional[List["GetConversationConversationAugmentedFilterOrWorkflows"]]
    collections: Optional[
        List["GetConversationConversationAugmentedFilterOrCollections"]
    ]
    users: Optional[List["GetConversationConversationAugmentedFilterOrUsers"]]
    observations: Optional[
        List["GetConversationConversationAugmentedFilterOrObservations"]
    ]


class GetConversationConversationAugmentedFilterOrFeeds(BaseModel):
    id: str


class GetConversationConversationAugmentedFilterOrWorkflows(BaseModel):
    id: str


class GetConversationConversationAugmentedFilterOrCollections(BaseModel):
    id: str


class GetConversationConversationAugmentedFilterOrUsers(BaseModel):
    id: str


class GetConversationConversationAugmentedFilterOrObservations(BaseModel):
    type: ObservableTypes
    observable: "GetConversationConversationAugmentedFilterOrObservationsObservable"
    states: Optional[List[Optional[EntityState]]]


class GetConversationConversationAugmentedFilterOrObservationsObservable(BaseModel):
    id: str


class GetConversationConversationAugmentedFilterAnd(BaseModel):
    feeds: Optional[List["GetConversationConversationAugmentedFilterAndFeeds"]]
    workflows: Optional[List["GetConversationConversationAugmentedFilterAndWorkflows"]]
    collections: Optional[
        List["GetConversationConversationAugmentedFilterAndCollections"]
    ]
    users: Optional[List["GetConversationConversationAugmentedFilterAndUsers"]]
    observations: Optional[
        List["GetConversationConversationAugmentedFilterAndObservations"]
    ]


class GetConversationConversationAugmentedFilterAndFeeds(BaseModel):
    id: str


class GetConversationConversationAugmentedFilterAndWorkflows(BaseModel):
    id: str


class GetConversationConversationAugmentedFilterAndCollections(BaseModel):
    id: str


class GetConversationConversationAugmentedFilterAndUsers(BaseModel):
    id: str


class GetConversationConversationAugmentedFilterAndObservations(BaseModel):
    type: ObservableTypes
    observable: "GetConversationConversationAugmentedFilterAndObservationsObservable"
    states: Optional[List[Optional[EntityState]]]


class GetConversationConversationAugmentedFilterAndObservationsObservable(BaseModel):
    id: str


GetConversation.model_rebuild()
GetConversationConversation.model_rebuild()
GetConversationConversationMessages.model_rebuild()
GetConversationConversationMessagesCitations.model_rebuild()
GetConversationConversationMessagesCitationsContent.model_rebuild()
GetConversationConversationFilter.model_rebuild()
GetConversationConversationFilterObservations.model_rebuild()
GetConversationConversationFilterOr.model_rebuild()
GetConversationConversationFilterOrObservations.model_rebuild()
GetConversationConversationFilterAnd.model_rebuild()
GetConversationConversationFilterAndObservations.model_rebuild()
GetConversationConversationAugmentedFilter.model_rebuild()
GetConversationConversationAugmentedFilterObservations.model_rebuild()
GetConversationConversationAugmentedFilterOr.model_rebuild()
GetConversationConversationAugmentedFilterOrObservations.model_rebuild()
GetConversationConversationAugmentedFilterAnd.model_rebuild()
GetConversationConversationAugmentedFilterAndObservations.model_rebuild()
