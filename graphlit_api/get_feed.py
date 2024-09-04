# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    EmailListingTypes,
    EntityState,
    FeedListingTypes,
    FeedServiceTypes,
    FeedTypes,
    NotionTypes,
    SearchServiceTypes,
    SharePointAuthenticationTypes,
    SiteTypes,
    TimedPolicyRecurrenceTypes,
    YouTubeTypes,
)


class GetFeed(BaseModel):
    feed: Optional["GetFeedFeed"]


class GetFeedFeed(BaseModel):
    id: str
    name: str
    creation_date: Any = Field(alias="creationDate")
    relevance: Optional[float]
    owner: "GetFeedFeedOwner"
    state: EntityState
    correlation_id: Optional[str] = Field(alias="correlationId")
    type: FeedTypes
    site: Optional["GetFeedFeedSite"]
    email: Optional["GetFeedFeedEmail"]
    issue: Optional["GetFeedFeedIssue"]
    rss: Optional["GetFeedFeedRss"]
    web: Optional["GetFeedFeedWeb"]
    search: Optional["GetFeedFeedSearch"]
    reddit: Optional["GetFeedFeedReddit"]
    notion: Optional["GetFeedFeedNotion"]
    youtube: Optional["GetFeedFeedYoutube"]
    slack: Optional["GetFeedFeedSlack"]
    discord: Optional["GetFeedFeedDiscord"]
    error: Optional[str]
    last_post_date: Optional[Any] = Field(alias="lastPostDate")
    last_read_date: Optional[Any] = Field(alias="lastReadDate")
    read_count: Optional[int] = Field(alias="readCount")
    workflow: Optional["GetFeedFeedWorkflow"]
    schedule_policy: Optional["GetFeedFeedSchedulePolicy"] = Field(
        alias="schedulePolicy"
    )


class GetFeedFeedOwner(BaseModel):
    id: str


class GetFeedFeedSite(BaseModel):
    site_type: SiteTypes = Field(alias="siteType")
    type: FeedServiceTypes
    is_recursive: Optional[bool] = Field(alias="isRecursive")
    s_3: Optional["GetFeedFeedSiteS3"] = Field(alias="s3")
    azure_blob: Optional["GetFeedFeedSiteAzureBlob"] = Field(alias="azureBlob")
    azure_file: Optional["GetFeedFeedSiteAzureFile"] = Field(alias="azureFile")
    google: Optional["GetFeedFeedSiteGoogle"]
    share_point: Optional["GetFeedFeedSiteSharePoint"] = Field(alias="sharePoint")
    one_drive: Optional["GetFeedFeedSiteOneDrive"] = Field(alias="oneDrive")
    google_drive: Optional["GetFeedFeedSiteGoogleDrive"] = Field(alias="googleDrive")
    read_limit: Optional[int] = Field(alias="readLimit")


class GetFeedFeedSiteS3(BaseModel):
    access_key: Optional[str] = Field(alias="accessKey")
    secret_access_key: Optional[str] = Field(alias="secretAccessKey")
    bucket_name: Optional[str] = Field(alias="bucketName")
    prefix: Optional[str]
    region: Optional[str]


class GetFeedFeedSiteAzureBlob(BaseModel):
    storage_access_key: Optional[str] = Field(alias="storageAccessKey")
    account_name: Optional[str] = Field(alias="accountName")
    container_name: Optional[str] = Field(alias="containerName")
    prefix: Optional[str]


class GetFeedFeedSiteAzureFile(BaseModel):
    storage_access_key: Optional[str] = Field(alias="storageAccessKey")
    account_name: Optional[str] = Field(alias="accountName")
    share_name: Optional[str] = Field(alias="shareName")
    prefix: Optional[str]


class GetFeedFeedSiteGoogle(BaseModel):
    credentials: Optional[str]
    container_name: Optional[str] = Field(alias="containerName")
    prefix: Optional[str]


class GetFeedFeedSiteSharePoint(BaseModel):
    authentication_type: SharePointAuthenticationTypes = Field(
        alias="authenticationType"
    )
    account_name: str = Field(alias="accountName")
    library_id: str = Field(alias="libraryId")
    folder_id: Optional[str] = Field(alias="folderId")
    tenant_id: Optional[str] = Field(alias="tenantId")
    refresh_token: Optional[str] = Field(alias="refreshToken")


