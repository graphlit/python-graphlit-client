# Generated by ariadne-codegen
# Source: ./documents

__all__ = [
    "ADD_CONTENTS_TO_COLLECTIONS_GQL",
    "CLEAR_CONVERSATION_GQL",
    "CLOSE_CONVERSATION_GQL",
    "CREATE_ALERT_GQL",
    "CREATE_COLLECTION_GQL",
    "CREATE_CONVERSATION_GQL",
    "CREATE_FEED_GQL",
    "CREATE_SPECIFICATION_GQL",
    "CREATE_WORKFLOW_GQL",
    "CREDITS_GQL",
    "DELETE_ALERTS_GQL",
    "DELETE_ALERT_GQL",
    "DELETE_ALL_ALERTS_GQL",
    "DELETE_ALL_CONTENTS_GQL",
    "DELETE_ALL_CONVERSATIONS_GQL",
    "DELETE_ALL_FEEDS_GQL",
    "DELETE_ALL_WORKFLOWS_GQL",
    "DELETE_COLLECTIONS_GQL",
    "DELETE_COLLECTION_GQL",
    "DELETE_CONTENTS_GQL",
    "DELETE_CONTENT_GQL",
    "DELETE_CONVERSATIONS_GQL",
    "DELETE_CONVERSATION_GQL",
    "DELETE_FEEDS_GQL",
    "DELETE_FEED_GQL",
    "DELETE_SPECIFICATION_GQL",
    "DELETE_WORKFLOWS_GQL",
    "DELETE_WORKFLOW_GQL",
    "DISABLE_ALERT_GQL",
    "DISABLE_FEED_GQL",
    "ENABLE_ALERT_GQL",
    "ENABLE_FEED_GQL",
    "EXTRACT_CONTENTS_GQL",
    "GET_ALERT_GQL",
    "GET_COLLECTION_GQL",
    "GET_CONTENT_GQL",
    "GET_CONVERSATION_GQL",
    "GET_FEED_GQL",
    "GET_PROJECT_GQL",
    "GET_SPECIFICATION_GQL",
    "GET_WORKFLOW_GQL",
    "INGEST_ENCODED_FILE_GQL",
    "INGEST_TEXT_GQL",
    "INGEST_URI_GQL",
    "IS_CONTENT_DONE_GQL",
    "IS_FEED_DONE_GQL",
    "LOOKUP_CREDITS_GQL",
    "LOOKUP_USAGE_GQL",
    "PROMPT_CONVERSATION_GQL",
    "PROMPT_SPECIFICATIONS_GQL",
    "PUBLISH_CONTENTS_GQL",
    "PUBLISH_CONVERSATION_GQL",
    "QUERY_ALERTS_GQL",
    "QUERY_COLLECTIONS_GQL",
    "QUERY_CONTENTS_GQL",
    "QUERY_CONTENT_FACETS_GQL",
    "QUERY_CONVERSATIONS_GQL",
    "QUERY_FEEDS_GQL",
    "QUERY_SPECIFICATIONS_GQL",
    "QUERY_WORKFLOWS_GQL",
    "REMOVE_CONTENTS_FROM_COLLECTION_GQL",
    "SUGGEST_CONVERSATION_GQL",
    "SUMMARIZE_CONTENTS_GQL",
    "UPDATE_ALERT_GQL",
    "UPDATE_COLLECTION_GQL",
    "UPDATE_CONTENT_GQL",
    "UPDATE_CONVERSATION_GQL",
    "UPDATE_FEED_GQL",
    "UPDATE_PROJECT_GQL",
    "UPDATE_SPECIFICATION_GQL",
    "UPDATE_WORKFLOW_GQL",
    "USAGE_GQL",
]

CREATE_ALERT_GQL = """
mutation CreateAlert($alert: AlertInput!, $correlationId: String) {
  createAlert(alert: $alert, correlationId: $correlationId) {
    id
    name
    state
    type
  }
}
"""

DELETE_ALERT_GQL = """
mutation DeleteAlert($id: ID!) {
  deleteAlert(id: $id) {
    id
    state
  }
}
"""

DELETE_ALERTS_GQL = """
mutation DeleteAlerts($ids: [ID!]!) {
  deleteAlerts(ids: $ids) {
    id
    state
  }
}
"""

DELETE_ALL_ALERTS_GQL = """
mutation DeleteAllAlerts {
  deleteAllAlerts {
    id
    state
  }
}
"""

DISABLE_ALERT_GQL = """
mutation DisableAlert($id: ID!) {
  disableAlert(id: $id) {
    id
    state
  }
}
"""

ENABLE_ALERT_GQL = """
mutation EnableAlert($id: ID!) {
  enableAlert(id: $id) {
    id
    state
  }
}
"""

