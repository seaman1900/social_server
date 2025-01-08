from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class PrintMetadata(BaseModel):
    views: int
    comments: int
    likes: int
    dislikes: int
    shares: int

class Print(BaseModel):
    content_id: str
    title: str
    author_id: str
    created_at: datetime
    price: float
    description: str
    content_body: str
    metadata: PrintMetadata
    pricing_type: str
    tags: List[str]
    comments: List[str]
    status: str