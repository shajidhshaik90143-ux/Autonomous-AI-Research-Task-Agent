from dataclasses import dataclass
from typing import Optional


@dataclass
class ResearchTask:
    id: Optional[int] = None
    task: str = ""
    plan: str = ""
    research: str = ""
    evaluation: str = ""
    report: str = ""
    status: str = "pending"
    created_at: Optional[str] = None


@dataclass
class Document:
    id: Optional[int] = None
    filename: str = ""
    content: str = ""
    created_at: Optional[str] = None