GET_ALERT_GQL = """
query GetAlert($id: ID!) {
  alert(id: $id) {
    id
    name
    creationDate
    owner {
      id
    }
    state
    correlationId
    type
    summaryPrompt
    publishPrompt
    filter {
      dateRange {
        from
        to
      }
      creationDateRange {
        from
        to
      }
      types
      fileTypes
      contents {
        id
      }
      feeds {
        id
      }
      workflows {
        id
      }
      collections {
        id
      }
      observations {
        type
        observable {
          id
        }
        states
      }
    }
    integration {
      type
      uri
      slack {
        token
        channel
      }
    }
    publishing {
      type
      elevenLabs {
        model
        voice
      }
    }
    summarySpecification {
      id
    }
    publishSpecification {
      id
    }
    lastAlertDate
  }
}
"""

QUERY_ALERTS_GQL = """
query QueryAlerts($filter: AlertFilter) {
  alerts(filter: $filter) {
    results {
      id
      name
      creationDate
      owner {
        id
      }
      state
      correlationId
      type
      summaryPrompt
      publishPrompt
      filter {
        dateRange {
          from
          to
        }
        creationDateRange {
          from
          to
        }
        types
        fileTypes
        contents {
          id
        }
        feeds {
          id
        }
        workflows {
          id
        }
        collections {
          id
        }
        observations {
          type
          observable {
            id
          }
          states
        }
      }
      integration {
        type
        uri
        slack {
          token
          channel
        }
      }
      publishing {
        type
        elevenLabs {
          model
          voice
        }
      }
      summarySpecification {
        id
      }
      publishSpecification {
        id
      }
      lastAlertDate
    }
  }
}
"""

UPDATE_ALERT_GQL = """
mutation UpdateAlert($alert: AlertUpdateInput!) {
  updateAlert(alert: $alert) {
    id
    name
    state
    type
  }
}
"""

ADD_CONTENTS_TO_COLLECTIONS_GQL = """
mutation AddContentsToCollections($contents: [EntityReferenceInput!]!, $collections: [EntityReferenceInput!]!) {
  addContentsToCollections(contents: $contents, collections: $collections) {
    id
    name
    state
    type
    contents {
      id
      name
    }
  }
}
"""

CREATE_COLLECTION_GQL = """
mutation CreateCollection($collection: CollectionInput!) {
  createCollection(collection: $collection) {
    id
    name
    state
    type
  }
}
"""

DELETE_COLLECTION_GQL = """
mutation DeleteCollection($id: ID!) {
  deleteCollection(id: $id) {
    id
    state
  }
}
"""

DELETE_COLLECTIONS_GQL = """
mutation DeleteCollections($ids: [ID!]!) {
  deleteCollections(ids: $ids) {
    id
    state
  }
}
"""

GET_COLLECTION_GQL = """
query GetCollection($id: ID!) {
  collection(id: $id) {
    id
    name
    creationDate
    owner {
      id
    }
    state
    type
    contents {
      id
      name
    }
  }
}
"""

QUERY_COLLECTIONS_GQL = """
query QueryCollections($filter: CollectionFilter) {
  collections(filter: $filter) {
    results {
      id
      name
      creationDate
      owner {
        id
      }
      state
      type
      contents {
        id
        name
      }
    }
  }
}
"""

REMOVE_CONTENTS_FROM_COLLECTION_GQL = """
mutation RemoveContentsFromCollection($contents: [EntityReferenceInput!]!, $collection: EntityReferenceInput!) {
  removeContentsFromCollection(contents: $contents, collection: $collection) {
    id
    name
    state
    type
    contents {
      id
      name
    }
  }
}
"""

UPDATE_COLLECTION_GQL = """
mutation UpdateCollection($collection: CollectionUpdateInput!) {
  updateCollection(collection: $collection) {
    id
    name
    state
    type
  }
}
"""

DELETE_ALL_CONTENTS_GQL = """
mutation DeleteAllContents {
  deleteAllContents {
    id
    state
  }
}
"""

DELETE_CONTENT_GQL = """
mutation DeleteContent($id: ID!) {
  deleteContent(id: $id) {
    id
    state
  }
}
"""

DELETE_CONTENTS_GQL = """
mutation DeleteContents($ids: [ID!]!) {
  deleteContents(ids: $ids) {
    id
    state
  }
}
"""

EXTRACT_CONTENTS_GQL = """
mutation ExtractContents($prompt: String!, $filter: ContentFilter, $specification: EntityReferenceInput!, $correlationId: String) {
  extractContents(
    prompt: $prompt
    filter: $filter
    specification: $specification
    correlationId: $correlationId
  ) {
    specification {
      id
    }
    content {
      id
    }
    value
    startTime
    endTime
    pageNumber
    error
  }
}
"""

