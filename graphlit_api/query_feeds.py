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


class QueryFeeds(BaseModel):
    feeds: Optional["QueryFeedsFeeds"]


class QueryFeedsFeeds(BaseModel):
    results: Optional[List[Optional["QueryFeedsFeedsResults"]]]


class QueryFeedsFeedsResults(BaseModel):
    id: str
    name: str
    creation_date: Any = Field(alias="creationDate")
    relevance: Optional[float]
    owner: "QueryFeedsFeedsResultsOwner"
    state: EntityState
    correlation_id: Optional[str] = Field(alias="correlationId")
    type: FeedTypes
    site: Optional["QueryFeedsFeedsResultsSite"]
    email: Optional["QueryFeedsFeedsResultsEmail"]
    issue: Optional["QueryFeedsFeedsResultsIssue"]
    rss: Optional["QueryFeedsFeedsResultsRss"]
    web: Optional["QueryFeedsFeedsResultsWeb"]
    search: Optional["QueryFeedsFeedsResultsSearch"]
    reddit: Optional["QueryFeedsFeedsResultsReddit"]
    notion: Optional["QueryFeedsFeedsResultsNotion"]
    intercom: Optional["QueryFeedsFeedsResultsIntercom"]
    zendesk: Optional["QueryFeedsFeedsResultsZendesk"]
    youtube: Optional["QueryFeedsFeedsResultsYoutube"]
    slack: Optional["QueryFeedsFeedsResultsSlack"]
    microsoft_teams: Optional["QueryFeedsFeedsResultsMicrosoftTeams"] = Field(
        alias="microsoftTeams"
    )
    discord: Optional["QueryFeedsFeedsResultsDiscord"]
    error: Optional[str]
    last_post_date: Optional[Any] = Field(alias="lastPostDate")
    last_read_date: Optional[Any] = Field(alias="lastReadDate")
    read_count: Optional[int] = Field(alias="readCount")
    workflow: Optional["QueryFeedsFeedsResultsWorkflow"]
    schedule_policy: Optional["QueryFeedsFeedsResultsSchedulePolicy"] = Field(
        alias="schedulePolicy"
    )


class QueryFeedsFeedsResultsOwner(BaseModel):
    id: str


class QueryFeedsFeedsResultsSite(BaseModel):
    site_type: SiteTypes = Field(alias="siteType")
    type: FeedServiceTypes
    is_recursive: Optional[bool] = Field(alias="isRecursive")
    s_3: Optional["QueryFeedsFeedsResultsSiteS3"] = Field(alias="s3")
    azure_blob: Optional["QueryFeedsFeedsResultsSiteAzureBlob"] = Field(
        alias="azureBlob"
    )
    azure_file: Optional["QueryFeedsFeedsResultsSiteAzureFile"] = Field(
        alias="azureFile"
    )
    google: Optional["QueryFeedsFeedsResultsSiteGoogle"]
    share_point: Optional["QueryFeedsFeedsResultsSiteSharePoint"] = Field(
        alias="sharePoint"
    )
    one_drive: Optional["QueryFeedsFeedsResultsSiteOneDrive"] = Field(alias="oneDrive")
    google_drive: Optional["QueryFeedsFeedsResultsSiteGoogleDrive"] = Field(
        alias="googleDrive"
    )
    dropbox: Optional["QueryFeedsFeedsResultsSiteDropbox"]
    box: Optional["QueryFeedsFeedsResultsSiteBox"]
    github: Optional["QueryFeedsFeedsResultsSiteGithub"]
    read_limit: Optional[int] = Field(alias="readLimit")


class QueryFeedsFeedsResultsSiteS3(BaseModel):
    access_key: Optional[str] = Field(alias="accessKey")
    secret_access_key: Optional[str] = Field(alias="secretAccessKey")
    bucket_name: Optional[str] = Field(alias="bucketName")
    prefix: Optional[str]
    region: Optional[str]


class QueryFeedsFeedsResultsSiteAzureBlob(BaseModel):
    storage_access_key: Optional[str] = Field(alias="storageAccessKey")
    account_name: Optional[str] = Field(alias="accountName")
    container_name: Optional[str] = Field(alias="containerName")
    prefix: Optional[str]


