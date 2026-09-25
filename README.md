# Vectra-shell-
senior design project
                            ┌──────────────────────────────────────────────┐
                            │   System Architect (Person 1)                │
                            │   Framework: LangGraph / Pydantic            │
                            └──────────────────────┬───────────────────────┘
                                                   │
         ┌─────────────────────────────────────────┼─────────────────────────────────────────┐
         ▼                                         ▼                                         ▼
┌─────────────────────────┐               ┌─────────────────────────┐               ┌─────────────────────────┐
│  Ingestion (Person 2)   │               │ Threat Intel (Person 3) │               │ AI Reasoning (Person 4) │
│                         │               │                         │               │                         │
│  • tree-sitter          │  ──(Python)─► │  • chromadb             │  ──(Python)─► │  • litellm / langchain   │
│  • ast / nbformat       │   Dict/JSON   │  • requests / nvdlib    │   Dict/JSON   │  • Prompt Engineering   │
└─────────────────────────┘               └─────────────────────────┘               └─────────────────────────┘
                                                                                                 │
                                                                                                 ▼
                                                                                    ┌─────────────────────────┐
                                                                                    │  DevSecOps (Person 5)   │
                                                                                    │                         │
                                                                                    │  • typer (CLI UI)       │
                                                                                    │  • pytest framework     │
                                                                                    └─────────────────────────┘
