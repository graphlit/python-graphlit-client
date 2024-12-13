# Generated by ariadne-codegen
# Source: https://data-scus.graphlit.io/api/v1/graphql

from enum import Enum


class OpenAIModels(str, Enum):
    GPT35_TURBO = "GPT35_TURBO"
    GPT35_TURBO_0613 = "GPT35_TURBO_0613"
    GPT35_TURBO_16K = "GPT35_TURBO_16K"
    GPT35_TURBO_16K_0613 = "GPT35_TURBO_16K_0613"
    GPT35_TURBO_16K_1106 = "GPT35_TURBO_16K_1106"
    GPT35_TURBO_16K_0125 = "GPT35_TURBO_16K_0125"
    GPT4 = "GPT4"
    GPT4_0613 = "GPT4_0613"
    GPT4_TURBO_VISION_128K = "GPT4_TURBO_VISION_128K"
    GPT4_TURBO_VISION_128K_1106 = "GPT4_TURBO_VISION_128K_1106"
    GPT4_32K = "GPT4_32K"
    GPT4_32K_0613 = "GPT4_32K_0613"
    GPT4_TURBO_128K = "GPT4_TURBO_128K"
    GPT4_TURBO_128K_1106 = "GPT4_TURBO_128K_1106"
    GPT4_TURBO_128K_0125 = "GPT4_TURBO_128K_0125"
    GPT4_TURBO_128K_20240409 = "GPT4_TURBO_128K_20240409"
    GPT4O_128K_20240513 = "GPT4O_128K_20240513"
    GPT4O_128K_20240806 = "GPT4O_128K_20240806"
    GPT4O_128K_20241120 = "GPT4O_128K_20241120"
    GPT4O_128K = "GPT4O_128K"
    GPT4O_MINI_128K_20240718 = "GPT4O_MINI_128K_20240718"
    GPT4O_MINI_128K = "GPT4O_MINI_128K"
    GPT4O_CHAT_128K = "GPT4O_CHAT_128K"
    O1_MINI_128K = "O1_MINI_128K"
    O1_MINI_128K_20240912 = "O1_MINI_128K_20240912"
    O1_PREVIEW_128K = "O1_PREVIEW_128K"
    O1_PREVIEW_128K_20240912 = "O1_PREVIEW_128K_20240912"
    ADA_002 = "ADA_002"
    EMBEDDING_3_SMALL = "EMBEDDING_3_SMALL"
    EMBEDDING_3_LARGE = "EMBEDDING_3_LARGE"
    CUSTOM = "CUSTOM"


class ConversationStrategyTypes(str, Enum):
    WINDOWED = "WINDOWED"
    SUMMARIZED = "SUMMARIZED"


class AzureOpenAIModels(str, Enum):
    GPT35_TURBO_16K = "GPT35_TURBO_16K"
    GPT4 = "GPT4"
    GPT4_TURBO_128K = "GPT4_TURBO_128K"
    CUSTOM = "CUSTOM"


class EntityEnrichmentServiceTypes(str, Enum):
    DIFFBOT = "DIFFBOT"
    WIKIPEDIA = "WIKIPEDIA"
    CRUNCHBASE = "CRUNCHBASE"
    FHIR = "FHIR"


class SummarizationTypes(str, Enum):
    SUMMARY = "SUMMARY"
    KEYWORDS = "KEYWORDS"
    BULLETS = "BULLETS"
    HEADLINES = "HEADLINES"
    POSTS = "POSTS"
    CHAPTERS = "CHAPTERS"
    QUESTIONS = "QUESTIONS"
    CUSTOM = "CUSTOM"


class EntityState(str, Enum):
    INITIALIZED = "INITIALIZED"
    RESTARTED = "RESTARTED"
    CREATED = "CREATED"
    INGESTED = "INGESTED"
    INDEXED = "INDEXED"
    PREPARED = "PREPARED"
    SANITIZED = "SANITIZED"
    EXTRACTED = "EXTRACTED"
    ENRICHED = "ENRICHED"
    CHANGED = "CHANGED"
    ARCHIVED = "ARCHIVED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    PENDING = "PENDING"
    QUEUED = "QUEUED"
    OPENED = "OPENED"
    CLOSED = "CLOSED"
    FINISHED = "FINISHED"
    PAUSED = "PAUSED"
    RUNNING = "RUNNING"
    SUBSCRIBED = "SUBSCRIBED"
    ERRORED = "ERRORED"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    DELETED = "DELETED"


class ContentFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"
    ORIGINAL_DATE = "ORIGINAL_DATE"
    OBSERVABLE = "OBSERVABLE"
    CONTENT_TYPE = "CONTENT_TYPE"
    FILE_TYPE = "FILE_TYPE"
    FORMAT = "FORMAT"
    FORMAT_NAME = "FORMAT_NAME"
    FILE_EXTENSION = "FILE_EXTENSION"
    FILE_SIZE = "FILE_SIZE"
    DEVICE_TYPE = "DEVICE_TYPE"
    IMAGE_MAKE = "IMAGE_MAKE"
    IMAGE_MODEL = "IMAGE_MODEL"
    IMAGE_SOFTWARE = "IMAGE_SOFTWARE"
    AUDIO_AUTHOR = "AUDIO_AUTHOR"
    AUDIO_SERIES = "AUDIO_SERIES"
    AUDIO_PUBLISHER = "AUDIO_PUBLISHER"
    VIDEO_MAKE = "VIDEO_MAKE"
    VIDEO_MODEL = "VIDEO_MODEL"
    VIDEO_SOFTWARE = "VIDEO_SOFTWARE"
    DOCUMENT_AUTHOR = "DOCUMENT_AUTHOR"
    DOCUMENT_PUBLISHER = "DOCUMENT_PUBLISHER"
    DOCUMENT_IS_ENCRYPTED = "DOCUMENT_IS_ENCRYPTED"
    DOCUMENT_HAS_DIGITAL_SIGNATURE = "DOCUMENT_HAS_DIGITAL_SIGNATURE"
    EMAIL_PRIORITY = "EMAIL_PRIORITY"
    EMAIL_SENSITIVITY = "EMAIL_SENSITIVITY"
    ISSUE_PROJECT = "ISSUE_PROJECT"
    ISSUE_TEAM = "ISSUE_TEAM"
    ISSUE_PRIORITY = "ISSUE_PRIORITY"
    ISSUE_STATUS = "ISSUE_STATUS"
    ISSUE_TYPE = "ISSUE_TYPE"


class MedicalDrugClassFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class ConversationSearchTypes(str, Enum):
    NONE = "NONE"
    VECTOR = "VECTOR"
    HYBRID = "HYBRID"


class H3ResolutionTypes(str, Enum):
    R0 = "R0"
    R1 = "R1"
    R2 = "R2"
    R3 = "R3"
    R4 = "R4"
    R5 = "R5"
    R6 = "R6"
    R7 = "R7"
    R8 = "R8"
    R9 = "R9"
    R10 = "R10"
    R11 = "R11"
    R12 = "R12"
    R13 = "R13"
    R14 = "R14"
    R15 = "R15"


class ContentTypes(str, Enum):
    FILE = "FILE"
    PAGE = "PAGE"
    MESSAGE = "MESSAGE"
    TEXT = "TEXT"
    POST = "POST"
    EMAIL = "EMAIL"
    EVENT = "EVENT"
    ISSUE = "ISSUE"


class CerebrasModels(str, Enum):
    LLAMA_3_1_70B = "LLAMA_3_1_70B"
    LLAMA_3_1_8B = "LLAMA_3_1_8B"
    CUSTOM = "CUSTOM"


class TextTypes(str, Enum):
    PLAIN = "PLAIN"
    MARKDOWN = "MARKDOWN"
    HTML = "HTML"


class OperationTypes(str, Enum):
    QUERY = "QUERY"
    MUTATION = "MUTATION"


class ContentIndexingServiceTypes(str, Enum):
    AZURE_AI_LANGUAGE = "AZURE_AI_LANGUAGE"


class OrganizationFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class LabelFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class SiteTypes(str, Enum):
    WATCH = "WATCH"
    SWEEP = "SWEEP"
    STORAGE = "STORAGE"


class ModelServiceTypes(str, Enum):
    GOOGLE = "GOOGLE"
    ANTHROPIC = "ANTHROPIC"
    AZURE_AI = "AZURE_AI"
    AZURE_OPEN_AI = "AZURE_OPEN_AI"
    OPEN_AI = "OPEN_AI"
    REPLICATE = "REPLICATE"
    GROQ = "GROQ"
    CEREBRAS = "CEREBRAS"
    MISTRAL = "MISTRAL"
    COHERE = "COHERE"
    DEEPSEEK = "DEEPSEEK"
    JINA = "JINA"
    VOYAGE = "VOYAGE"


class MedicalStudyFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class CollectionTypes(str, Enum):
    COLLECTION = "COLLECTION"


class MedicalDeviceFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class AlertTypes(str, Enum):
    PROMPT = "PROMPT"


class RetrievalStrategyTypes(str, Enum):
    CONTENT = "CONTENT"
    CHUNK = "CHUNK"
    SECTION = "SECTION"


class SearchQueryTypes(str, Enum):
    SIMPLE = "SIMPLE"
    FULL = "FULL"


class IntegrationServiceTypes(str, Enum):
    SLACK = "SLACK"
    WEB_HOOK = "WEB_HOOK"


