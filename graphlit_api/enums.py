# Generated by ariadne-codegen
# Source: https://data-scus.graphlit.io/api/v1/graphql

from enum import Enum


class ApplyPolicy(str, Enum):
    BEFORE_RESOLVER = "BEFORE_RESOLVER"
    AFTER_RESOLVER = "AFTER_RESOLVER"
    VALIDATION = "VALIDATION"


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


class TimeIntervalTypes(str, Enum):
    MINUTE = "MINUTE"
    HOUR = "HOUR"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    QUARTER = "QUARTER"
    YEAR = "YEAR"


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


class AlertTypes(str, Enum):
    PROMPT = "PROMPT"


class CollectionTypes(str, Enum):
    COLLECTION = "COLLECTION"


class FacetValueTypes(str, Enum):
    VALUE = "VALUE"
    RANGE = "RANGE"
    OBJECT = "OBJECT"


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


class ContentTypes(str, Enum):
    FILE = "FILE"
    PAGE = "PAGE"
    MESSAGE = "MESSAGE"
    TEXT = "TEXT"
    POST = "POST"
    EMAIL = "EMAIL"
    EVENT = "EVENT"
    ISSUE = "ISSUE"


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


class DeviceTypes(str, Enum):
    DRONE = "DRONE"
    ROBOT = "ROBOT"
    MOBILE = "MOBILE"
    CAMERA = "CAMERA"
    STREAM = "STREAM"
    SCREEN = "SCREEN"
    GEOSPATIAL = "GEOSPATIAL"
    UNKNOWN = "UNKNOWN"


class ConversationTypes(str, Enum):
    CONTENT = "CONTENT"


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


class OrganizationFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class PersonFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class PlaceFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class EnvironmentTypes(str, Enum):
    DEVELOPMENT = "DEVELOPMENT"
    PRODUCTION = "PRODUCTION"


class ResourceConnectorTypes(str, Enum):
    AMAZON = "AMAZON"
    AZURE = "AZURE"
    GOOGLE = "GOOGLE"


class RenditionTypes(str, Enum):
    CONTENT = "CONTENT"


class SpecificationTypes(str, Enum):
    COMPLETION = "COMPLETION"
    EXTRACTION = "EXTRACTION"
    PREPARATION = "PREPARATION"


class ModelServiceTypes(str, Enum):
    ANTHROPIC = "ANTHROPIC"
    AZURE_OPEN_AI = "AZURE_OPEN_AI"
    OPEN_AI = "OPEN_AI"
    REPLICATE = "REPLICATE"
    GROQ = "GROQ"
    MISTRAL = "MISTRAL"
    COHERE = "COHERE"
    DEEPSEEK = "DEEPSEEK"


class ConversationSearchTypes(str, Enum):
    VECTOR = "VECTOR"
    HYBRID = "HYBRID"


class OrderByTypes(str, Enum):
    NAME = "NAME"
    CREATION_DATE = "CREATION_DATE"
    ORIGINAL_DATE = "ORIGINAL_DATE"
    RELEVANCE = "RELEVANCE"


class OrderDirectionTypes(str, Enum):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class SearchTypes(str, Enum):
    KEYWORD = "KEYWORD"
    VECTOR = "VECTOR"
    HYBRID = "HYBRID"


class SearchQueryTypes(str, Enum):
    SIMPLE = "SIMPLE"
    FULL = "FULL"


class ContentPublishingServiceTypes(str, Enum):
    ELEVEN_LABS_AUDIO = "ELEVEN_LABS_AUDIO"
    TEXT = "TEXT"


class ContentPublishingFormats(str, Enum):
    MP3 = "MP3"
    TEXT = "TEXT"
    MARKDOWN = "MARKDOWN"
    HTML = "HTML"


class IntegrationServiceTypes(str, Enum):
    SLACK = "SLACK"
    WEB_HOOK = "WEB_HOOK"


class TimedPolicyRecurrenceTypes(str, Enum):
    ONCE = "ONCE"
    REPEAT = "REPEAT"


class PolicyTimeTypes(str, Enum):
    RELATIVE_TIME = "RELATIVE_TIME"
    ABSOLUTE_TIME = "ABSOLUTE_TIME"


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


class ImageProjectionTypes(str, Enum):
    EQUIRECTANGULAR = "EQUIRECTANGULAR"
    CYLINDRICAL = "CYLINDRICAL"


class OrientationTypes(str, Enum):
    TOP_LEFT = "TOP_LEFT"
    TOP_RIGHT = "TOP_RIGHT"
    BOTTOM_RIGHT = "BOTTOM_RIGHT"
    BOTTOM_LEFT = "BOTTOM_LEFT"
    LEFT_TOP = "LEFT_TOP"
    RIGHT_TOP = "RIGHT_TOP"
    RIGHT_BOTTOM = "RIGHT_BOTTOM"
    LEFT_BOTTOM = "LEFT_BOTTOM"


class MailSensitivity(str, Enum):
    NONE = "NONE"
    NORMAL = "NORMAL"
    PERSONAL = "PERSONAL"
    PRIVATE = "PRIVATE"
    COMPANY_CONFIDENTIAL = "COMPANY_CONFIDENTIAL"


