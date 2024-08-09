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


class QueryConversations(BaseModel):
    conversations: Optional["QueryConversationsConversations"]


class QueryConversationsConversations(BaseModel):
    results: Optional[List[Optional["QueryConversationsConversationsResults"]]]


class QueryConversationsConversationsResults(BaseModel):
    id: str
    name: str
    creation_date: Any = Field(alias="creationDate")
    relevance: Optional[float]
    owner: "QueryConversationsConversationsResultsOwner"
    state: EntityState
    correlation_id: Optional[str] = Field(alias="correlationId")
    type: Optional[ConversationTypes]
    messages: Optional[List[Optional["QueryConversationsConversationsResultsMessages"]]]
    specification: Optional["QueryConversationsConversationsResultsSpecification"]
    filter: Optional["QueryConversationsConversationsResultsFilter"]
    augmented_filter: Optional[
        "QueryConversationsConversationsResultsAugmentedFilter"
    ] = Field(alias="augmentedFilter")


class QueryConversationsConversationsResultsOwner(BaseModel):
    id: str


class QueryConversationsConversationsResultsMessages(BaseModel):
    role: ConversationRoleTypes
    author: Optional[str]
    message: str
    citations: Optional[
        List[Optional["QueryConversationsConversationsResultsMessagesCitations"]]
    ]
    tokens: int
    throughput: Optional[float]
    completion_time: Optional[Any] = Field(alias="completionTime")
    timestamp: Any
    model_service: Optional[ModelServiceTypes] = Field(alias="modelService")
    model: Optional[str]


class QueryConversationsConversationsResultsMessagesCitations(BaseModel):
    content: Optional["QueryConversationsConversationsResultsMessagesCitationsContent"]
    index: Optional[int]
    text: Optional[str]
    start_time: Optional[Any] = Field(alias="startTime")
    end_time: Optional[Any] = Field(alias="endTime")
    page_number: Optional[int] = Field(alias="pageNumber")
    frame_number: Optional[int] = Field(alias="frameNumber")


class QueryConversationsConversationsResultsMessagesCitationsContent(BaseModel):
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
    video: Optional[
        "QueryConversationsConversationsResultsMessagesCitationsContentVideo"
    ]
    audio: Optional[
        "QueryConversationsConversationsResultsMessagesCitationsContentAudio"
    ]
    image: Optional[
        "QueryConversationsConversationsResultsMessagesCitationsContentImage"
    ]
    document: Optional[
        "QueryConversationsConversationsResultsMessagesCitationsContentDocument"
    ]


class QueryConversationsConversationsResultsMessagesCitationsContentVideo(BaseModel):
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


class QueryConversationsConversationsResultsMessagesCitationsContentAudio(BaseModel):
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


class QueryConversationsConversationsResultsMessagesCitationsContentImage(BaseModel):
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


class QueryConversationsConversationsResultsMessagesCitationsContentDocument(BaseModel):
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


class QueryConversationsConversationsResultsSpecification(BaseModel):
    id: str
    name: str


class QueryConversationsConversationsResultsFilter(BaseModel):
    date_range: Optional["QueryConversationsConversationsResultsFilterDateRange"] = (
        Field(alias="dateRange")
    )
    creation_date_range: Optional[
        "QueryConversationsConversationsResultsFilterCreationDateRange"
    ] = Field(alias="creationDateRange")
    types: Optional[List[ContentTypes]]
    file_types: Optional[List[Optional[FileTypes]]] = Field(alias="fileTypes")
    contents: Optional[List["QueryConversationsConversationsResultsFilterContents"]]
    feeds: Optional[List["QueryConversationsConversationsResultsFilterFeeds"]]
    workflows: Optional[List["QueryConversationsConversationsResultsFilterWorkflows"]]
    collections: Optional[
        List["QueryConversationsConversationsResultsFilterCollections"]
    ]
    observations: Optional[
        List["QueryConversationsConversationsResultsFilterObservations"]
    ]
    or_: Optional[List["QueryConversationsConversationsResultsFilterOr"]] = Field(
        alias="or"
    )
    and_: Optional[List["QueryConversationsConversationsResultsFilterAnd"]] = Field(
        alias="and"
    )


class QueryConversationsConversationsResultsFilterDateRange(BaseModel):
    from_: Optional[Any] = Field(alias="from")
    to: Optional[Any]


class QueryConversationsConversationsResultsFilterCreationDateRange(BaseModel):
    from_: Optional[Any] = Field(alias="from")
    to: Optional[Any]


class QueryConversationsConversationsResultsFilterContents(BaseModel):
    id: str