GET_CONTENT_GQL = """
query GetContent($id: ID!) {
  content(id: $id) {
    id
    name
    creationDate
    owner {
      id
    }
    state
    originalDate
    finishedDate
    workflowDuration
    uri
    type
    fileType
    mimeType
    fileName
    fileSize
    masterUri
    imageUri
    textUri
    audioUri
    transcriptUri
    video {
      width
      height
      duration
      software
      make
      model
    }
    audio {
      keywords
      author
      series
      episode
      episodeType
      season
      publisher
      copyright
      language
      genre
      title
      bitrate
      channels
      sampleRate
      bitsPerSample
      duration
    }
    image {
      width
      height
      description
      software
      identifier
      make
      model
    }
    document {
      title
      subject
      author
      software
      publisher
      description
      summary
      keywords
      pageCount
      worksheetCount
      slideCount
      wordCount
      lineCount
      paragraphCount
      characterCount
      isEncrypted
      hasDigitalSignature
    }
    email {
      subject
      identifier
      sensitivity
      priority
      importance
      labels
      from {
        name
        familyName
        givenName
        email
      }
      to {
        name
        familyName
        givenName
        email
      }
      cc {
        name
        familyName
        givenName
        email
      }
      bcc {
        name
        familyName
        givenName
        email
      }
    }
    issue {
      title
      project
      team
      status
      priority
      type
      identifier
      labels
    }
    observations {
      type
      observable {
        id
        name
      }
      occurrences {
        type
        confidence
        boundingBox {
          left
          top
          width
          height
        }
        pageIndex
        startTime
        endTime
      }
    }
    parent {
      id
    }
    children {
      id
    }
    collections {
      id
    }
    feed {
      id
    }
    workflow {
      id
    }
    markdown
    links {
      uri
      linkType
    }
    error
  }
}
"""

INGEST_ENCODED_FILE_GQL = """
mutation IngestEncodedFile($name: String!, $data: String!, $mimeType: String!, $id: ID, $isSynchronous: Boolean, $collections: [EntityReferenceInput!], $workflow: EntityReferenceInput, $correlationId: String) {
  ingestEncodedFile(
    name: $name
    data: $data
    mimeType: $mimeType
    id: $id
    isSynchronous: $isSynchronous
    collections: $collections
    workflow: $workflow
    correlationId: $correlationId
  ) {
    id
    name
    state
    type
    fileType
    mimeType
    uri
  }
}
"""

INGEST_TEXT_GQL = """
mutation IngestText($name: String!, $text: String!, $textType: TextTypes, $uri: URL, $id: ID, $isSynchronous: Boolean, $collections: [EntityReferenceInput!], $workflow: EntityReferenceInput, $correlationId: String) {
  ingestText(
    name: $name
    text: $text
    textType: $textType
    uri: $uri
    id: $id
    isSynchronous: $isSynchronous
    collections: $collections
    workflow: $workflow
    correlationId: $correlationId
  ) {
    id
    name
    state
    type
    fileType
    mimeType
    uri
  }
}
"""

INGEST_URI_GQL = """
mutation IngestUri($name: String, $uri: URL!, $id: ID, $isSynchronous: Boolean, $collections: [EntityReferenceInput!], $workflow: EntityReferenceInput, $correlationId: String) {
  ingestUri(
    name: $name
    uri: $uri
    id: $id
    collections: $collections
    workflow: $workflow
    isSynchronous: $isSynchronous
    correlationId: $correlationId
  ) {
    id
    name
    state
    type
    fileType
    mimeType
    uri
  }
}
"""

IS_CONTENT_DONE_GQL = """
query IsContentDone($id: ID!) {
  isContentDone(id: $id) {
    result
  }
}
"""

PUBLISH_CONTENTS_GQL = """
mutation PublishContents($summaryPrompt: String, $publishPrompt: String!, $connector: ContentPublishingConnectorInput!, $filter: ContentFilter, $correlationId: String, $name: String, $summarySpecification: EntityReferenceInput, $publishSpecification: EntityReferenceInput, $workflow: EntityReferenceInput) {
  publishContents(
    summaryPrompt: $summaryPrompt
    publishPrompt: $publishPrompt
    connector: $connector
    filter: $filter
    correlationId: $correlationId
    name: $name
    summarySpecification: $summarySpecification
    publishSpecification: $publishSpecification
    workflow: $workflow
  ) {
    id
    name
    state
    type
    fileType
    mimeType
    uri
    textUri
    audioUri
    markdown
  }
}
"""

QUERY_CONTENT_FACETS_GQL = """
query QueryContentFacets($filter: ContentFilter, $facets: [ContentFacetInput!]) {
  contents(filter: $filter, facets: $facets) {
    facets {
      facet
      type
      observable {
        type
        observable {
          id
          name
        }
      }
      count
    }
  }
}
"""