class QueryFeedsFeedsResultsSiteAzureFile(BaseModel):
    storage_access_key: Optional[str] = Field(alias="storageAccessKey")
    account_name: Optional[str] = Field(alias="accountName")
    share_name: Optional[str] = Field(alias="shareName")
    prefix: Optional[str]


class QueryFeedsFeedsResultsSiteGoogle(BaseModel):
    credentials: Optional[str]
    container_name: Optional[str] = Field(alias="containerName")
    prefix: Optional[str]


class QueryFeedsFeedsResultsSiteSharePoint(BaseModel):
    authentication_type: SharePointAuthenticationTypes = Field(
        alias="authenticationType"
    )
    account_name: str = Field(alias="accountName")
    library_id: str = Field(alias="libraryId")
    folder_id: Optional[str] = Field(alias="folderId")
    tenant_id: Optional[str] = Field(alias="tenantId")
    client_id: Optional[str] = Field(alias="clientId")
    client_secret: Optional[str] = Field(alias="clientSecret")
    refresh_token: Optional[str] = Field(alias="refreshToken")


class QueryFeedsFeedsResultsSiteOneDrive(BaseModel):
    folder_id: Optional[str] = Field(alias="folderId")
    files: Optional[List[Optional[str]]]
    client_id: str = Field(alias="clientId")
    client_secret: str = Field(alias="clientSecret")
    refresh_token: str = Field(alias="refreshToken")


class QueryFeedsFeedsResultsSiteGoogleDrive(BaseModel):
    folder_id: Optional[str] = Field(alias="folderId")
    files: Optional[List[Optional[str]]]
    refresh_token: str = Field(alias="refreshToken")
    client_id: str = Field(alias="clientId")
    client_secret: str = Field(alias="clientSecret")


class QueryFeedsFeedsResultsSiteDropbox(BaseModel):
    path: Optional[str]
    app_key: str = Field(alias="appKey")
    app_secret: str = Field(alias="appSecret")
    refresh_token: str = Field(alias="refreshToken")
    redirect_uri: str = Field(alias="redirectUri")


class QueryFeedsFeedsResultsSiteBox(BaseModel):
    folder_id: Optional[str] = Field(alias="folderId")
    client_id: str = Field(alias="clientId")
    client_secret: str = Field(alias="clientSecret")
    refresh_token: str = Field(alias="refreshToken")
    redirect_uri: str = Field(alias="redirectUri")


class QueryFeedsFeedsResultsSiteGithub(BaseModel):
    uri: Optional[Any]
    repository_owner: str = Field(alias="repositoryOwner")
    repository_name: str = Field(alias="repositoryName")
    refresh_token: Optional[str] = Field(alias="refreshToken")
    personal_access_token: Optional[str] = Field(alias="personalAccessToken")


class QueryFeedsFeedsResultsEmail(BaseModel):
    type: FeedServiceTypes
    include_attachments: Optional[bool] = Field(alias="includeAttachments")
    google: Optional["QueryFeedsFeedsResultsEmailGoogle"]
    microsoft: Optional["QueryFeedsFeedsResultsEmailMicrosoft"]
    read_limit: Optional[int] = Field(alias="readLimit")


class QueryFeedsFeedsResultsEmailGoogle(BaseModel):
    type: Optional[EmailListingTypes]
    refresh_token: Optional[str] = Field(alias="refreshToken")
    client_id: str = Field(alias="clientId")
    client_secret: str = Field(alias="clientSecret")


class QueryFeedsFeedsResultsEmailMicrosoft(BaseModel):
    type: Optional[EmailListingTypes]
    refresh_token: str = Field(alias="refreshToken")
    client_id: str = Field(alias="clientId")
    client_secret: str = Field(alias="clientSecret")


