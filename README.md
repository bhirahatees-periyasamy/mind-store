# 🧠 Vault — Semantic Memory Microservice

## 📌 Overview

**Vault** is the semantic memory microservice of the CargoMind system.
It is responsible for ingesting repositories, generating embeddings, indexing knowledge, and providing retrieval capabilities that enable CargoMind to reason across large codebases.

Vault follows a **retrieval-augmented memory architecture**, separating knowledge storage from execution logic to improve scalability, modularity, and experimentation.

---

## 🎯 Objectives

Vault aims to provide:

* Repository-scale semantic memory
* Fast contextual retrieval
* Language-model-friendly knowledge representation
* Modular embedding and vector storage abstraction
* A stable API for CargoMind integration

---
## Folder Structure
```
Vault/
│
├── README.md
├── pyproject.toml
├── requirements.txt
├── .gitignore
│
├── docs/
│   └── architecture.md
│
├── app/                      # main package
│   │
│   ├── main.py               # service entry
│   │
│   ├── api/                  # HTTP routes
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── health.py
│   │
│   ├── indexing/             # ingestion pipeline
│   │   ├── __init__.py
│   │   ├── chunker.py
│   │   ├── loader.py
│   │   └── indexer.py
│   │
│   ├── embeddings/           # embedding abstraction
│   │   ├── __init__.py
│   │   └── embedder.py
│   │
│   ├── vector/               # vector DB wrapper
│   │   ├── __init__.py
│   │   └── store.py
│   │
│   ├── retrieval/            # semantic search
│   │   ├── __init__.py
│   │   └── search.py
│   │
│   ├── models/               # request/response schemas
│   │   ├── __init__.py
│   │   └── schemas.py
│   │
│   ├── core/                 # config, logging
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── logging.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── file_utils.py
│
├── tests/
│   ├── test_indexing.py
│   └── test_retrieval.py
│
└── scripts/                  # helper scripts
    └── index_repo.py
```


---

## 🏗️ Architecture

### High-level flow

```
Repository → Loader → Chunker → Embedder → Vector Store → Retrieval API
```

### System interaction

```
CargoMind → Vault API → Retrieval → Vector DB → Context returned
```

Vault does not perform reasoning or execution; it serves as a knowledge layer.

---

## 📦 Core Responsibilities

### 1. Repository ingestion

* Load files from local repositories
* Filter supported file types
* Normalize content
* Track metadata (path, language, repo)

### 2. Chunking

* Split files into semantically meaningful segments
* Maintain contextual boundaries
* Preserve metadata mapping

### 3. Embedding generation

* Convert chunks into vector representations
* Support pluggable embedding providers
* Enable future model swapping

### 4. Vector storage

* Persist embeddings
* Support similarity search
* Maintain metadata alongside vectors

### 5. Retrieval

* Accept semantic queries
* Perform similarity search
* Rank results
* Return structured context

---

## 🧩 Module Design

### API Layer

**Purpose:** expose HTTP interface for CargoMind

Responsibilities:

* request validation
* response formatting
* routing
* health monitoring

---

### Indexing Layer

**Purpose:** convert repositories into searchable knowledge

Components:

* loader
* chunker
* indexer

Responsibilities:

* ingestion orchestration
* metadata assignment
* embedding pipeline invocation

---

### Embeddings Layer

**Purpose:** abstraction over embedding providers

Responsibilities:

* text-to-vector conversion
* provider swapping
* batching
* rate control

---

### Vector Layer

**Purpose:** storage abstraction for vector database

Responsibilities:

* insert embeddings
* similarity search
* metadata persistence
* provider independence

---

### Retrieval Layer

**Purpose:** query-time context discovery

Responsibilities:

* query embedding
* similarity search
* ranking
* context packaging

---

### Core Layer

**Purpose:** shared infrastructure

Responsibilities:

* configuration
* logging
* environment handling
* dependency wiring

---

## 🔗 API Contract

### Index repository

**POST** `/index`

#### Request

```
{
  "path": "/repo/path"
}
```

#### Behavior

* loads repository
* chunks files
* generates embeddings
* persists vectors

---

### Semantic search

**POST** `/search`

#### Request

```
{
  "query": "authentication logic",
  "k": 5
}
```

#### Response

```
{
  "results": [
    {
      "content": "...",
      "path": "src/auth.rs",
      "score": 0.92
    }
  ]
}
```

---

### Health check

**GET** `/health`

#### Purpose

* service readiness
* orchestration monitoring

---

## 🧠 Data Model

### Chunk

* id
* content
* path
* language
* repo
* position metadata

### Embedding record

* chunk id
* vector
* metadata

### Retrieval result

* content
* metadata
* similarity score

---

## ⚙️ Design Principles

### Separation of concerns

Vault does not perform reasoning or planning.

### Provider abstraction

Embedding and vector providers must be replaceable.

### Stateless API

All state resides in storage layers.

### Metadata-first design

Context must remain traceable to source files.

### Incremental extensibility

New ingestion strategies and retrieval algorithms should be addable without breaking API.

---

## 🧪 Testing Strategy

### Unit tests

* chunking correctness
* embedding pipeline
* vector storage operations

### Integration tests

* indexing pipeline
* retrieval accuracy
* API behavior

### Evaluation tests

* query relevance
* context completeness
* latency thresholds

---

## 🚀 Future Extensions

* incremental indexing
* background indexing workers
* multi-repository memory
* hybrid lexical + semantic search
* temporal memory
* caching layer
* access control
* distributed vector storage

---

## 🏁 MVP Definition

Vault is considered MVP-complete when:

* repository indexing works end-to-end
* embeddings are generated
* semantic search returns relevant chunks
* API integration with CargoMind succeeds
* metadata mapping remains intact

---

## 📖 System Role Summary

Vault acts as the semantic memory substrate of CargoMind, enabling repository-scale understanding by transforming raw code into structured, retrievable knowledge.

It provides the contextual foundation required for autonomous coding agents to reason beyond immediate context windows.

---
