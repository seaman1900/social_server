from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class PrintMetadata(BaseModel):
    views: int
    comments: int
    likes: int
    dislikes: int
    total_invest: int

class Print(BaseModel):
    print_id: str
    author_id: str
    title: str
    created_at: datetime
    price: int
    description: str
    body: str
    metadata: PrintMetadata
    tags: List[str]
    status: str