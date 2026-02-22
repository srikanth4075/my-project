# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

FastAPI-based Todo REST API with in-memory storage.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run dev server (auto-reload)
uvicorn app.main:app --reload

# Run dev server on a specific port
uvicorn app.main:app --reload --port 8080

# Run all tests
python3 -m pytest tests -v

# Run a single test
python3 -m pytest tests/test_todos.py::test_create_todo -v
```

Swagger UI is available at `http://127.0.0.1:8000/docs` when the server is running.

## Architecture

- `app/main.py` — FastAPI app and route definitions (CRUD endpoints under `/todos`)
- `app/models.py` — Pydantic models: `TodoCreate`, `TodoUpdate`, `TodoResponse`
- `app/database.py` — In-memory storage layer with `get_all`, `get_by_id`, `create`, `update`, `delete` functions