class LinkTypes(str, Enum):
    TYPE_FORM = "TYPE_FORM"
    AIRTABLE = "AIRTABLE"
    MICROSOFT_TEAMS = "MICROSOFT_TEAMS"
    DISCORD = "DISCORD"
    APPLE = "APPLE"
    SLACK = "SLACK"
    ANGEL_LIST = "ANGEL_LIST"
    CRUNCHBASE = "CRUNCHBASE"
    LINKED_IN = "LINKED_IN"
    DIFFBOT = "DIFFBOT"
    REDDIT = "REDDIT"
    GOOGLE = "GOOGLE"
    IFTTT = "IFTTT"
    FACEBOOK = "FACEBOOK"
    WIKIPEDIA = "WIKIPEDIA"
    WIKIMEDIA = "WIKIMEDIA"
    WIKIDATA = "WIKIDATA"
    INSTAGRAM = "INSTAGRAM"
    TWITCH = "TWITCH"
    POCKET_CASTS = "POCKET_CASTS"
    SPOTIFY = "SPOTIFY"
    TUNE_IN = "TUNE_IN"
    STITCHER = "STITCHER"
    ANCHOR_FM = "ANCHOR_FM"
    TRANSISTOR_FM = "TRANSISTOR_FM"
    I_TUNES = "I_TUNES"
    PANDORA = "PANDORA"
    SOUND_CLOUD = "SOUND_CLOUD"
    BANDCAMP = "BANDCAMP"
    TIK_TOK = "TIK_TOK"
    YOU_TUBE = "YOU_TUBE"
    TWITTER = "TWITTER"
    X = "X"
    MEDIUM = "MEDIUM"
    NOTION = "NOTION"
    LINEAR = "LINEAR"
    GIT_HUB = "GIT_HUB"
    GIT_HUB_PAGES = "GIT_HUB_PAGES"
    RSS = "RSS"
    EMAIL = "EMAIL"
    MEDIA = "MEDIA"
    WEB = "WEB"
    FILE = "FILE"


class PlaceFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class MailImportance(str, Enum):
    NORMAL = "NORMAL"
    LOW = "LOW"
    HIGH = "HIGH"


class MedicalProcedureFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class ApplyPolicy(str, Enum):
    BEFORE_RESOLVER = "BEFORE_RESOLVER"
    AFTER_RESOLVER = "AFTER_RESOLVER"
    VALIDATION = "VALIDATION"


class SpecificationTypes(str, Enum):
    COMPLETION = "COMPLETION"
    TEXT_EMBEDDING = "TEXT_EMBEDDING"
    IMAGE_EMBEDDING = "IMAGE_EMBEDDING"
    EXTRACTION = "EXTRACTION"
    PREPARATION = "PREPARATION"


class PersonFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class FeedServiceTypes(str, Enum):
    GOOGLE_BLOB = "GOOGLE_BLOB"
    S3_BLOB = "S3_BLOB"
    AZURE_BLOB = "AZURE_BLOB"
    AZURE_FILE = "AZURE_FILE"
    SHARE_POINT = "SHARE_POINT"
    ONE_DRIVE = "ONE_DRIVE"
    GOOGLE_DRIVE = "GOOGLE_DRIVE"
    GOOGLE_EMAIL = "GOOGLE_EMAIL"
    MICROSOFT_EMAIL = "MICROSOFT_EMAIL"
    ATLASSIAN_JIRA = "ATLASSIAN_JIRA"
    LINEAR = "LINEAR"
    GIT_HUB_ISSUES = "GIT_HUB_ISSUES"
    GIT_HUB = "GIT_HUB"


class MedicalDrugFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class MedicalTherapyFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class RerankingModelServiceTypes(str, Enum):
    COHERE = "COHERE"
    JINA = "JINA"
    VOYAGE = "VOYAGE"


class EntityTypes(str, Enum):
    ACTIVITY = "ACTIVITY"
    ALERT = "ALERT"
    CATEGORY = "CATEGORY"
    COLLECTION = "COLLECTION"
    CONNECTOR = "CONNECTOR"
    CONTENT = "CONTENT"
    CONVERSATION = "CONVERSATION"
    EVENT = "EVENT"
    FEED = "FEED"
    JOB = "JOB"
    LABEL = "LABEL"
    METADATA = "METADATA"
    MEDICAL_STUDY = "MEDICAL_STUDY"
    MEDICAL_CONDITION = "MEDICAL_CONDITION"
    MEDICAL_GUIDELINE = "MEDICAL_GUIDELINE"
    MEDICAL_DRUG = "MEDICAL_DRUG"
    MEDICAL_DRUG_CLASS = "MEDICAL_DRUG_CLASS"
    MEDICAL_INDICATION = "MEDICAL_INDICATION"
    MEDICAL_CONTRAINDICATION = "MEDICAL_CONTRAINDICATION"
    MEDICAL_TEST = "MEDICAL_TEST"
    MEDICAL_DEVICE = "MEDICAL_DEVICE"
    MEDICAL_THERAPY = "MEDICAL_THERAPY"
    MEDICAL_PROCEDURE = "MEDICAL_PROCEDURE"
    OBSERVATION = "OBSERVATION"
    ORGANIZATION = "ORGANIZATION"
    PERSON = "PERSON"
    PLACE = "PLACE"
    PRODUCT = "PRODUCT"
    PROJECT = "PROJECT"
    RENDITION = "RENDITION"
    REPO = "REPO"
    SITE = "SITE"
    SOFTWARE = "SOFTWARE"
    SPECIFICATION = "SPECIFICATION"
    WORKFLOW = "WORKFLOW"


