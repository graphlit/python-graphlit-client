# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    AnthropicModels,
    AzureOpenAIModels,
    CerebrasModels,
    CohereModels,
    ConversationSearchTypes,
    ConversationStrategyTypes,
    DeepseekModels,
    EntityState,
    GoogleModels,
    GraphStrategyTypes,
    GroqModels,
    JinaModels,
    MistralModels,
    ModelServiceTypes,
    OpenAIModels,
    PromptStrategyTypes,
    ReplicateModels,
    RerankingModelServiceTypes,
    RetrievalStrategyTypes,
    RevisionStrategyTypes,
    SpecificationTypes,
    VoyageModels,
)


class QuerySpecifications(BaseModel):
    specifications: Optional["QuerySpecificationsSpecifications"]


class QuerySpecificationsSpecifications(BaseModel):
    results: Optional[List[Optional["QuerySpecificationsSpecificationsResults"]]]


class QuerySpecificationsSpecificationsResults(BaseModel):
    id: str
    name: str
    creation_date: Any = Field(alias="creationDate")
    relevance: Optional[float]
    owner: "QuerySpecificationsSpecificationsResultsOwner"
    state: EntityState
    type: Optional[SpecificationTypes]
    service_type: Optional[ModelServiceTypes] = Field(alias="serviceType")
    system_prompt: Optional[str] = Field(alias="systemPrompt")
    custom_guidance: Optional[str] = Field(alias="customGuidance")
    custom_instructions: Optional[str] = Field(alias="customInstructions")
    search_type: Optional[ConversationSearchTypes] = Field(alias="searchType")
    number_similar: Optional[int] = Field(alias="numberSimilar")
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
    graph_strategy: Optional[
        "QuerySpecificationsSpecificationsResultsGraphStrategy"
    ] = Field(alias="graphStrategy")
    revision_strategy: Optional[
        "QuerySpecificationsSpecificationsResultsRevisionStrategy"
    ] = Field(alias="revisionStrategy")
    azure_ai: Optional["QuerySpecificationsSpecificationsResultsAzureAi"] = Field(
        alias="azureAI"
    )
    open_ai: Optional["QuerySpecificationsSpecificationsResultsOpenAi"] = Field(
        alias="openAI"
    )
    azure_open_ai: Optional["QuerySpecificationsSpecificationsResultsAzureOpenAi"] = (
        Field(alias="azureOpenAI")
    )
    cohere: Optional["QuerySpecificationsSpecificationsResultsCohere"]
    anthropic: Optional["QuerySpecificationsSpecificationsResultsAnthropic"]
    google: Optional["QuerySpecificationsSpecificationsResultsGoogle"]
    replicate: Optional["QuerySpecificationsSpecificationsResultsReplicate"]
    mistral: Optional["QuerySpecificationsSpecificationsResultsMistral"]
    groq: Optional["QuerySpecificationsSpecificationsResultsGroq"]
    cerebras: Optional["QuerySpecificationsSpecificationsResultsCerebras"]
    deepseek: Optional["QuerySpecificationsSpecificationsResultsDeepseek"]
    jina: Optional["QuerySpecificationsSpecificationsResultsJina"]
    voyage: Optional["QuerySpecificationsSpecificationsResultsVoyage"]


class QuerySpecificationsSpecificationsResultsOwner(BaseModel):
    id: str


class QuerySpecificationsSpecificationsResultsStrategy(BaseModel):
    type: Optional[ConversationStrategyTypes]
    message_limit: Optional[int] = Field(alias="messageLimit")
    embed_citations: Optional[bool] = Field(alias="embedCitations")
    flatten_citations: Optional[bool] = Field(alias="flattenCitations")
    enable_facets: Optional[bool] = Field(alias="enableFacets")
    disable_guardrails: Optional[bool] = Field(alias="disableGuardrails")
    messages_weight: Optional[float] = Field(alias="messagesWeight")
    contents_weight: Optional[float] = Field(alias="contentsWeight")


class QuerySpecificationsSpecificationsResultsPromptStrategy(BaseModel):
    type: PromptStrategyTypes


class QuerySpecificationsSpecificationsResultsRetrievalStrategy(BaseModel):
    type: RetrievalStrategyTypes
    content_limit: Optional[int] = Field(alias="contentLimit")
    disable_fallback: Optional[bool] = Field(alias="disableFallback")


class QuerySpecificationsSpecificationsResultsRerankingStrategy(BaseModel):
    service_type: RerankingModelServiceTypes = Field(alias="serviceType")
    threshold: Optional[float]


class QuerySpecificationsSpecificationsResultsGraphStrategy(BaseModel):
    type: GraphStrategyTypes
    generate_graph: Optional[bool] = Field(alias="generateGraph")
    observable_limit: Optional[int] = Field(alias="observableLimit")