class QueryConversationsConversationsResultsFilterFeeds(BaseModel):
    id: str


class QueryConversationsConversationsResultsFilterWorkflows(BaseModel):
    id: str


class QueryConversationsConversationsResultsFilterCollections(BaseModel):
    id: str


class QueryConversationsConversationsResultsFilterObservations(BaseModel):
    type: ObservableTypes
    observable: "QueryConversationsConversationsResultsFilterObservationsObservable"
    states: Optional[List[Optional[EntityState]]]


class QueryConversationsConversationsResultsFilterObservationsObservable(BaseModel):
    id: str


class QueryConversationsConversationsResultsFilterOr(BaseModel):
    feeds: Optional[List["QueryConversationsConversationsResultsFilterOrFeeds"]]
    workflows: Optional[List["QueryConversationsConversationsResultsFilterOrWorkflows"]]
    collections: Optional[
        List["QueryConversationsConversationsResultsFilterOrCollections"]
    ]
    observations: Optional[
        List["QueryConversationsConversationsResultsFilterOrObservations"]
    ]


class QueryConversationsConversationsResultsFilterOrFeeds(BaseModel):
    id: str


class QueryConversationsConversationsResultsFilterOrWorkflows(BaseModel):
    id: str


class QueryConversationsConversationsResultsFilterOrCollections(BaseModel):
    id: str


class QueryConversationsConversationsResultsFilterOrObservations(BaseModel):
    type: ObservableTypes
    observable: "QueryConversationsConversationsResultsFilterOrObservationsObservable"
    states: Optional[List[Optional[EntityState]]]


class QueryConversationsConversationsResultsFilterOrObservationsObservable(BaseModel):
    id: str


class QueryConversationsConversationsResultsFilterAnd(BaseModel):
    feeds: Optional[List["QueryConversationsConversationsResultsFilterAndFeeds"]]
    workflows: Optional[
        List["QueryConversationsConversationsResultsFilterAndWorkflows"]
    ]
    collections: Optional[
        List["QueryConversationsConversationsResultsFilterAndCollections"]
    ]
    observations: Optional[
        List["QueryConversationsConversationsResultsFilterAndObservations"]
    ]


class QueryConversationsConversationsResultsFilterAndFeeds(BaseModel):
    id: str


class QueryConversationsConversationsResultsFilterAndWorkflows(BaseModel):
    id: str


class QueryConversationsConversationsResultsFilterAndCollections(BaseModel):
    id: str


class QueryConversationsConversationsResultsFilterAndObservations(BaseModel):
    type: ObservableTypes
    observable: "QueryConversationsConversationsResultsFilterAndObservationsObservable"
    states: Optional[List[Optional[EntityState]]]


class QueryConversationsConversationsResultsFilterAndObservationsObservable(BaseModel):
    id: str


class QueryConversationsConversationsResultsAugmentedFilter(BaseModel):
    date_range: Optional[
        "QueryConversationsConversationsResultsAugmentedFilterDateRange"
    ] = Field(alias="dateRange")
    creation_date_range: Optional[
        "QueryConversationsConversationsResultsAugmentedFilterCreationDateRange"
    ] = Field(alias="creationDateRange")
    types: Optional[List[ContentTypes]]
    file_types: Optional[List[Optional[FileTypes]]] = Field(alias="fileTypes")
    contents: Optional[
        List["QueryConversationsConversationsResultsAugmentedFilterContents"]
    ]
    feeds: Optional[List["QueryConversationsConversationsResultsAugmentedFilterFeeds"]]
    workflows: Optional[
        List["QueryConversationsConversationsResultsAugmentedFilterWorkflows"]
    ]
    collections: Optional[
        List["QueryConversationsConversationsResultsAugmentedFilterCollections"]
    ]
    observations: Optional[
        List["QueryConversationsConversationsResultsAugmentedFilterObservations"]
    ]
    or_: Optional[List["QueryConversationsConversationsResultsAugmentedFilterOr"]] = (
        Field(alias="or")
    )
    and_: Optional[List["QueryConversationsConversationsResultsAugmentedFilterAnd"]] = (
        Field(alias="and")
    )


class QueryConversationsConversationsResultsAugmentedFilterDateRange(BaseModel):
    from_: Optional[Any] = Field(alias="from")
    to: Optional[Any]


class QueryConversationsConversationsResultsAugmentedFilterCreationDateRange(BaseModel):
    from_: Optional[Any] = Field(alias="from")
    to: Optional[Any]


class QueryConversationsConversationsResultsAugmentedFilterContents(BaseModel):
    id: str