class AzureDocumentIntelligenceModels(str, Enum):
    READ_OCR = "READ_OCR"
    LAYOUT = "LAYOUT"
    INVOICE = "INVOICE"
    RECEIPT = "RECEIPT"
    IDENTIFICATION_DOCUMENT = "IDENTIFICATION_DOCUMENT"
    US_HEALTH_INSURANCE_CARD = "US_HEALTH_INSURANCE_CARD"
    US_TAX_FORM_W2 = "US_TAX_FORM_W2"
    US_TAX_FORM1098 = "US_TAX_FORM1098"
    US_TAX_FORM1098_E = "US_TAX_FORM1098_E"
    US_TAX_FORM1098_T = "US_TAX_FORM1098_T"
    US_TAX_FORM1099 = "US_TAX_FORM1099"
    US_MARRIAGE_CERTIFICATE = "US_MARRIAGE_CERTIFICATE"
    US_MORTGAGE1003 = "US_MORTGAGE1003"
    US_MORTGAGE1008 = "US_MORTGAGE1008"
    US_MORTGAGE_DISCLOSURE = "US_MORTGAGE_DISCLOSURE"
    CREDIT_CARD = "CREDIT_CARD"
    US_PAY_STUB = "US_PAY_STUB"
    US_BANK_CHECK = "US_BANK_CHECK"
    US_BANK_STATEMENT = "US_BANK_STATEMENT"


class SearchTypes(str, Enum):
    KEYWORD = "KEYWORD"
    VECTOR = "VECTOR"
    HYBRID = "HYBRID"


class NotionTypes(str, Enum):
    PAGE = "PAGE"
    DATABASE = "DATABASE"


class OrderDirectionTypes(str, Enum):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class MedicalTestFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class CategoryFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class ImageProjectionTypes(str, Enum):
    EQUIRECTANGULAR = "EQUIRECTANGULAR"
    CYLINDRICAL = "CYLINDRICAL"


class PolicyTimeTypes(str, Enum):
    RELATIVE_TIME = "RELATIVE_TIME"
    ABSOLUTE_TIME = "ABSOLUTE_TIME"


class ElevenLabsModels(str, Enum):
    MULTILINGUAL_V1 = "MULTILINGUAL_V1"
    MULTILINGUAL_V2 = "MULTILINGUAL_V2"
    ENGLISH_V1 = "ENGLISH_V1"
    TURBO_V2 = "TURBO_V2"
    TURBO_V2_5 = "TURBO_V2_5"


class OccurrenceTypes(str, Enum):
    IMAGE = "IMAGE"
    TIME = "TIME"
    TEXT = "TEXT"


class MedicalIndicationFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class YouTubeTypes(str, Enum):
    VIDEO = "VIDEO"
    VIDEOS = "VIDEOS"
    PLAYLIST = "PLAYLIST"
    CHANNEL = "CHANNEL"


class OrientationTypes(str, Enum):
    TOP_LEFT = "TOP_LEFT"
    TOP_RIGHT = "TOP_RIGHT"
    BOTTOM_RIGHT = "BOTTOM_RIGHT"
    BOTTOM_LEFT = "BOTTOM_LEFT"
    LEFT_TOP = "LEFT_TOP"
    RIGHT_TOP = "RIGHT_TOP"
    RIGHT_BOTTOM = "RIGHT_BOTTOM"
    LEFT_BOTTOM = "LEFT_BOTTOM"


class EmailListingTypes(str, Enum):
    PAST = "PAST"
    NEW = "NEW"


class TimeIntervalTypes(str, Enum):
    MINUTE = "MINUTE"
    HOUR = "HOUR"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    QUARTER = "QUARTER"
    YEAR = "YEAR"


class EventFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class DeviceTypes(str, Enum):
    DRONE = "DRONE"
    ROBOT = "ROBOT"
    MOBILE = "MOBILE"
    CAMERA = "CAMERA"
    STREAM = "STREAM"
    SCREEN = "SCREEN"
    GEOSPATIAL = "GEOSPATIAL"
    UNKNOWN = "UNKNOWN"


class EnvironmentTypes(str, Enum):
    DEVELOPMENT = "DEVELOPMENT"
    PRODUCTION = "PRODUCTION"


class MailPriority(str, Enum):
    NORMAL = "NORMAL"
    LOW = "LOW"
    HIGH = "HIGH"


class SharePointAuthenticationTypes(str, Enum):
    APPLICATION = "APPLICATION"
    USER = "USER"


class FeedConnectorTypes(str, Enum):
    GOOGLE = "GOOGLE"
    AMAZON = "AMAZON"
    AZURE = "AZURE"
    SHARE_POINT = "SHARE_POINT"
    ONE_DRIVE = "ONE_DRIVE"
    GOOGLE_DRIVE = "GOOGLE_DRIVE"
    GOOGLE_EMAIL = "GOOGLE_EMAIL"
    MICROSOFT_EMAIL = "MICROSOFT_EMAIL"
    ATLASSIAN = "ATLASSIAN"
    LINEAR = "LINEAR"
    GIT_HUB = "GIT_HUB"


class ProductFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class FileTypes(str, Enum):
    VIDEO = "VIDEO"
    AUDIO = "AUDIO"
    IMAGE = "IMAGE"
    ANIMATION = "ANIMATION"
    DOCUMENT = "DOCUMENT"
    EMAIL = "EMAIL"
    CODE = "CODE"
    DATA = "DATA"
    PACKAGE = "PACKAGE"
    SHAPE = "SHAPE"
    POINT_CLOUD = "POINT_CLOUD"
    GEOMETRY = "GEOMETRY"
    DRAWING = "DRAWING"
    MANIFEST = "MANIFEST"
    UNKNOWN = "UNKNOWN"


class VoyageModels(str, Enum):
    VOYAGE = "VOYAGE"
    VOYAGE_3_0 = "VOYAGE_3_0"
    VOYAGE_LITE_3_0 = "VOYAGE_LITE_3_0"
    VOYAGE_FINANCE_2_0 = "VOYAGE_FINANCE_2_0"
    VOYAGE_MULTILINGUAL_2_0 = "VOYAGE_MULTILINGUAL_2_0"
    VOYAGE_LAW_2_0 = "VOYAGE_LAW_2_0"
    VOYAGE_CODE_2_0 = "VOYAGE_CODE_2_0"
    CUSTOM = "CUSTOM"


class GroqModels(str, Enum):
    LLAVA_1_5_7B_PREVIEW = "LLAVA_1_5_7B_PREVIEW"
    MIXTRAL_8X7B_INSTRUCT = "MIXTRAL_8X7B_INSTRUCT"
    LLAMA_3_3_70B = "LLAMA_3_3_70B"
    LLAMA_3_2_90B_TEXT_PREVIEW = "LLAMA_3_2_90B_TEXT_PREVIEW"
    LLAMA_3_2_90B_VISION_PREVIEW = "LLAMA_3_2_90B_VISION_PREVIEW"
    LLAMA_3_2_11B_TEXT_PREVIEW = "LLAMA_3_2_11B_TEXT_PREVIEW"
    LLAMA_3_2_11B_VISION_PREVIEW = "LLAMA_3_2_11B_VISION_PREVIEW"
    LLAMA_3_2_3B_PREVIEW = "LLAMA_3_2_3B_PREVIEW"
    LLAMA_3_2_1B_PREVIEW = "LLAMA_3_2_1B_PREVIEW"
    LLAMA_3_1_405B = "LLAMA_3_1_405B"
    LLAMA_3_1_70B = "LLAMA_3_1_70B"
    LLAMA_3_1_8B = "LLAMA_3_1_8B"
    LLAMA_3_70B = "LLAMA_3_70B"
    LLAMA_3_8B = "LLAMA_3_8B"
    CUSTOM = "CUSTOM"


class PromptStrategyTypes(str, Enum):
    OPTIMIZE_SEARCH = "OPTIMIZE_SEARCH"
    REWRITE = "REWRITE"
    NONE = "NONE"


class AzureDocumentIntelligenceVersions(str, Enum):
    V2023_07_31 = "V2023_07_31"
    V2024_02_29_PREVIEW = "V2024_02_29_PREVIEW"
    V2024_07_31_PREVIEW = "V2024_07_31_PREVIEW"


class MailSensitivity(str, Enum):
    NONE = "NONE"
    NORMAL = "NORMAL"
    PERSONAL = "PERSONAL"
    PRIVATE = "PRIVATE"
    COMPANY_CONFIDENTIAL = "COMPANY_CONFIDENTIAL"


