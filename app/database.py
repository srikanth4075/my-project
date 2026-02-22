from typing import Optional

from app.models import TodoCreate, TodoUpdate, TodoResponse

_todos: dict = {}
_next_id: int = 1


def get_all() -> list:
    return list(_todos.values())


def get_by_id(todo_id: int) -> Optional[TodoResponse]:
    return _todos.get(todo_id)


def create(todo: TodoCreate) -> TodoResponse:
    global _next_id
    new_todo = TodoResponse(id=_next_id, **todo.dict())
    _todos[_next_id] = new_todo
    _next_id += 1
    return new_todo


def update(todo_id: int, todo: TodoUpdate) -> Optional[TodoResponse]:
    existing = _todos.get(todo_id)
    if existing is None:
        return None
    updated_data = existing.dict()
    updated_data.update(todo.dict(exclude_unset=True))
    updated = TodoResponse(**updated_data)
    _todos[todo_id] = updated
    return updated


def delete(todo_id: int) -> bool:
    return _todos.pop(todo_id, None) is not None
