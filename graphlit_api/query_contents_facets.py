# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    ContentFacetTypes,
    ContentTypes,
    EntityState,
    FacetValueTypes,
    FileTypes,
    ImageProjectionTypes,
    LinkTypes,
    MailImportance,
    MailPriority,
    MailSensitivity,
    ObservableTypes,
    OccurrenceTypes,
    OrientationTypes,
    TextRoles,
)


class QueryContentsFacets(BaseModel):
    contents: Optional["QueryContentsFacetsContents"]


class QueryContentsFacetsContents(BaseModel):
    results: Optional[List[Optional["QueryContentsFacetsContentsResults"]]]
    facets: Optional[List[Optional["QueryContentsFacetsContentsFacets"]]]


class QueryContentsFacetsContentsResults(BaseModel):
    id: str
    name: str
    creation_date: Any = Field(alias="creationDate")
    relevance: Optional[float]
    owner: "QueryContentsFacetsContentsResultsOwner"
    state: EntityState
    original_date: Optional[Any] = Field(alias="originalDate")
    finished_date: Optional[Any] = Field(alias="finishedDate")
    workflow_duration: Optional[Any] = Field(alias="workflowDuration")
    uri: Optional[Any]
    description: Optional[str]
    identifier: Optional[str]
    markdown: Optional[str]
    address: Optional["QueryContentsFacetsContentsResultsAddress"]
    location: Optional["QueryContentsFacetsContentsResultsLocation"]
    type: Optional[ContentTypes]
    file_type: Optional[FileTypes] = Field(alias="fileType")
    mime_type: Optional[str] = Field(alias="mimeType")
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
    video: Optional["QueryContentsFacetsContentsResultsVideo"]
    audio: Optional["QueryContentsFacetsContentsResultsAudio"]
    image: Optional["QueryContentsFacetsContentsResultsImage"]
    document: Optional["QueryContentsFacetsContentsResultsDocument"]
    email: Optional["QueryContentsFacetsContentsResultsEmail"]
    issue: Optional["QueryContentsFacetsContentsResultsIssue"]
    package: Optional["QueryContentsFacetsContentsResultsPackage"]
    language: Optional["QueryContentsFacetsContentsResultsLanguage"]
    parent: Optional["QueryContentsFacetsContentsResultsParent"]
    children: Optional[List[Optional["QueryContentsFacetsContentsResultsChildren"]]]
    feed: Optional["QueryContentsFacetsContentsResultsFeed"]
    collections: Optional[
        List[Optional["QueryContentsFacetsContentsResultsCollections"]]
    ]
    links: Optional[List["QueryContentsFacetsContentsResultsLinks"]]
    observations: Optional[
        List[Optional["QueryContentsFacetsContentsResultsObservations"]]
    ]
    workflow: Optional["QueryContentsFacetsContentsResultsWorkflow"]
    pages: Optional[List["QueryContentsFacetsContentsResultsPages"]]
    segments: Optional[List["QueryContentsFacetsContentsResultsSegments"]]
    error: Optional[str]


class QueryContentsFacetsContentsResultsOwner(BaseModel):
    id: str


class QueryContentsFacetsContentsResultsAddress(BaseModel):
    street_address: Optional[str] = Field(alias="streetAddress")
    city: Optional[str]
    region: Optional[str]
    country: Optional[str]
    postal_code: Optional[str] = Field(alias="postalCode")


class QueryContentsFacetsContentsResultsLocation(BaseModel):
    latitude: Optional[float]
    longitude: Optional[float]


class QueryContentsFacetsContentsResultsVideo(BaseModel):
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


class QueryContentsFacetsContentsResultsAudio(BaseModel):
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


class QueryContentsFacetsContentsResultsImage(BaseModel):
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


class QueryContentsFacetsContentsResultsDocument(BaseModel):
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


class QueryContentsFacetsContentsResultsEmail(BaseModel):
    identifier: Optional[str]
    subject: Optional[str]
    labels: Optional[List[Optional[str]]]
    sensitivity: Optional[MailSensitivity]
    priority: Optional[MailPriority]
    importance: Optional[MailImportance]
    from_: Optional[List[Optional["QueryContentsFacetsContentsResultsEmailFrom"]]] = (
        Field(alias="from")
    )
    to: Optional[List[Optional["QueryContentsFacetsContentsResultsEmailTo"]]]
    cc: Optional[List[Optional["QueryContentsFacetsContentsResultsEmailCc"]]]
    bcc: Optional[List[Optional["QueryContentsFacetsContentsResultsEmailBcc"]]]


class QueryContentsFacetsContentsResultsEmailFrom(BaseModel):
    name: Optional[str]
    email: Optional[str]
    given_name: Optional[str] = Field(alias="givenName")
    family_name: Optional[str] = Field(alias="familyName")


class QueryContentsFacetsContentsResultsEmailTo(BaseModel):
    name: Optional[str]
    email: Optional[str]
    given_name: Optional[str] = Field(alias="givenName")
    family_name: Optional[str] = Field(alias="familyName")


class QueryContentsFacetsContentsResultsEmailCc(BaseModel):
    name: Optional[str]
    email: Optional[str]
    given_name: Optional[str] = Field(alias="givenName")
    family_name: Optional[str] = Field(alias="familyName")


