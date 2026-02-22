# Todo API

A REST API for managing todos, built with FastAPI.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

API docs available at http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /todos | List all todos |
| POST | /todos | Create a todo |
| GET | /todos/{id} | Get a todo |
| PUT | /todos/{id} | Update a todo |
| DELETE | /todos/{id} | Delete a todo |

## Tests

```bash
python3 -m pytest tests -v
```