class QueryFeedsFeedsResultsIssue(BaseModel):
    type: FeedServiceTypes
    include_attachments: Optional[bool] = Field(alias="includeAttachments")
    jira: Optional["QueryFeedsFeedsResultsIssueJira"]
    linear: Optional["QueryFeedsFeedsResultsIssueLinear"]
    github: Optional["QueryFeedsFeedsResultsIssueGithub"]
    intercom: Optional["QueryFeedsFeedsResultsIssueIntercom"]
    zendesk: Optional["QueryFeedsFeedsResultsIssueZendesk"]
    read_limit: Optional[int] = Field(alias="readLimit")


class QueryFeedsFeedsResultsIssueJira(BaseModel):
    uri: Any
    project: str
    email: str
    token: str
    offset: Optional[Any]


class QueryFeedsFeedsResultsIssueLinear(BaseModel):
    key: str
    project: str


class QueryFeedsFeedsResultsIssueGithub(BaseModel):
    uri: Optional[Any]
    repository_owner: str = Field(alias="repositoryOwner")
    repository_name: str = Field(alias="repositoryName")
    refresh_token: Optional[str] = Field(alias="refreshToken")
    personal_access_token: Optional[str] = Field(alias="personalAccessToken")


class QueryFeedsFeedsResultsIssueIntercom(BaseModel):
    access_token: str = Field(alias="accessToken")


class QueryFeedsFeedsResultsIssueZendesk(BaseModel):
    subdomain: str
    access_token: str = Field(alias="accessToken")


class QueryFeedsFeedsResultsRss(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    uri: Any


class QueryFeedsFeedsResultsWeb(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    uri: Any
    include_files: Optional[bool] = Field(alias="includeFiles")
    allowed_paths: Optional[List[str]] = Field(alias="allowedPaths")
    excluded_paths: Optional[List[str]] = Field(alias="excludedPaths")


class QueryFeedsFeedsResultsSearch(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    type: Optional[SearchServiceTypes]
    text: str


class QueryFeedsFeedsResultsReddit(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    subreddit_name: str = Field(alias="subredditName")


class QueryFeedsFeedsResultsNotion(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    token: str
    identifiers: List[str]
    type: NotionTypes


class QueryFeedsFeedsResultsIntercom(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    access_token: str = Field(alias="accessToken")


class QueryFeedsFeedsResultsZendesk(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    subdomain: str
    access_token: str = Field(alias="accessToken")


class QueryFeedsFeedsResultsYoutube(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    type: YouTubeTypes
    video_name: Optional[str] = Field(alias="videoName")
    video_identifiers: Optional[List[str]] = Field(alias="videoIdentifiers")
    channel_identifier: Optional[str] = Field(alias="channelIdentifier")
    playlist_identifier: Optional[str] = Field(alias="playlistIdentifier")


class QueryFeedsFeedsResultsSlack(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    type: Optional[FeedListingTypes]
    token: str
    channel: str
    include_attachments: Optional[bool] = Field(alias="includeAttachments")


class QueryFeedsFeedsResultsMicrosoftTeams(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    type: Optional[FeedListingTypes]
    client_id: str = Field(alias="clientId")
    client_secret: str = Field(alias="clientSecret")
    refresh_token: str = Field(alias="refreshToken")
    team_id: str = Field(alias="teamId")
    channel_id: str = Field(alias="channelId")


class QueryFeedsFeedsResultsDiscord(BaseModel):
    read_limit: Optional[int] = Field(alias="readLimit")
    type: Optional[FeedListingTypes]
    token: str
    channel: str
    include_attachments: Optional[bool] = Field(alias="includeAttachments")


class QueryFeedsFeedsResultsWorkflow(BaseModel):
    id: str
    name: str


class QueryFeedsFeedsResultsSchedulePolicy(BaseModel):
    recurrence_type: Optional[TimedPolicyRecurrenceTypes] = Field(
        alias="recurrenceType"
    )
    repeat_interval: Optional[Any] = Field(alias="repeatInterval")


QueryFeeds.model_rebuild()
QueryFeedsFeeds.model_rebuild()
QueryFeedsFeedsResults.model_rebuild()
QueryFeedsFeedsResultsSite.model_rebuild()
QueryFeedsFeedsResultsEmail.model_rebuild()
QueryFeedsFeedsResultsIssue.model_rebuild()
