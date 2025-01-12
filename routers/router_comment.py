from typing import Dict, List, Optional
from fastapi import HTTPException, Path
from models.comment import Comment
from fastapi import APIRouter

router = APIRouter(prefix="/comment", tags=["comments"])

# 模拟数据库
fake_comments_db: Dict[str, Comment] = {}

# 创建评论
@router.post("/", response_model=Comment)
async def create_comment(comment: Comment):
    if comment.comment_id in fake_comments_db:
        raise HTTPException(status_code=400, detail="Comment with this ID already exists")
    
    fake_comments_db[comment.comment_id] = comment
    return comment

# 获取单个评论
@router.get("/{comment_id}", response_model=Comment)
async def get_comment(comment_id: str = Path(..., description="The ID of the comment to retrieve")):
    if comment_id not in fake_comments_db:
        raise HTTPException(status_code=404, detail="Comment not found")
    return fake_comments_db[comment_id]

# 获取某个评论的所有回复
@router.get("/{comment_id}/replies", response_model=List[Comment])
async def get_replies(comment_id: str):
    replies = [comment for comment in fake_comments_db.values() if comment.parent_id == comment_id]
    return replies

# 更新评论
@router.put("/{comment_id}", response_model=Comment)
async def update_comment(comment_id: str, updated_comment: Comment):
    if comment_id not in fake_comments_db:
        raise HTTPException(status_code=404, detail="Comment not found")
    
    fake_comments_db[comment_id] = updated_comment
    return updated_comment

# 删除评论
@router.delete("/{comment_id}", response_model=Dict[str, str])
async def delete_comment(comment_id: str):
    if comment_id not in fake_comments_db:
        raise HTTPException(status_code=404, detail="Comment not found")
    
    del fake_comments_db[comment_id]
    return {"message": "Comment deleted successfully"}