QUERY_CONTENTS_GQL = """
query QueryContents($filter: ContentFilter) {
  contents(filter: $filter) {
    results {
      id
      name
      creationDate
      owner {
        id
      }
      state
      originalDate
      finishedDate
      workflowDuration
      uri
      type
      fileType
      mimeType
      fileName
      fileSize
      masterUri
      imageUri
      textUri
      audioUri
      transcriptUri
      video {
        width
        height
        duration
        software
        make
        model
      }
      audio {
        keywords
        author
        series
        episode
        episodeType
        season
        publisher
        copyright
        language
        genre
        title
        bitrate
        channels
        sampleRate
        bitsPerSample
        duration
      }
      image {
        width
        height
        description
        software
        identifier
        make
        model
      }
      document {
        title
        subject
        author
        software
        publisher
        description
        summary
        keywords
        pageCount
        worksheetCount
        slideCount
        wordCount
        lineCount
        paragraphCount
        characterCount
        isEncrypted
        hasDigitalSignature
      }
      email {
        subject
        identifier
        sensitivity
        priority
        importance
        labels
        from {
          name
          familyName
          givenName
          email
        }
        to {
          name
          familyName
          givenName
          email
        }
        cc {
          name
          familyName
          givenName
          email
        }
        bcc {
          name
          familyName
          givenName
          email
        }
      }
      issue {
        title
        project
        team
        status
        priority
        type
        identifier
        labels
      }
      observations {
        type
        observable {
          id
          name
        }
        occurrences {
          type
          confidence
          boundingBox {
            left
            top
            width
            height
          }
          pageIndex
          startTime
          endTime
        }
      }
      parent {
        id
      }
      children {
        id
      }
      collections {
        id
      }
      feed {
        id
      }
      workflow {
        id
      }
      markdown
      links {
        uri
        linkType
      }
      error
    }
  }
}
"""

SUMMARIZE_CONTENTS_GQL = """
mutation SummarizeContents($summarizations: [SummarizationStrategyInput!]!, $filter: ContentFilter, $correlationId: String) {
  summarizeContents(
    summarizations: $summarizations
    filter: $filter
    correlationId: $correlationId
  ) {
    specification {
      id
    }
    content {
      id
    }
    type
    items {
      text
      tokens
      summarizationTime
    }
    error
  }
}
"""

UPDATE_CONTENT_GQL = """
mutation UpdateContent($content: ContentUpdateInput!) {
  updateContent(content: $content) {
    id
    name
    state
    type
    fileType
    mimeType
    uri
  }
}
"""

CLEAR_CONVERSATION_GQL = """
mutation ClearConversation($id: ID!) {
  clearConversation(id: $id) {
    id
    name
    state
    type
  }
}
"""

CLOSE_CONVERSATION_GQL = """
mutation CloseConversation($id: ID!) {
  closeConversation(id: $id) {
    id
    name
    state
    type
  }
}
"""

CREATE_CONVERSATION_GQL = """
mutation CreateConversation($conversation: ConversationInput!, $correlationId: String) {
  createConversation(conversation: $conversation, correlationId: $correlationId) {
    id
    name
    state
    type
  }
}
"""

DELETE_ALL_CONVERSATIONS_GQL = """
mutation DeleteAllConversations {
  deleteAllConversations {
    id
    state
  }
}
"""

DELETE_CONVERSATION_GQL = """
mutation DeleteConversation($id: ID!) {
  deleteConversation(id: $id) {
    id
    state
  }
}
"""

DELETE_CONVERSATIONS_GQL = """
mutation DeleteConversations($ids: [ID!]!) {
  deleteConversations(ids: $ids) {
    id
    state
  }
}
"""

GET_CONVERSATION_GQL = """
query GetConversation($id: ID!) {
  conversation(id: $id) {
    id
    name
    creationDate
    owner {
      id
    }
    state
    correlationId
    type
    messages {
      role
      author
      message
      citations {
        content {
          id
        }
        index
        text
        startTime
        endTime
        pageNumber
        frameNumber
      }
      tokens
      throughput
      completionTime
      timestamp
      modelService
      model
    }
    specification {
      id
      name
    }
    filter {
      dateRange {
        from
        to
      }
      creationDateRange {
        from
        to
      }
      types
      fileTypes
      contents {
        id
      }
      feeds {
        id
      }
      workflows {
        id
      }
      collections {
        id
      }
      observations {
        type
        observable {
          id
        }
        states
      }
    }
  }
}
"""

PROMPT_CONVERSATION_GQL = """
mutation PromptConversation($prompt: String!, $id: ID, $correlationId: String) {
  promptConversation(prompt: $prompt, id: $id, correlationId: $correlationId) {
    conversation {
      id
    }
    message {
      role
      author
      message
      citations {
        content {
          id
          type
          fileType
          fileName
        }
        index
        text
        startTime
        endTime
        pageNumber
        frameNumber
      }
      tokens
      throughput
      completionTime
      timestamp
      modelService
      model
    }
    messageCount
    facets {
      type
      value
      range {
        from
        to
      }
      count
      facet
      observable {
        type
        observable {
          id
          name
        }
      }
    }
  }
}
"""