class GetFeedFeedSiteOneDrive(BaseModel):
    folder_id: Optional[str] = Field(alias="folderId")
    refresh_token: str = Field(alias="refreshToken")


class GetFeedFeedSiteGoogleDrive(BaseModel):
    folder_id: Optional[str] = Field(alias="folderId")
    refresh_token: str = Field(alias="refreshToken")
    client_id: str = Field(alias="clientId")
    client_secret: str = Field(alias="clientSecret")


class GetFeedFeedEmail(BaseModel):
    type: FeedServiceTypes
    include_attachments: Optional[bool] = Field(alias="includeAttachments")
    google: Optional["GetFeedFeedEmailGoogle"]
    microsoft: Optional["GetFeedFeedEmailMicrosoft"]
    read_limit: Optional[int] = Field(alias="readLimit")


class GetFeedFeedEmailGoogle(BaseModel):
    type: Optional[EmailListingTypes]
    refresh_token: Optional[str] = Field(alias="refreshToken")
    client_id: str = Field(alias="clientId")
    client_secret: str = Field(alias="clientSecret")


class GetFeedFeedEmailMicrosoft(BaseModel):
    type: Optional[EmailListingTypes]
    refresh_token: str = Field(alias="refreshToken")


class GetFeedFeedIssue(BaseModel):
    type: FeedServiceTypes
    include_attachments: Optional[bool] = Field(alias="includeAttachments")
    jira: Optional["GetFeedFeedIssueJira"]
    linear: Optional["GetFeedFeedIssueLinear"]
    github: Optional["GetFeedFeedIssueGithub"]
    read_limit: Optional[int] = Field(alias="readLimit")


class GetFeedFeedIssueJira(BaseModel):
    uri: Any
    project: str
    email: str
    token: str
    offset: Optional[Any]


class GetFeedFeedIssueLinear(BaseModel):
    key: str
    project: str


class GetFeedFeedIssueGithub(BaseModel):
    uri: Optional[Any]
    repository_owner: str = Field(alias="repositoryOwner")
    repository_name: str = Field(alias="repositoryName")
    refresh_token: Optional[str] = Field(alias="refreshToken")
    personal_access_token: Optional[str] = Field(alias="personalAccessToken")


class GetFeedFeedRss(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    uri: Any


class GetFeedFeedWeb(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    uri: Any
    include_files: Optional[bool] = Field(alias="includeFiles")
    allowed_paths: Optional[List[str]] = Field(alias="allowedPaths")
    excluded_paths: Optional[List[str]] = Field(alias="excludedPaths")


class GetFeedFeedSearch(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    type: Optional[SearchServiceTypes]
    text: str


class GetFeedFeedReddit(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    subreddit_name: str = Field(alias="subredditName")


class GetFeedFeedNotion(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    token: str
    identifiers: List[str]
    type: NotionTypes


class GetFeedFeedYoutube(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    type: YouTubeTypes
    video_name: Optional[str] = Field(alias="videoName")
    video_identifiers: Optional[List[str]] = Field(alias="videoIdentifiers")
    channel_identifier: Optional[str] = Field(alias="channelIdentifier")
    playlist_identifier: Optional[str] = Field(alias="playlistIdentifier")


class GetFeedFeedSlack(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    type: Optional[FeedListingTypes]
    token: str
    channel: str
    include_attachments: Optional[bool] = Field(alias="includeAttachments")


class GetFeedFeedDiscord(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    type: Optional[FeedListingTypes]
    token: str
    channel: str
    include_attachments: Optional[bool] = Field(alias="includeAttachments")


class GetFeedFeedWorkflow(BaseModel):
    id: str
    name: str


class GetFeedFeedSchedulePolicy(BaseModel):
    recurrence_type: Optional[TimedPolicyRecurrenceTypes] = Field(
        alias="recurrenceType"
    )
    repeat_interval: Optional[Any] = Field(alias="repeatInterval")


GetFeed.model_rebuild()
GetFeedFeed.model_rebuild()
GetFeedFeedSite.model_rebuild()
GetFeedFeedEmail.model_rebuild()
GetFeedFeedIssue.model_rebuild()