class DeepseekModels(str, Enum):
    CHAT = "CHAT"
    CODER = "CODER"
    CUSTOM = "CUSTOM"


class SearchServiceTypes(str, Enum):
    TAVILY = "TAVILY"
    EXA = "EXA"


class MedicalContraindicationFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class RepoFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class GraphStrategyTypes(str, Enum):
    EXTRACT_ENTITIES_FILTER = "EXTRACT_ENTITIES_FILTER"
    EXTRACT_ENTITIES_GRAPH = "EXTRACT_ENTITIES_GRAPH"
    NONE = "NONE"


class JinaModels(str, Enum):
    CLIP_IMAGE = "CLIP_IMAGE"
    EMBED = "EMBED"
    EMBED_3_0 = "EMBED_3_0"
    CUSTOM = "CUSTOM"


class UnitTypes(str, Enum):
    KILOMETER = "KILOMETER"
    METER = "METER"
    CENTIMETER = "CENTIMETER"
    MILLIMETER = "MILLIMETER"
    MICROMETER = "MICROMETER"
    NANOMETER = "NANOMETER"
    ANGSTROM = "ANGSTROM"
    DECIMETER = "DECIMETER"
    DECAMETER = "DECAMETER"
    HECTOMETER = "HECTOMETER"
    GIGAMETER = "GIGAMETER"
    ASTRONOMICAL_UNIT = "ASTRONOMICAL_UNIT"
    LIGHT_YEAR = "LIGHT_YEAR"
    PARSEC = "PARSEC"
    MILE = "MILE"
    YARD = "YARD"
    FOOT = "FOOT"
    INCH = "INCH"
    MIL = "MIL"
    MICRO_INCH = "MICRO_INCH"
    CUSTOM = "CUSTOM"
    UNITLESS = "UNITLESS"


class ConversationTypes(str, Enum):
    CONTENT = "CONTENT"


class MedicalConditionFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class SoftwareFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class ResourceConnectorTypes(str, Enum):
    AMAZON = "AMAZON"
    AZURE = "AZURE"
    GOOGLE = "GOOGLE"


class ReplicateModels(str, Enum):
    MISTRAL_7B = "MISTRAL_7B"
    MISTRAL_7B_INSTRUCT = "MISTRAL_7B_INSTRUCT"
    LLAMA_2_7B = "LLAMA_2_7B"
    LLAMA_2_13B = "LLAMA_2_13B"
    LLAMA_2_70B = "LLAMA_2_70B"
    LLAMA_2_7B_CHAT = "LLAMA_2_7B_CHAT"
    LLAMA_2_13B_CHAT = "LLAMA_2_13B_CHAT"
    LLAMA_2_70B_CHAT = "LLAMA_2_70B_CHAT"
    CUSTOM = "CUSTOM"


class FilePreparationServiceTypes(str, Enum):
    AZURE_DOCUMENT_INTELLIGENCE = "AZURE_DOCUMENT_INTELLIGENCE"
    DEEPGRAM = "DEEPGRAM"
    DOCUMENT = "DOCUMENT"
    EMAIL = "EMAIL"
    MODEL_DOCUMENT = "MODEL_DOCUMENT"


class FacetValueTypes(str, Enum):
    VALUE = "VALUE"
    RANGE = "RANGE"
    OBJECT = "OBJECT"


class BillableMetrics(str, Enum):
    BYTES = "BYTES"
    TOKENS = "TOKENS"
    LENGTH = "LENGTH"
    TIME = "TIME"
    UNITS = "UNITS"
    COST = "COST"
    REQUESTS = "REQUESTS"
    CREDITS = "CREDITS"


class CohereModels(str, Enum):
    EMBED_ENGLISH_3_0 = "EMBED_ENGLISH_3_0"
    EMBED_MULTILINGUAL_3_0 = "EMBED_MULTILINGUAL_3_0"
    COMMAND_R = "COMMAND_R"
    COMMAND_R_202403 = "COMMAND_R_202403"
    COMMAND_R_202408 = "COMMAND_R_202408"
    COMMAND_R_PLUS = "COMMAND_R_PLUS"
    COMMAND_R_PLUS_202404 = "COMMAND_R_PLUS_202404"
    COMMAND_R_PLUS_202408 = "COMMAND_R_PLUS_202408"
    CUSTOM = "CUSTOM"


class TimedPolicyRecurrenceTypes(str, Enum):
    ONCE = "ONCE"
    REPEAT = "REPEAT"


class MedicalGuidelineFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class DeepgramModels(str, Enum):
    NOVA2 = "NOVA2"
    NOVA2_MEETING = "NOVA2_MEETING"
    NOVA2_PHONECALL = "NOVA2_PHONECALL"
    NOVA2_VOICEMAIL = "NOVA2_VOICEMAIL"
    NOVA2_FINANCE = "NOVA2_FINANCE"
    NOVA2_CONVERSATIONAL_AI = "NOVA2_CONVERSATIONAL_AI"
    NOVA2_VIDEO = "NOVA2_VIDEO"
    NOVA2_MEDICAL = "NOVA2_MEDICAL"
    NOVA2_DRIVETHRU = "NOVA2_DRIVETHRU"
    NOVA2_AUTOMOTIVE = "NOVA2_AUTOMOTIVE"
    WHISPER_TINY = "WHISPER_TINY"
    WHISPER_SMALL = "WHISPER_SMALL"
    WHISPER_BASE = "WHISPER_BASE"
    WHISPER_MEDIUM = "WHISPER_MEDIUM"
    WHISPER_LARGE = "WHISPER_LARGE"


class FeedTypes(str, Enum):
    NOTION = "NOTION"
    SLACK = "SLACK"
    MICROSOFT_TEAMS = "MICROSOFT_TEAMS"
    DISCORD = "DISCORD"
    REDDIT = "REDDIT"
    WEB = "WEB"
    RSS = "RSS"
    SITE = "SITE"
    YOU_TUBE = "YOU_TUBE"
    EMAIL = "EMAIL"
    ISSUE = "ISSUE"
    SEARCH = "SEARCH"


class AnthropicModels(str, Enum):
    CLAUDE_2 = "CLAUDE_2"
    CLAUDE_2_0 = "CLAUDE_2_0"
    CLAUDE_2_1 = "CLAUDE_2_1"
    CLAUDE_INSTANT_1 = "CLAUDE_INSTANT_1"
    CLAUDE_INSTANT_1_2 = "CLAUDE_INSTANT_1_2"
    CLAUDE_3_OPUS = "CLAUDE_3_OPUS"
    CLAUDE_3_OPUS_20240229 = "CLAUDE_3_OPUS_20240229"
    CLAUDE_3_SONNET = "CLAUDE_3_SONNET"
    CLAUDE_3_SONNET_20240229 = "CLAUDE_3_SONNET_20240229"
    CLAUDE_3_HAIKU = "CLAUDE_3_HAIKU"
    CLAUDE_3_HAIKU_20240307 = "CLAUDE_3_HAIKU_20240307"
    CLAUDE_3_5_SONNET = "CLAUDE_3_5_SONNET"
    CLAUDE_3_5_SONNET_20241022 = "CLAUDE_3_5_SONNET_20241022"
    CLAUDE_3_5_SONNET_20240620 = "CLAUDE_3_5_SONNET_20240620"
    CLAUDE_3_5_HAIKU = "CLAUDE_3_5_HAIKU"
    CLAUDE_3_5_HAIKU_20241022 = "CLAUDE_3_5_HAIKU_20241022"
    CUSTOM = "CUSTOM"


class OpenAIVisionDetailLevels(str, Enum):
    HIGH = "HIGH"
    LOW = "LOW"


class FeedListingTypes(str, Enum):
    PAST = "PAST"
    NEW = "NEW"


class MetadataTypes(str, Enum):
    CONTENT = "CONTENT"


class ObservableTypes(str, Enum):
    CATEGORY = "CATEGORY"
    LABEL = "LABEL"
    EVENT = "EVENT"
    ORGANIZATION = "ORGANIZATION"
    PERSON = "PERSON"
    PLACE = "PLACE"
    PRODUCT = "PRODUCT"
    REPO = "REPO"
    SOFTWARE = "SOFTWARE"
    MEDICAL_STUDY = "MEDICAL_STUDY"
    MEDICAL_CONDITION = "MEDICAL_CONDITION"
    MEDICAL_GUIDELINE = "MEDICAL_GUIDELINE"
    MEDICAL_DRUG = "MEDICAL_DRUG"
    MEDICAL_DRUG_CLASS = "MEDICAL_DRUG_CLASS"
    MEDICAL_INDICATION = "MEDICAL_INDICATION"
    MEDICAL_CONTRAINDICATION = "MEDICAL_CONTRAINDICATION"
    MEDICAL_TEST = "MEDICAL_TEST"
    MEDICAL_DEVICE = "MEDICAL_DEVICE"
    MEDICAL_THERAPY = "MEDICAL_THERAPY"
    MEDICAL_PROCEDURE = "MEDICAL_PROCEDURE"