PUBLISH_CONVERSATION_GQL = """
mutation PublishConversation($id: ID!, $connector: ContentPublishingConnectorInput!, $name: String, $workflow: EntityReferenceInput, $correlationId: String) {
  publishConversation(
    id: $id
    connector: $connector
    name: $name
    workflow: $workflow
    correlationId: $correlationId
  ) {
    id
    name
    state
    type
    fileType
    mimeType
    uri
    textUri
    audioUri
    markdown
  }
}
"""

QUERY_CONVERSATIONS_GQL = """
query QueryConversations($filter: ConversationFilter) {
  conversations(filter: $filter) {
    results {
      id
      name
      creationDate
      owner {
        id
      }
      state
      correlationId
      type
      messages {
        role
        author
        message
        citations {
          content {
            id
          }
          index
          text
          startTime
          endTime
          pageNumber
          frameNumber
        }
        tokens
        throughput
        completionTime
        timestamp
        modelService
        model
      }
      specification {
        id
        name
      }
      filter {
        dateRange {
          from
          to
        }
        creationDateRange {
          from
          to
        }
        types
        fileTypes
        contents {
          id
        }
        feeds {
          id
        }
        workflows {
          id
        }
        collections {
          id
        }
        observations {
          type
          observable {
            id
          }
          states
        }
      }
    }
  }
}
"""

SUGGEST_CONVERSATION_GQL = """
mutation SuggestConversation($id: ID!, $count: Int, $correlationId: String) {
  suggestConversation(id: $id, count: $count, correlationId: $correlationId) {
    prompts
  }
}
"""

UPDATE_CONVERSATION_GQL = """
mutation UpdateConversation($conversation: ConversationUpdateInput!) {
  updateConversation(conversation: $conversation) {
    id
    name
    state
    type
  }
}
"""

CREATE_FEED_GQL = """
mutation CreateFeed($feed: FeedInput!, $correlationId: String) {
  createFeed(feed: $feed, correlationId: $correlationId) {
    id
    name
    state
    type
  }
}
"""

DELETE_ALL_FEEDS_GQL = """
mutation DeleteAllFeeds {
  deleteAllFeeds {
    id
    state
  }
}
"""

DELETE_FEED_GQL = """
mutation DeleteFeed($id: ID!) {
  deleteFeed(id: $id) {
    id
    state
  }
}
"""

DELETE_FEEDS_GQL = """
mutation DeleteFeeds($ids: [ID!]!) {
  deleteFeeds(ids: $ids) {
    id
    state
  }
}
"""

DISABLE_FEED_GQL = """
mutation DisableFeed($id: ID!) {
  disableFeed(id: $id) {
    id
    state
  }
}
"""

ENABLE_FEED_GQL = """
mutation EnableFeed($id: ID!) {
  enableFeed(id: $id) {
    id
    state
  }
}
"""

GET_FEED_GQL = """
query GetFeed($id: ID!) {
  feed(id: $id) {
    id
    name
    creationDate
    owner {
      id
    }
    state
    correlationId
    type
    site {
      siteType
      type
      isRecursive
      s3 {
        accessKey
        secretAccessKey
        bucketName
        prefix
        region
      }
      azureBlob {
        storageAccessKey
        accountName
        containerName
        prefix
      }
      azureFile {
        storageAccessKey
        accountName
        shareName
        prefix
      }
      google {
        credentials
        containerName
        prefix
      }
      sharePoint {
        authenticationType
        accountName
        libraryId
        tenantId
        refreshToken
      }
      oneDrive {
        folderId
        refreshToken
      }
      googleDrive {
        folderId
        refreshToken
      }
    }
    email {
      type
      includeAttachments
      google {
        type
        refreshToken
      }
      microsoft {
        type
        tenantId
        refreshToken
      }
    }
    issue {
      type
      includeAttachments
      jira {
        uri
        project
        email
        token
      }
      linear {
        key
        project
      }
      github {
        uri
        repositoryOwner
        repositoryName
        refreshToken
        personalAccessToken
      }
    }
    rss {
      readLimit
      uri
    }
    web {
      readLimit
      uri
      includeFiles
    }
    reddit {
      readLimit
      subredditName
    }
    notion {
      readLimit
      token
      identifiers
      type
    }
    youtube {
      readLimit
      type
      videoName
      videoIdentifiers
      channelIdentifier
      playlistIdentifier
    }
    slack {
      readLimit
      type
      token
      channel
      includeAttachments
    }
    discord {
      readLimit
      type
      token
      channel
      includeAttachments
    }
    error
    lastPostDate
    lastReadDate
    readCount
    workflow {
      id
      name
    }
    schedulePolicy {
      recurrenceType
      repeatInterval
    }
  }
}
"""

