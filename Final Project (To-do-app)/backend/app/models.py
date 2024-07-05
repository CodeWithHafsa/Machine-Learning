from sqlmodel import SQLModel, Field
from typing import Optional

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    task: str
    notes: Optional[str] = None
    due_date: Optional[str] = None
