# SRE AI Assistant

A lightweight AI assistant that ingests Terraform, Kubernetes, and GitHub Actions context and enables you to query your infrastructure using GPT-4 or other LLMs.

## Features
- Parses real SRE context (Terraform, FluxCD, GitHub Actions)
- Indexes context using vector embeddings
- Provides a conversational interface to query your stack

## Setup
1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your OpenAI API key in a `.env` file
4. Run: `python main.py`

## Folder Structure
```
sre-ai-assistant/
├── ingest/
├── context_index/
├── prompt_engine/
├── main.py
└── config.yaml
```