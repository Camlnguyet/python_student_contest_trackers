# Data models
from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name: str
    grade: Optional[str] = None

class Contest(BaseModel):
    name: str
    date: Optional[str] = None

class Score(BaseModel):
    student_id: int
    contest_id: int
    score: float