IS_FEED_DONE_GQL = """
query IsFeedDone($id: ID!) {
  isFeedDone(id: $id) {
    result
  }
}
"""

QUERY_FEEDS_GQL = """
query QueryFeeds($filter: FeedFilter) {
  feeds(filter: $filter) {
    results {
      id
      name
      creationDate
      owner {
        id
      }
      state
      correlationId
      type
      site {
        siteType
        type
        isRecursive
        s3 {
          accessKey
          secretAccessKey
          bucketName
          prefix
          region
        }
        azureBlob {
          storageAccessKey
          accountName
          containerName
          prefix
        }
        azureFile {
          storageAccessKey
          accountName
          shareName
          prefix
        }
        google {
          credentials
          containerName
          prefix
        }
        sharePoint {
          authenticationType
          accountName
          libraryId
          tenantId
          refreshToken
        }
        oneDrive {
          folderId
          refreshToken
        }
        googleDrive {
          folderId
          refreshToken
        }
      }
      email {
        type
        includeAttachments
        google {
          type
          refreshToken
        }
        microsoft {
          type
          tenantId
          refreshToken
        }
      }
      issue {
        type
        includeAttachments
        jira {
          uri
          project
          email
          token
        }
        linear {
          key
          project
        }
        github {
          uri
          repositoryOwner
          repositoryName
          refreshToken
          personalAccessToken
        }
      }
      rss {
        readLimit
        uri
      }
      web {
        readLimit
        uri
        includeFiles
      }
      reddit {
        readLimit
        subredditName
      }
      notion {
        readLimit
        token
        identifiers
        type
      }
      youtube {
        readLimit
        type
        videoName
        videoIdentifiers
        channelIdentifier
        playlistIdentifier
      }
      slack {
        readLimit
        type
        token
        channel
        includeAttachments
      }
      discord {
        readLimit
        type
        token
        channel
        includeAttachments
      }
      error
      lastPostDate
      lastReadDate
      readCount
      workflow {
        id
        name
      }
      schedulePolicy {
        recurrenceType
        repeatInterval
      }
    }
  }
}
"""

UPDATE_FEED_GQL = """
mutation UpdateFeed($feed: FeedUpdateInput!) {
  updateFeed(feed: $feed) {
    id
    name
    state
    type
  }
}
"""

CREDITS_GQL = """
query Credits($startDate: DateTime!, $duration: TimeSpan!) {
  credits(startDate: $startDate, duration: $duration) {
    correlationId
    ownerId
    credits
    storageRatio
    computeRatio
    preparationRatio
    extractionRatio
    enrichmentRatio
    publishingRatio
    searchRatio
    conversationRatio
  }
}
"""

GET_PROJECT_GQL = """
query GetProject {
  project {
    id
    name
    creationDate
    modifiedDate
    state
    environmentType
    platform
    region
    workflow {
      id
      name
    }
    specification {
      id
      name
    }
    quota {
      storage
      contents
      feeds
      posts
      conversations
    }
    callbackUri
  }
}
"""

LOOKUP_CREDITS_GQL = """
query LookupCredits($correlationId: String!) {
  lookupCredits(correlationId: $correlationId) {
    correlationId
    ownerId
    credits
    storageRatio
    computeRatio
    preparationRatio
    extractionRatio
    enrichmentRatio
    publishingRatio
    searchRatio
    conversationRatio
  }
}
"""

LOOKUP_USAGE_GQL = """
query LookupUsage($correlationId: String!) {
  lookupUsage(correlationId: $correlationId) {
    correlationId
    date
    credits
    name
    metric
    workflow
    entityType
    entityId
    projectId
    ownerId
    uri
    duration
    throughput
    contentType
    fileType
    modelService
    modelName
    processorName
    prompt
    promptTokens
    completion
    completionTokens
    tokens
    count
    request
    variables
    response
  }
}
"""

UPDATE_PROJECT_GQL = """
mutation UpdateProject($project: ProjectUpdateInput!) {
  updateProject(project: $project) {
    id
    name
  }
}
"""

USAGE_GQL = """
query Usage($startDate: DateTime!, $duration: TimeSpan!) {
  usage(startDate: $startDate, duration: $duration) {
    correlationId
    date
    credits
    name
    metric
    workflow
    entityType
    entityId
    projectId
    ownerId
    uri
    duration
    throughput
    contentType
    fileType
    modelService
    modelName
    processorName
    prompt
    promptTokens
    completion
    completionTokens
    tokens
    count
    request
    variables
    response
  }
}
"""

CREATE_SPECIFICATION_GQL = """
mutation CreateSpecification($specification: SpecificationInput!) {
  createSpecification(specification: $specification) {
    id
    name
    state
    type
    serviceType
  }
}
"""