class QueryContentsFacetsContentsResultsEmailBcc(BaseModel):
    name: Optional[str]
    email: Optional[str]
    given_name: Optional[str] = Field(alias="givenName")
    family_name: Optional[str] = Field(alias="familyName")


class QueryContentsFacetsContentsResultsIssue(BaseModel):
    identifier: Optional[str]
    title: Optional[str]
    project: Optional[str]
    team: Optional[str]
    status: Optional[str]
    priority: Optional[str]
    type: Optional[str]
    labels: Optional[List[Optional[str]]]


class QueryContentsFacetsContentsResultsPackage(BaseModel):
    file_count: Optional[int] = Field(alias="fileCount")
    folder_count: Optional[int] = Field(alias="folderCount")
    is_encrypted: Optional[bool] = Field(alias="isEncrypted")


class QueryContentsFacetsContentsResultsLanguage(BaseModel):
    languages: Optional[List[Optional[str]]]


class QueryContentsFacetsContentsResultsParent(BaseModel):
    id: str
    name: str


class QueryContentsFacetsContentsResultsChildren(BaseModel):
    id: str
    name: str


class QueryContentsFacetsContentsResultsFeed(BaseModel):
    id: str
    name: str


class QueryContentsFacetsContentsResultsCollections(BaseModel):
    id: str
    name: str


class QueryContentsFacetsContentsResultsLinks(BaseModel):
    uri: Optional[Any]
    link_type: Optional[LinkTypes] = Field(alias="linkType")


class QueryContentsFacetsContentsResultsObservations(BaseModel):
    id: str
    type: ObservableTypes
    observable: "QueryContentsFacetsContentsResultsObservationsObservable"
    related: Optional["QueryContentsFacetsContentsResultsObservationsRelated"]
    related_type: Optional[ObservableTypes] = Field(alias="relatedType")
    relation: Optional[str]
    occurrences: Optional[
        List[Optional["QueryContentsFacetsContentsResultsObservationsOccurrences"]]
    ]
    state: EntityState


class QueryContentsFacetsContentsResultsObservationsObservable(BaseModel):
    id: str
    name: Optional[str]


class QueryContentsFacetsContentsResultsObservationsRelated(BaseModel):
    id: str
    name: Optional[str]


class QueryContentsFacetsContentsResultsObservationsOccurrences(BaseModel):
    type: Optional[OccurrenceTypes]
    confidence: Optional[float]
    start_time: Optional[Any] = Field(alias="startTime")
    end_time: Optional[Any] = Field(alias="endTime")
    page_index: Optional[int] = Field(alias="pageIndex")
    bounding_box: Optional[
        "QueryContentsFacetsContentsResultsObservationsOccurrencesBoundingBox"
    ] = Field(alias="boundingBox")


class QueryContentsFacetsContentsResultsObservationsOccurrencesBoundingBox(BaseModel):
    left: Optional[float]
    top: Optional[float]
    width: Optional[float]
    height: Optional[float]


class QueryContentsFacetsContentsResultsWorkflow(BaseModel):
    id: str
    name: str


class QueryContentsFacetsContentsResultsPages(BaseModel):
    index: Optional[int]
    chunks: Optional[List[Optional["QueryContentsFacetsContentsResultsPagesChunks"]]]


class QueryContentsFacetsContentsResultsPagesChunks(BaseModel):
    index: Optional[int]
    page_index: Optional[int] = Field(alias="pageIndex")
    row_index: Optional[int] = Field(alias="rowIndex")
    column_index: Optional[int] = Field(alias="columnIndex")
    confidence: Optional[float]
    text: Optional[str]
    role: Optional[TextRoles]
    relevance: Optional[float]


class QueryContentsFacetsContentsResultsSegments(BaseModel):
    start_time: Optional[Any] = Field(alias="startTime")
    end_time: Optional[Any] = Field(alias="endTime")
    text: Optional[str]
    relevance: Optional[float]


class QueryContentsFacetsContentsFacets(BaseModel):
    facet: Optional[ContentFacetTypes]
    count: Optional[Any]
    type: Optional[FacetValueTypes]
    value: Optional[str]
    range: Optional["QueryContentsFacetsContentsFacetsRange"]
    observable: Optional["QueryContentsFacetsContentsFacetsObservable"]


class QueryContentsFacetsContentsFacetsRange(BaseModel):
    from_: Optional[str] = Field(alias="from")
    to: Optional[str]


class QueryContentsFacetsContentsFacetsObservable(BaseModel):
    type: Optional[ObservableTypes]
    observable: Optional["QueryContentsFacetsContentsFacetsObservableObservable"]


class QueryContentsFacetsContentsFacetsObservableObservable(BaseModel):
    id: str
    name: Optional[str]


QueryContentsFacets.model_rebuild()
QueryContentsFacetsContents.model_rebuild()
QueryContentsFacetsContentsResults.model_rebuild()
QueryContentsFacetsContentsResultsEmail.model_rebuild()
QueryContentsFacetsContentsResultsObservations.model_rebuild()
QueryContentsFacetsContentsResultsObservationsOccurrences.model_rebuild()
QueryContentsFacetsContentsResultsPages.model_rebuild()
QueryContentsFacetsContentsFacets.model_rebuild()
QueryContentsFacetsContentsFacetsObservable.model_rebuild()