class MailPriority(str, Enum):
    NORMAL = "NORMAL"
    LOW = "LOW"
    HIGH = "HIGH"


class MailImportance(str, Enum):
    NORMAL = "NORMAL"
    LOW = "LOW"
    HIGH = "HIGH"


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


class ConversationRoleTypes(str, Enum):
    SYSTEM = "SYSTEM"
    ASSISTANT = "ASSISTANT"
    USER = "USER"
    FUNCTION = "FUNCTION"


class SiteTypes(str, Enum):
    WATCH = "WATCH"
    SWEEP = "SWEEP"
    STORAGE = "STORAGE"


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


class SearchServiceTypes(str, Enum):
    TAVILY = "TAVILY"
    EXA = "EXA"


class YouTubeTypes(str, Enum):
    VIDEO = "VIDEO"
    VIDEOS = "VIDEOS"
    PLAYLIST = "PLAYLIST"
    CHANNEL = "CHANNEL"


class NotionTypes(str, Enum):
    PAGE = "PAGE"
    DATABASE = "DATABASE"


class FeedListingTypes(str, Enum):
    PAST = "PAST"
    NEW = "NEW"


class OccurrenceTypes(str, Enum):
    IMAGE = "IMAGE"
    TIME = "TIME"
    TEXT = "TEXT"


class ConversationStrategyTypes(str, Enum):
    WINDOWED = "WINDOWED"
    SUMMARIZED = "SUMMARIZED"


class PromptStrategyTypes(str, Enum):
    OPTIMIZE_SEARCH = "OPTIMIZE_SEARCH"
    REWRITE = "REWRITE"
    NONE = "NONE"


class RetrievalStrategyTypes(str, Enum):
    CONTENT = "CONTENT"
    CHUNK = "CHUNK"
    SECTION = "SECTION"


class RerankingModelServiceTypes(str, Enum):
    COHERE = "COHERE"
    JINA = "JINA"
    PONGO = "PONGO"


class GraphStrategyTypes(str, Enum):
    EXTRACT_ENTITIES_FILTER = "EXTRACT_ENTITIES_FILTER"
    EXTRACT_ENTITIES_GRAPH = "EXTRACT_ENTITIES_GRAPH"
    NONE = "NONE"


class RevisionStrategyTypes(str, Enum):
    REVISE = "REVISE"
    CUSTOM = "CUSTOM"
    NONE = "NONE"


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
    GPT4O_128K = "GPT4O_128K"
    GPT4O_MINI_128K_20240718 = "GPT4O_MINI_128K_20240718"
    GPT4O_MINI_128K = "GPT4O_MINI_128K"
    GPT4O_CHAT_128K = "GPT4O_CHAT_128K"
    CUSTOM = "CUSTOM"


class OpenAIVisionDetailLevels(str, Enum):
    HIGH = "HIGH"
    LOW = "LOW"


class AzureOpenAIModels(str, Enum):
    GPT35_TURBO_16K = "GPT35_TURBO_16K"
    GPT4 = "GPT4"
    GPT4_TURBO_128K = "GPT4_TURBO_128K"
    CUSTOM = "CUSTOM"


class CohereModels(str, Enum):
    COMMAND_R = "COMMAND_R"
    COMMAND_R_202403 = "COMMAND_R_202403"
    COMMAND_R_202408 = "COMMAND_R_202408"
    COMMAND_R_PLUS = "COMMAND_R_PLUS"
    COMMAND_R_PLUS_202404 = "COMMAND_R_PLUS_202404"
    COMMAND_R_PLUS_202408 = "COMMAND_R_PLUS_202408"
    CUSTOM = "CUSTOM"


class AnthropicModels(str, Enum):
    CLAUDE_2 = "CLAUDE_2"
    CLAUDE_2_0 = "CLAUDE_2_0"
    CLAUDE_2_1 = "CLAUDE_2_1"
    CLAUDE_INSTANT_1 = "CLAUDE_INSTANT_1"
    CLAUDE_INSTANT_1_2 = "CLAUDE_INSTANT_1_2"
    CLAUDE_3_OPUS = "CLAUDE_3_OPUS"
    CLAUDE_3_SONNET = "CLAUDE_3_SONNET"
    CLAUDE_3_HAIKU = "CLAUDE_3_HAIKU"
    CLAUDE_3_5_SONNET = "CLAUDE_3_5_SONNET"
    CUSTOM = "CUSTOM"


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


class MistralModels(str, Enum):
    MIXTRAL_8X7B_INSTRUCT = "MIXTRAL_8X7B_INSTRUCT"
    MISTRAL_NEMO = "MISTRAL_NEMO"
    MISTRAL_SMALL = "MISTRAL_SMALL"
    MISTRAL_MEDIUM = "MISTRAL_MEDIUM"
    MISTRAL_LARGE = "MISTRAL_LARGE"
    CUSTOM = "CUSTOM"