DELETE_SPECIFICATION_GQL = """
mutation DeleteSpecification($id: ID!) {
  deleteSpecification(id: $id) {
    id
    state
  }
}
"""

GET_SPECIFICATION_GQL = """
query GetSpecification($id: ID!) {
  specification(id: $id) {
    id
    name
    creationDate
    owner {
      id
    }
    state
    type
    serviceType
    systemPrompt
    customGuidance
    strategy {
      type
      messageLimit
      embedCitations
      enableFacets
      messagesWeight
      contentsWeight
    }
    promptStrategy {
      type
    }
    retrievalStrategy {
      type
      contentLimit
    }
    rerankingStrategy {
      serviceType
    }
    openAI {
      tokenLimit
      completionTokenLimit
      model
      key
      modelName
      temperature
      probability
    }
    azureOpenAI {
      tokenLimit
      completionTokenLimit
      model
      key
      endpoint
      deploymentName
      temperature
      probability
    }
    anthropic {
      tokenLimit
      completionTokenLimit
      model
      key
      modelName
      temperature
      probability
    }
    replicate {
      tokenLimit
      completionTokenLimit
      model
      key
      modelName
      temperature
      probability
    }
    tools {
      name
      description
      schema
      uri
    }
  }
}
"""

PROMPT_SPECIFICATIONS_GQL = """
mutation PromptSpecifications($prompt: String!, $ids: [ID!]!) {
  promptSpecifications(prompt: $prompt, ids: $ids) {
    specification {
      id
    }
    messages {
      role
      author
      message
      citations {
        content {
          id
        }
        index
        text
        startTime
        endTime
        pageNumber
        frameNumber
      }
      tokens
      throughput
      completionTime
      timestamp
      modelService
      model
    }
    error
  }
}
"""

QUERY_SPECIFICATIONS_GQL = """
query QuerySpecifications($filter: SpecificationFilter) {
  specifications(filter: $filter) {
    results {
      id
      name
      creationDate
      owner {
        id
      }
      state
      type
      serviceType
      systemPrompt
      customGuidance
      strategy {
        type
        messageLimit
        embedCitations
        enableFacets
        messagesWeight
        contentsWeight
      }
      promptStrategy {
        type
      }
      retrievalStrategy {
        type
        contentLimit
      }
      rerankingStrategy {
        serviceType
      }
      openAI {
        tokenLimit
        completionTokenLimit
        model
        key
        modelName
        temperature
        probability
      }
      azureOpenAI {
        tokenLimit
        completionTokenLimit
        model
        key
        endpoint
        deploymentName
        temperature
        probability
      }
      anthropic {
        tokenLimit
        completionTokenLimit
        model
        key
        modelName
        temperature
        probability
      }
      replicate {
        tokenLimit
        completionTokenLimit
        model
        key
        modelName
        temperature
        probability
      }
      tools {
        name
        description
        schema
        uri
      }
    }
  }
}
"""

UPDATE_SPECIFICATION_GQL = """
mutation UpdateSpecification($specification: SpecificationUpdateInput!) {
  updateSpecification(specification: $specification) {
    id
    name
    state
    type
    serviceType
  }
}
"""

CREATE_WORKFLOW_GQL = """
mutation CreateWorkflow($workflow: WorkflowInput!) {
  createWorkflow(workflow: $workflow) {
    id
    name
    state
    ingestion {
      if {
        types
        fileTypes
      }
      collections {
        id
      }
    }
    preparation {
      disableSmartCapture
      summarizations {
        type
        specification {
          id
        }
        tokens
        items
      }
      jobs {
        connector {
          type
          fileTypes
          azureDocument {
            model
          }
          deepgram {
            model
            key
            enableRedaction
            enableSpeakerDiarization
          }
          document {
            includeImages
          }
          email {
            includeAttachments
          }
        }
      }
    }
    extraction {
      jobs {
        connector {
          type
          contentTypes
          fileTypes
          extractedTypes
          azureText {
            confidenceThreshold
            enablePII
          }
          azureImage {
            confidenceThreshold
          }
          openAIImage {
            confidenceThreshold
            detailLevel
          }
          modelText {
            specification {
              id
            }
          }
        }
      }
    }
    enrichment {
      link {
        enableCrawling
        allowedDomains
        excludedDomains
        allowedLinks
        excludedLinks
        allowedFiles
        excludedFiles
        allowContentDomain
        maximumLinks
      }
      jobs {
        connector {
          type
          enrichedTypes
        }
      }
    }
    actions {
      connector {
        type
        uri
        slack {
          token
          channel
        }
      }
    }
  }
}
"""

DELETE_ALL_WORKFLOWS_GQL = """
mutation DeleteAllWorkflows {
  deleteAllWorkflows {
    id
    state
  }
}
"""

