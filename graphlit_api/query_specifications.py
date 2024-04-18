# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    AnthropicModels,
    AzureOpenAIModels,
    ConversationStrategyTypes,
    EntityState,
    ModelServiceTypes,
    OpenAIModels,
    PromptStrategyTypes,
    ReplicateModels,
    RetrievalStrategyTypes,
    SpecificationTypes,
)


class QuerySpecifications(BaseModel):
    specifications: Optional["QuerySpecificationsSpecifications"]


class QuerySpecificationsSpecifications(BaseModel):
    results: Optional[List[Optional["QuerySpecificationsSpecificationsResults"]]]


class QuerySpecificationsSpecificationsResults(BaseModel):
    id: str
    name: str
    creation_date: Any = Field(alias="creationDate")
    owner: "QuerySpecificationsSpecificationsResultsOwner"
    state: EntityState
    type: Optional[SpecificationTypes]
    service_type: Optional[ModelServiceTypes] = Field(alias="serviceType")
    system_prompt: Optional[str] = Field(alias="systemPrompt")
    custom_guidance: Optional[str] = Field(alias="customGuidance")
    strategy: Optional["QuerySpecificationsSpecificationsResultsStrategy"]
    prompt_strategy: Optional[
        "QuerySpecificationsSpecificationsResultsPromptStrategy"
    ] = Field(alias="promptStrategy")
    retrieval_strategy: Optional[
        "QuerySpecificationsSpecificationsResultsRetrievalStrategy"
    ] = Field(alias="retrievalStrategy")
    reranking_strategy: Optional[
        "QuerySpecificationsSpecificationsResultsRerankingStrategy"
    ] = Field(alias="rerankingStrategy")
    open_ai: Optional["QuerySpecificationsSpecificationsResultsOpenAi"] = Field(
        alias="openAI"
    )
    azure_open_ai: Optional["QuerySpecificationsSpecificationsResultsAzureOpenAi"] = (
        Field(alias="azureOpenAI")
    )
    anthropic: Optional["QuerySpecificationsSpecificationsResultsAnthropic"]
    replicate: Optional["QuerySpecificationsSpecificationsResultsReplicate"]
    tools: Optional[List["QuerySpecificationsSpecificationsResultsTools"]]


class QuerySpecificationsSpecificationsResultsOwner(BaseModel):
    id: str


class QuerySpecificationsSpecificationsResultsStrategy(BaseModel):
    type: ConversationStrategyTypes
    message_limit: Optional[int] = Field(alias="messageLimit")
    embed_citations: Optional[bool] = Field(alias="embedCitations")
    enable_facets: Optional[bool] = Field(alias="enableFacets")
    messages_weight: Optional[float] = Field(alias="messagesWeight")
    contents_weight: Optional[float] = Field(alias="contentsWeight")


class QuerySpecificationsSpecificationsResultsPromptStrategy(BaseModel):
    type: PromptStrategyTypes


class QuerySpecificationsSpecificationsResultsRetrievalStrategy(BaseModel):
    type: RetrievalStrategyTypes
    content_limit: Optional[int] = Field(alias="contentLimit")


class QuerySpecificationsSpecificationsResultsRerankingStrategy(BaseModel):
    service_type: ModelServiceTypes = Field(alias="serviceType")


class QuerySpecificationsSpecificationsResultsOpenAi(BaseModel):
    token_limit: Optional[int] = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    model: OpenAIModels
    key: Optional[str]
    model_name: Optional[str] = Field(alias="modelName")
    temperature: Optional[float]
    probability: Optional[float]


class QuerySpecificationsSpecificationsResultsAzureOpenAi(BaseModel):
    token_limit: Optional[int] = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    model: AzureOpenAIModels
    key: Optional[str]
    endpoint: Optional[Any]
    deployment_name: Optional[str] = Field(alias="deploymentName")
    temperature: Optional[float]
    probability: Optional[float]


class QuerySpecificationsSpecificationsResultsAnthropic(BaseModel):
    token_limit: Optional[int] = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    model: AnthropicModels
    key: Optional[str]
    model_name: Optional[str] = Field(alias="modelName")
    temperature: Optional[float]
    probability: Optional[float]


class QuerySpecificationsSpecificationsResultsReplicate(BaseModel):
    token_limit: Optional[int] = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    model: ReplicateModels
    key: Optional[str]
    model_name: Optional[str] = Field(alias="modelName")
    temperature: Optional[float]
    probability: Optional[float]


class QuerySpecificationsSpecificationsResultsTools(BaseModel):
    name: str
    description: Optional[str]
    schema_: str = Field(alias="schema")
    uri: Optional[Any]


QuerySpecifications.model_rebuild()
QuerySpecificationsSpecifications.model_rebuild()
QuerySpecificationsSpecificationsResults.model_rebuild()