class GroqModels(str, Enum):
    LLAVA_1_5_7B = "LLAVA_1_5_7B"
    MIXTRAL_8X7B_INSTRUCT = "MIXTRAL_8X7B_INSTRUCT"
    LLAMA_3_1_405B = "LLAMA_3_1_405B"
    LLAMA_3_1_70B = "LLAMA_3_1_70B"
    LLAMA_3_1_8B = "LLAMA_3_1_8B"
    LLAMA_3_70B = "LLAMA_3_70B"
    LLAMA_3_8B = "LLAMA_3_8B"
    CUSTOM = "CUSTOM"


class DeepseekModels(str, Enum):
    CHAT = "CHAT"
    CODER = "CODER"
    CUSTOM = "CUSTOM"


class ElevenLabsModels(str, Enum):
    MULTILINGUAL_V1 = "MULTILINGUAL_V1"
    MULTILINGUAL_V2 = "MULTILINGUAL_V2"
    ENGLISH_V1 = "ENGLISH_V1"
    TURBO_V2 = "TURBO_V2"


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
    TABLE_COLUMN_HEADER = "TABLE_COLUMN_HEADER"
    TABLE_ROW_HEADER = "TABLE_ROW_HEADER"
    TABLE_CORNER_HEADER = "TABLE_CORNER_HEADER"
    TABLE_CELL = "TABLE_CELL"
    TABLE_CAPTION = "TABLE_CAPTION"
    TABLE = "TABLE"
    FIGURE = "FIGURE"
    DIAGRAM = "DIAGRAM"
    WATERMARK = "WATERMARK"
    EQUATION = "EQUATION"
    PARAGRAPH = "PARAGRAPH"
    CHECKBOX = "CHECKBOX"
    RADIO_BUTTON = "RADIO_BUTTON"
    COLUMN_HEADER = "COLUMN_HEADER"
    ROW_HEADER = "ROW_HEADER"
    CORNER_HEADER = "CORNER_HEADER"


class SharePointAuthenticationTypes(str, Enum):
    APPLICATION = "APPLICATION"
    USER = "USER"


class EmailListingTypes(str, Enum):
    PAST = "PAST"
    NEW = "NEW"


class SummarizationTypes(str, Enum):
    SUMMARY = "SUMMARY"
    KEYWORDS = "KEYWORDS"
    BULLETS = "BULLETS"
    HEADLINES = "HEADLINES"
    POSTS = "POSTS"
    CHAPTERS = "CHAPTERS"
    QUESTIONS = "QUESTIONS"
    CUSTOM = "CUSTOM"


class ContentIndexingServiceTypes(str, Enum):
    AZURE_AI_LANGUAGE = "AZURE_AI_LANGUAGE"


class FilePreparationServiceTypes(str, Enum):
    AZURE_DOCUMENT_INTELLIGENCE = "AZURE_DOCUMENT_INTELLIGENCE"
    DEEPGRAM = "DEEPGRAM"
    DOCUMENT = "DOCUMENT"
    EMAIL = "EMAIL"
    MODEL_DOCUMENT = "MODEL_DOCUMENT"


class EntityExtractionServiceTypes(str, Enum):
    ROBOFLOW_IMAGE = "ROBOFLOW_IMAGE"
    MODEL_TEXT = "MODEL_TEXT"
    OPEN_AI_IMAGE = "OPEN_AI_IMAGE"
    MODEL_IMAGE = "MODEL_IMAGE"
    AZURE_COGNITIVE_SERVICES_IMAGE = "AZURE_COGNITIVE_SERVICES_IMAGE"
    AZURE_COGNITIVE_SERVICES_TEXT = "AZURE_COGNITIVE_SERVICES_TEXT"


class EntityEnrichmentServiceTypes(str, Enum):
    DIFFBOT = "DIFFBOT"
    WIKIPEDIA = "WIKIPEDIA"
    CRUNCHBASE = "CRUNCHBASE"
    FHIR = "FHIR"


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


class AzureDocumentIntelligenceVersions(str, Enum):
    V2023_07_31 = "V2023_07_31"
    V2024_02_29_PREVIEW = "V2024_02_29_PREVIEW"
    V2024_07_31_PREVIEW = "V2024_07_31_PREVIEW"


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


class TextTypes(str, Enum):
    PLAIN = "PLAIN"
    MARKDOWN = "MARKDOWN"
    HTML = "HTML"


class CategoryFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class EventFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class LabelFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class MedicalStudyFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class MedicalConditionFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class MedicalGuidelineFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class MedicalDrugFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class MedicalDrugClassFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class MedicalContraindicationFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class MedicalIndicationFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class MedicalProcedureFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class MedicalDeviceFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class MedicalTherapyFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class MedicalTestFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class ProductFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class BillableMetrics(str, Enum):
    BYTES = "BYTES"
    TOKENS = "TOKENS"
    LENGTH = "LENGTH"
    TIME = "TIME"
    UNITS = "UNITS"
    COST = "COST"
    REQUESTS = "REQUESTS"
    CREDITS = "CREDITS"


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


class OperationTypes(str, Enum):
    QUERY = "QUERY"
    MUTATION = "MUTATION"


class RepoFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"


class SoftwareFacetTypes(str, Enum):
    CREATION_DATE = "CREATION_DATE"
