# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    ContentTypes,
    EntityState,
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


class GetContent(BaseModel):
    content: Optional["GetContentContent"]


class GetContentContent(BaseModel):
    id: str
    name: str
    creation_date: Any = Field(alias="creationDate")
    relevance: Optional[float]
    owner: "GetContentContentOwner"
    state: EntityState
    original_date: Optional[Any] = Field(alias="originalDate")
    finished_date: Optional[Any] = Field(alias="finishedDate")
    workflow_duration: Optional[Any] = Field(alias="workflowDuration")
    uri: Optional[Any]
    description: Optional[str]
    identifier: Optional[str]
    markdown: Optional[str]
    address: Optional["GetContentContentAddress"]
    location: Optional["GetContentContentLocation"]
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
    video: Optional["GetContentContentVideo"]
    audio: Optional["GetContentContentAudio"]
    image: Optional["GetContentContentImage"]
    document: Optional["GetContentContentDocument"]
    email: Optional["GetContentContentEmail"]
    issue: Optional["GetContentContentIssue"]
    package: Optional["GetContentContentPackage"]
    language: Optional["GetContentContentLanguage"]
    parent: Optional["GetContentContentParent"]
    children: Optional[List[Optional["GetContentContentChildren"]]]
    feed: Optional["GetContentContentFeed"]
    collections: Optional[List[Optional["GetContentContentCollections"]]]
    links: Optional[List["GetContentContentLinks"]]
    observations: Optional[List[Optional["GetContentContentObservations"]]]
    workflow: Optional["GetContentContentWorkflow"]
    pages: Optional[List["GetContentContentPages"]]
    segments: Optional[List["GetContentContentSegments"]]
    frames: Optional[List["GetContentContentFrames"]]
    error: Optional[str]


class GetContentContentOwner(BaseModel):
    id: str


class GetContentContentAddress(BaseModel):
    street_address: Optional[str] = Field(alias="streetAddress")
    city: Optional[str]
    region: Optional[str]
    country: Optional[str]
    postal_code: Optional[str] = Field(alias="postalCode")


class GetContentContentLocation(BaseModel):
    latitude: Optional[float]
    longitude: Optional[float]


class GetContentContentVideo(BaseModel):
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


class GetContentContentAudio(BaseModel):
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


class GetContentContentImage(BaseModel):
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


class GetContentContentDocument(BaseModel):
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


class GetContentContentEmail(BaseModel):
    identifier: Optional[str]
    subject: Optional[str]
    labels: Optional[List[Optional[str]]]
    sensitivity: Optional[MailSensitivity]
    priority: Optional[MailPriority]
    importance: Optional[MailImportance]
    from_: Optional[List[Optional["GetContentContentEmailFrom"]]] = Field(alias="from")
    to: Optional[List[Optional["GetContentContentEmailTo"]]]
    cc: Optional[List[Optional["GetContentContentEmailCc"]]]
    bcc: Optional[List[Optional["GetContentContentEmailBcc"]]]


class GetContentContentEmailFrom(BaseModel):
    name: Optional[str]
    email: Optional[str]
    given_name: Optional[str] = Field(alias="givenName")
    family_name: Optional[str] = Field(alias="familyName")


class GetContentContentEmailTo(BaseModel):
    name: Optional[str]
    email: Optional[str]
    given_name: Optional[str] = Field(alias="givenName")
    family_name: Optional[str] = Field(alias="familyName")


class GetContentContentEmailCc(BaseModel):
    name: Optional[str]
    email: Optional[str]
    given_name: Optional[str] = Field(alias="givenName")
    family_name: Optional[str] = Field(alias="familyName")


class GetContentContentEmailBcc(BaseModel):
    name: Optional[str]
    email: Optional[str]
    given_name: Optional[str] = Field(alias="givenName")
    family_name: Optional[str] = Field(alias="familyName")


class GetContentContentIssue(BaseModel):
    identifier: Optional[str]
    title: Optional[str]
    project: Optional[str]
    team: Optional[str]
    status: Optional[str]
    priority: Optional[str]
    type: Optional[str]
    labels: Optional[List[Optional[str]]]


class GetContentContentPackage(BaseModel):
    file_count: Optional[int] = Field(alias="fileCount")
    folder_count: Optional[int] = Field(alias="folderCount")
    is_encrypted: Optional[bool] = Field(alias="isEncrypted")


class GetContentContentLanguage(BaseModel):
    languages: Optional[List[Optional[str]]]


class GetContentContentParent(BaseModel):
    id: str
    name: str


class GetContentContentChildren(BaseModel):
    id: str
    name: str


class GetContentContentFeed(BaseModel):
    id: str
    name: str


class GetContentContentCollections(BaseModel):
    id: str
    name: str


class GetContentContentLinks(BaseModel):
    uri: Optional[Any]
    link_type: Optional[LinkTypes] = Field(alias="linkType")


class GetContentContentObservations(BaseModel):
    id: str
    type: ObservableTypes
    observable: "GetContentContentObservationsObservable"
    related: Optional["GetContentContentObservationsRelated"]
    related_type: Optional[ObservableTypes] = Field(alias="relatedType")
    relation: Optional[str]
    occurrences: Optional[List[Optional["GetContentContentObservationsOccurrences"]]]
    state: EntityState


class GetContentContentObservationsObservable(BaseModel):
    id: str
    name: Optional[str]


class GetContentContentObservationsRelated(BaseModel):
    id: str
    name: Optional[str]


class GetContentContentObservationsOccurrences(BaseModel):
    type: Optional[OccurrenceTypes]
    confidence: Optional[float]
    start_time: Optional[Any] = Field(alias="startTime")
    end_time: Optional[Any] = Field(alias="endTime")
    page_index: Optional[int] = Field(alias="pageIndex")
    bounding_box: Optional["GetContentContentObservationsOccurrencesBoundingBox"] = (
        Field(alias="boundingBox")
    )


class GetContentContentObservationsOccurrencesBoundingBox(BaseModel):
    left: Optional[float]
    top: Optional[float]
    width: Optional[float]
    height: Optional[float]


class GetContentContentWorkflow(BaseModel):
    id: str
    name: str


class GetContentContentPages(BaseModel):
    index: Optional[int]
    text: Optional[str]
    relevance: Optional[float]
    chunks: Optional[List[Optional["GetContentContentPagesChunks"]]]


class GetContentContentPagesChunks(BaseModel):
    index: Optional[int]
    page_index: Optional[int] = Field(alias="pageIndex")
    row_index: Optional[int] = Field(alias="rowIndex")
    column_index: Optional[int] = Field(alias="columnIndex")
    confidence: Optional[float]
    text: Optional[str]
    role: Optional[TextRoles]
    relevance: Optional[float]


class GetContentContentSegments(BaseModel):
    start_time: Optional[Any] = Field(alias="startTime")
    end_time: Optional[Any] = Field(alias="endTime")
    text: Optional[str]
    relevance: Optional[float]


class GetContentContentFrames(BaseModel):
    index: Optional[int]
    description: Optional[str]
    text: Optional[str]
    relevance: Optional[float]


GetContent.model_rebuild()
GetContentContent.model_rebuild()
GetContentContentEmail.model_rebuild()
GetContentContentObservations.model_rebuild()
GetContentContentObservationsOccurrences.model_rebuild()
GetContentContentPages.model_rebuild()
