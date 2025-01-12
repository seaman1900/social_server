from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Comment(BaseModel):
    comment_id: str
    parent_id: str
    user_id: str
    create_at: datetime
    content: str
    status: str