class GoogleModels(str, Enum):
    GEMINI_2_0_FLASH_EXPERIMENTAL = "GEMINI_2_0_FLASH_EXPERIMENTAL"
    GEMINI_1_5_FLASH_8B = "GEMINI_1_5_FLASH_8B"
    GEMINI_1_5_FLASH_8B_001 = "GEMINI_1_5_FLASH_8B_001"
    GEMINI_1_5_FLASH = "GEMINI_1_5_FLASH"
    GEMINI_1_5_PRO = "GEMINI_1_5_PRO"
    GEMINI_1_5_FLASH_001 = "GEMINI_1_5_FLASH_001"
    GEMINI_1_5_PRO_001 = "GEMINI_1_5_PRO_001"
    GEMINI_1_5_FLASH_002 = "GEMINI_1_5_FLASH_002"
    GEMINI_1_5_PRO_002 = "GEMINI_1_5_PRO_002"
    EMBEDDING_004 = "EMBEDDING_004"
    CUSTOM = "CUSTOM"


class EntityExtractionServiceTypes(str, Enum):
    ROBOFLOW_IMAGE = "ROBOFLOW_IMAGE"
    MODEL_TEXT = "MODEL_TEXT"
    MODEL_IMAGE = "MODEL_IMAGE"
    OPEN_AI_IMAGE = "OPEN_AI_IMAGE"
    AZURE_COGNITIVE_SERVICES_IMAGE = "AZURE_COGNITIVE_SERVICES_IMAGE"
    AZURE_COGNITIVE_SERVICES_TEXT = "AZURE_COGNITIVE_SERVICES_TEXT"


class ContentPublishingFormats(str, Enum):
    MP3 = "MP3"
    TEXT = "TEXT"
    MARKDOWN = "MARKDOWN"
    HTML = "HTML"


class RenditionTypes(str, Enum):
    CONTENT = "CONTENT"


class MistralModels(str, Enum):
    MIXTRAL_8X7B_INSTRUCT = "MIXTRAL_8X7B_INSTRUCT"
    MISTRAL_NEMO = "MISTRAL_NEMO"
    MISTRAL_SMALL = "MISTRAL_SMALL"
    MISTRAL_MEDIUM = "MISTRAL_MEDIUM"
    MISTRAL_LARGE = "MISTRAL_LARGE"
    PIXTRAL_12B_2409 = "PIXTRAL_12B_2409"
    PIXTRAL_LARGE = "PIXTRAL_LARGE"
    MISTRAL_EMBED = "MISTRAL_EMBED"
    CUSTOM = "CUSTOM"


class ConversationRoleTypes(str, Enum):
    SYSTEM = "SYSTEM"
    ASSISTANT = "ASSISTANT"
    USER = "USER"


class TextRoles(str, Enum):
    PAGE_HEADER = "PAGE_HEADER"
    PAGE_FOOTER = "PAGE_FOOTER"
    PAGE_NUMBER = "PAGE_NUMBER"
    TITLE = "TITLE"
    SECTION_HEADING = "SECTION_HEADING"
    FOOTNOTE = "FOOTNOTE"
    CODE = "CODE"
    LIST_ITEM = "LIST_ITEM"
    HEADING1 = "HEADING1"
    HEADING2 = "HEADING2"
    HEADING3 = "HEADING3"
    HEADING4 = "HEADING4"
    HEADING5 = "HEADING5"
    HEADING6 = "HEADING6"
    TABLE_COLUMN_HEADER = "TABLE_COLUMN_HEADER"
    TABLE_ROW_HEADER = "TABLE_ROW_HEADER"
    TABLE_CORNER_HEADER = "TABLE_CORNER_HEADER"
    TABLE_CELL = "TABLE_CELL"
    TABLE_CAPTION = "TABLE_CAPTION"
    TABLE_HEADER = "TABLE_HEADER"
    TABLE = "TABLE"
    FIGURE = "FIGURE"
    FIGURE_CAPTION = "FIGURE_CAPTION"
    DIAGRAM = "DIAGRAM"
    DIAGRAM_CAPTION = "DIAGRAM_CAPTION"
    WATERMARK = "WATERMARK"
    EQUATION = "EQUATION"
    PARAGRAPH = "PARAGRAPH"
    CHECKBOX = "CHECKBOX"
    RADIO_BUTTON = "RADIO_BUTTON"
    COLUMN_HEADER = "COLUMN_HEADER"
    ROW_HEADER = "ROW_HEADER"
    CORNER_HEADER = "CORNER_HEADER"


class ContentPublishingServiceTypes(str, Enum):
    ELEVEN_LABS_AUDIO = "ELEVEN_LABS_AUDIO"
    TEXT = "TEXT"


class OrderByTypes(str, Enum):
    NAME = "NAME"
    CREATION_DATE = "CREATION_DATE"
    ORIGINAL_DATE = "ORIGINAL_DATE"
    RELEVANCE = "RELEVANCE"


class RevisionStrategyTypes(str, Enum):
    REVISE = "REVISE"
    CUSTOM = "CUSTOM"
    NONE = "NONE"