class QueryConversationsConversationsResultsAugmentedFilterFeeds(BaseModel):
    id: str


class QueryConversationsConversationsResultsAugmentedFilterWorkflows(BaseModel):
    id: str


class QueryConversationsConversationsResultsAugmentedFilterCollections(BaseModel):
    id: str


class QueryConversationsConversationsResultsAugmentedFilterObservations(BaseModel):
    type: ObservableTypes
    observable: (
        "QueryConversationsConversationsResultsAugmentedFilterObservationsObservable"
    )
    states: Optional[List[Optional[EntityState]]]


class QueryConversationsConversationsResultsAugmentedFilterObservationsObservable(
    BaseModel
):
    id: str


class QueryConversationsConversationsResultsAugmentedFilterOr(BaseModel):
    feeds: Optional[
        List["QueryConversationsConversationsResultsAugmentedFilterOrFeeds"]
    ]
    workflows: Optional[
        List["QueryConversationsConversationsResultsAugmentedFilterOrWorkflows"]
    ]
    collections: Optional[
        List["QueryConversationsConversationsResultsAugmentedFilterOrCollections"]
    ]
    observations: Optional[
        List["QueryConversationsConversationsResultsAugmentedFilterOrObservations"]
    ]


class QueryConversationsConversationsResultsAugmentedFilterOrFeeds(BaseModel):
    id: str


class QueryConversationsConversationsResultsAugmentedFilterOrWorkflows(BaseModel):
    id: str


class QueryConversationsConversationsResultsAugmentedFilterOrCollections(BaseModel):
    id: str


class QueryConversationsConversationsResultsAugmentedFilterOrObservations(BaseModel):
    type: ObservableTypes
    observable: (
        "QueryConversationsConversationsResultsAugmentedFilterOrObservationsObservable"
    )
    states: Optional[List[Optional[EntityState]]]


class QueryConversationsConversationsResultsAugmentedFilterOrObservationsObservable(
    BaseModel
):
    id: str


class QueryConversationsConversationsResultsAugmentedFilterAnd(BaseModel):
    feeds: Optional[
        List["QueryConversationsConversationsResultsAugmentedFilterAndFeeds"]
    ]
    workflows: Optional[
        List["QueryConversationsConversationsResultsAugmentedFilterAndWorkflows"]
    ]
    collections: Optional[
        List["QueryConversationsConversationsResultsAugmentedFilterAndCollections"]
    ]
    observations: Optional[
        List["QueryConversationsConversationsResultsAugmentedFilterAndObservations"]
    ]


class QueryConversationsConversationsResultsAugmentedFilterAndFeeds(BaseModel):
    id: str


class QueryConversationsConversationsResultsAugmentedFilterAndWorkflows(BaseModel):
    id: str


class QueryConversationsConversationsResultsAugmentedFilterAndCollections(BaseModel):
    id: str


class QueryConversationsConversationsResultsAugmentedFilterAndObservations(BaseModel):
    type: ObservableTypes
    observable: (
        "QueryConversationsConversationsResultsAugmentedFilterAndObservationsObservable"
    )
    states: Optional[List[Optional[EntityState]]]


class QueryConversationsConversationsResultsAugmentedFilterAndObservationsObservable(
    BaseModel
):
    id: str


QueryConversations.model_rebuild()
QueryConversationsConversations.model_rebuild()
QueryConversationsConversationsResults.model_rebuild()
QueryConversationsConversationsResultsMessages.model_rebuild()
QueryConversationsConversationsResultsMessagesCitations.model_rebuild()
QueryConversationsConversationsResultsMessagesCitationsContent.model_rebuild()
QueryConversationsConversationsResultsFilter.model_rebuild()
QueryConversationsConversationsResultsFilterObservations.model_rebuild()
QueryConversationsConversationsResultsFilterOr.model_rebuild()
QueryConversationsConversationsResultsFilterOrObservations.model_rebuild()
QueryConversationsConversationsResultsFilterAnd.model_rebuild()
QueryConversationsConversationsResultsFilterAndObservations.model_rebuild()
QueryConversationsConversationsResultsAugmentedFilter.model_rebuild()
QueryConversationsConversationsResultsAugmentedFilterObservations.model_rebuild()
QueryConversationsConversationsResultsAugmentedFilterOr.model_rebuild()
QueryConversationsConversationsResultsAugmentedFilterOrObservations.model_rebuild()
QueryConversationsConversationsResultsAugmentedFilterAnd.model_rebuild()
QueryConversationsConversationsResultsAugmentedFilterAndObservations.model_rebuild()