DELETE_WORKFLOW_GQL = """
mutation DeleteWorkflow($id: ID!) {
  deleteWorkflow(id: $id) {
    id
    state
  }
}
"""

DELETE_WORKFLOWS_GQL = """
mutation DeleteWorkflows($ids: [ID!]!) {
  deleteWorkflows(ids: $ids) {
    id
    state
  }
}
"""

GET_WORKFLOW_GQL = """
query GetWorkflow($id: ID!) {
  workflow(id: $id) {
    id
    name
    creationDate
    owner {
      id
    }
    state
    ingestion {
      if {
        types
        fileTypes
      }
      collections {
        id
      }
    }
    preparation {
      disableSmartCapture
      summarizations {
        type
        specification {
          id
        }
        tokens
        items
      }
      jobs {
        connector {
          type
          fileTypes
          azureDocument {
            model
          }
          deepgram {
            model
            key
            enableRedaction
            enableSpeakerDiarization
          }
          document {
            includeImages
          }
          email {
            includeAttachments
          }
        }
      }
    }
    extraction {
      jobs {
        connector {
          type
          contentTypes
          fileTypes
          extractedTypes
          azureText {
            confidenceThreshold
            enablePII
          }
          azureImage {
            confidenceThreshold
          }
          openAIImage {
            confidenceThreshold
            detailLevel
          }
          modelText {
            specification {
              id
            }
          }
        }
      }
    }
    enrichment {
      link {
        enableCrawling
        allowedDomains
        excludedDomains
        allowedLinks
        excludedLinks
        allowedFiles
        excludedFiles
        allowContentDomain
        maximumLinks
      }
      jobs {
        connector {
          type
          enrichedTypes
        }
      }
    }
    actions {
      connector {
        type
        uri
        slack {
          token
          channel
        }
      }
    }
  }
}
"""

QUERY_WORKFLOWS_GQL = """
query QueryWorkflows($filter: WorkflowFilter) {
  workflows(filter: $filter) {
    results {
      id
      name
      creationDate
      owner {
        id
      }
      state
      ingestion {
        if {
          types
          fileTypes
        }
        collections {
          id
        }
      }
      preparation {
        disableSmartCapture
        summarizations {
          type
          specification {
            id
          }
          tokens
          items
        }
        jobs {
          connector {
            type
            fileTypes
            azureDocument {
              model
            }
            deepgram {
              model
              key
              enableRedaction
              enableSpeakerDiarization
            }
            document {
              includeImages
            }
            email {
              includeAttachments
            }
          }
        }
      }
      extraction {
        jobs {
          connector {
            type
            contentTypes
            fileTypes
            extractedTypes
            azureText {
              confidenceThreshold
              enablePII
            }
            azureImage {
              confidenceThreshold
            }
            openAIImage {
              confidenceThreshold
              detailLevel
            }
            modelText {
              specification {
                id
              }
            }
          }
        }
      }
      enrichment {
        link {
          enableCrawling
          allowedDomains
          excludedDomains
          allowedLinks
          excludedLinks
          allowedFiles
          excludedFiles
          allowContentDomain
          maximumLinks
        }
        jobs {
          connector {
            type
            enrichedTypes
          }
        }
      }
      actions {
        connector {
          type
          uri
          slack {
            token
            channel
          }
        }
      }
    }
  }
}
"""

UPDATE_WORKFLOW_GQL = """
mutation UpdateWorkflow($workflow: WorkflowUpdateInput!) {
  updateWorkflow(workflow: $workflow) {
    id
    name
    state
    ingestion {
      if {
        types
        fileTypes
      }
      collections {
        id
      }
    }
    preparation {
      disableSmartCapture
      summarizations {
        type
        specification {
          id
        }
        tokens
        items
      }
      jobs {
        connector {
          type
          fileTypes
          azureDocument {
            model
          }
          deepgram {
            model
            key
            enableRedaction
            enableSpeakerDiarization
          }
          document {
            includeImages
          }
          email {
            includeAttachments
          }
        }
      }
    }
    extraction {
      jobs {
        connector {
          type
          contentTypes
          fileTypes
          extractedTypes
          azureText {
            confidenceThreshold
            enablePII
          }
          azureImage {
            confidenceThreshold
          }
          openAIImage {
            confidenceThreshold
            detailLevel
          }
          modelText {
            specification {
              id
            }
          }
        }
      }
    }
    enrichment {
      link {
        enableCrawling
        allowedDomains
        excludedDomains
        allowedLinks
        excludedLinks
        allowedFiles
        excludedFiles
        allowContentDomain
        maximumLinks
      }
      jobs {
        connector {
          type
          enrichedTypes
        }
      }
    }
    actions {
      connector {
        type
        uri
        slack {
          token
          channel
        }
      }
    }
  }
}
"""