class QuerySpecificationsSpecificationsResultsRevisionStrategy(BaseModel):
    type: RevisionStrategyTypes
    custom_revision: Optional[str] = Field(alias="customRevision")
    count: Optional[int]


class QuerySpecificationsSpecificationsResultsAzureAi(BaseModel):
    token_limit: int = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    key: str
    endpoint: Any
    temperature: Optional[float]
    probability: Optional[float]
    chunk_token_limit: Optional[int] = Field(alias="chunkTokenLimit")


class QuerySpecificationsSpecificationsResultsOpenAi(BaseModel):
    token_limit: Optional[int] = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    model: OpenAIModels
    key: Optional[str]
    model_name: Optional[str] = Field(alias="modelName")
    temperature: Optional[float]
    probability: Optional[float]
    chunk_token_limit: Optional[int] = Field(alias="chunkTokenLimit")


class QuerySpecificationsSpecificationsResultsAzureOpenAi(BaseModel):
    token_limit: Optional[int] = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    model: AzureOpenAIModels
    key: Optional[str]
    endpoint: Optional[Any]
    deployment_name: Optional[str] = Field(alias="deploymentName")
    temperature: Optional[float]
    probability: Optional[float]
    chunk_token_limit: Optional[int] = Field(alias="chunkTokenLimit")


class QuerySpecificationsSpecificationsResultsCohere(BaseModel):
    token_limit: Optional[int] = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    model: CohereModels
    key: Optional[str]
    model_name: Optional[str] = Field(alias="modelName")
    temperature: Optional[float]
    probability: Optional[float]
    chunk_token_limit: Optional[int] = Field(alias="chunkTokenLimit")


class QuerySpecificationsSpecificationsResultsAnthropic(BaseModel):
    token_limit: Optional[int] = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    model: AnthropicModels
    key: Optional[str]
    model_name: Optional[str] = Field(alias="modelName")
    temperature: Optional[float]
    probability: Optional[float]


class QuerySpecificationsSpecificationsResultsGoogle(BaseModel):
    token_limit: Optional[int] = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    model: GoogleModels
    key: Optional[str]
    model_name: Optional[str] = Field(alias="modelName")
    temperature: Optional[float]
    probability: Optional[float]
    chunk_token_limit: Optional[int] = Field(alias="chunkTokenLimit")


class QuerySpecificationsSpecificationsResultsReplicate(BaseModel):
    token_limit: Optional[int] = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    model: ReplicateModels
    key: Optional[str]
    model_name: Optional[str] = Field(alias="modelName")
    temperature: Optional[float]
    probability: Optional[float]


class QuerySpecificationsSpecificationsResultsMistral(BaseModel):
    token_limit: Optional[int] = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    model: MistralModels
    key: Optional[str]
    model_name: Optional[str] = Field(alias="modelName")
    endpoint: Optional[Any]
    temperature: Optional[float]
    probability: Optional[float]
    chunk_token_limit: Optional[int] = Field(alias="chunkTokenLimit")


class QuerySpecificationsSpecificationsResultsGroq(BaseModel):
    token_limit: Optional[int] = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    model: GroqModels
    key: Optional[str]
    model_name: Optional[str] = Field(alias="modelName")
    endpoint: Optional[Any]
    temperature: Optional[float]
    probability: Optional[float]


class QuerySpecificationsSpecificationsResultsCerebras(BaseModel):
    token_limit: Optional[int] = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    model: CerebrasModels
    key: Optional[str]
    model_name: Optional[str] = Field(alias="modelName")
    endpoint: Optional[Any]
    temperature: Optional[float]
    probability: Optional[float]


class QuerySpecificationsSpecificationsResultsDeepseek(BaseModel):
    token_limit: Optional[int] = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    model: DeepseekModels
    key: Optional[str]
    model_name: Optional[str] = Field(alias="modelName")
    temperature: Optional[float]
    probability: Optional[float]


class QuerySpecificationsSpecificationsResultsJina(BaseModel):
    model: JinaModels
    key: Optional[str]
    model_name: Optional[str] = Field(alias="modelName")
    chunk_token_limit: Optional[int] = Field(alias="chunkTokenLimit")


class QuerySpecificationsSpecificationsResultsVoyage(BaseModel):
    model: VoyageModels
    key: Optional[str]
    model_name: Optional[str] = Field(alias="modelName")
    chunk_token_limit: Optional[int] = Field(alias="chunkTokenLimit")


QuerySpecifications.model_rebuild()
QuerySpecificationsSpecifications.model_rebuild()
QuerySpecificationsSpecificationsResults.model_rebuild()
