# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    ContentTypes,
    ConversationRoleTypes,
    EntityState,
    FileTypes,
    ImageProjectionTypes,
    ModelServiceTypes,
    OrientationTypes,
)


class ReviseEncodedImage(BaseModel):
    revise_encoded_image: Optional["ReviseEncodedImageReviseEncodedImage"] = Field(
        alias="reviseEncodedImage"
    )


class ReviseEncodedImageReviseEncodedImage(BaseModel):
    conversation: Optional["ReviseEncodedImageReviseEncodedImageConversation"]
    message: Optional["ReviseEncodedImageReviseEncodedImageMessage"]
    message_count: Optional[int] = Field(alias="messageCount")


class ReviseEncodedImageReviseEncodedImageConversation(BaseModel):
    id: str


class ReviseEncodedImageReviseEncodedImageMessage(BaseModel):
    role: ConversationRoleTypes
    author: Optional[str]
    message: Optional[str]
    citations: Optional[
        List[Optional["ReviseEncodedImageReviseEncodedImageMessageCitations"]]
    ]
    tool_calls: Optional[
        List[Optional["ReviseEncodedImageReviseEncodedImageMessageToolCalls"]]
    ] = Field(alias="toolCalls")
    tokens: Optional[int]
    throughput: Optional[float]
    completion_time: Optional[Any] = Field(alias="completionTime")
    timestamp: Optional[Any]
    model_service: Optional[ModelServiceTypes] = Field(alias="modelService")
    model: Optional[str]
    data: Optional[str]
    mime_type: Optional[str] = Field(alias="mimeType")


class ReviseEncodedImageReviseEncodedImageMessageCitations(BaseModel):
    content: Optional["ReviseEncodedImageReviseEncodedImageMessageCitationsContent"]
    index: Optional[int]
    text: str
    start_time: Optional[Any] = Field(alias="startTime")
    end_time: Optional[Any] = Field(alias="endTime")
    page_number: Optional[int] = Field(alias="pageNumber")
    frame_number: Optional[int] = Field(alias="frameNumber")


class ReviseEncodedImageReviseEncodedImageMessageCitationsContent(BaseModel):
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
    video: Optional["ReviseEncodedImageReviseEncodedImageMessageCitationsContentVideo"]
    audio: Optional["ReviseEncodedImageReviseEncodedImageMessageCitationsContentAudio"]
    image: Optional["ReviseEncodedImageReviseEncodedImageMessageCitationsContentImage"]
    document: Optional[
        "ReviseEncodedImageReviseEncodedImageMessageCitationsContentDocument"
    ]


class ReviseEncodedImageReviseEncodedImageMessageCitationsContentVideo(BaseModel):
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


class ReviseEncodedImageReviseEncodedImageMessageCitationsContentAudio(BaseModel):
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


class ReviseEncodedImageReviseEncodedImageMessageCitationsContentImage(BaseModel):
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


class ReviseEncodedImageReviseEncodedImageMessageCitationsContentDocument(BaseModel):
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


class ReviseEncodedImageReviseEncodedImageMessageToolCalls(BaseModel):
    id: str
    name: str
    arguments: str


ReviseEncodedImage.model_rebuild()
ReviseEncodedImageReviseEncodedImage.model_rebuild()
ReviseEncodedImageReviseEncodedImageMessage.model_rebuild()
ReviseEncodedImageReviseEncodedImageMessageCitations.model_rebuild()
ReviseEncodedImageReviseEncodedImageMessageCitationsContent.model_rebuild()
