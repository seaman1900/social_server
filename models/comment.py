from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Media(BaseModel):
    type: str  # 例如: "image", "video"
    url: str

class Comment(BaseModel):
    comment_id: str
    user_id: str
    username: str
    avatar_url: str
    content: str
    media: List[Media]
    timestamp: datetime
    updated_at: datetime
    likes: int
    dislikes: int
    replies: int
    parent_comment_id: Optional[str] = None  # 父评论ID（如果是回复）
    root_comment_id: Optional[str] = None   # 根评论ID（如果是回复）
    status: str  # 例如: "approved", "pending", "rejected"
    is_deleted: bool