from fastapi import APIRouter, HTTPException, Path
from typing import List, Dict
from models.print import Print
from tools.misc import generate_content_id

router = APIRouter(prefix="/print", tags=["users"])

# 模拟数据库
fake_prints_db: Dict[str, Print] = {}

# 获取所有付费内容
@router.get("/", response_model=List[Print])
async def get_all_prints():
    return list(fake_prints_db.values())

# 获取单个付费内容
@router.get("/{content_id}", response_model=Print)
async def get_print(content_id: str = Path(..., description="The ID of the print to retrieve")):
    if content_id not in fake_prints_db:
        raise HTTPException(status_code=404, detail="Print not found")
    return fake_prints_db[content_id]

# 创建付费内容
@router.post("/create", response_model=Print)
async def create_print(print_data: Print):
    if print_data.content_id in fake_prints_db:
        raise HTTPException(status_code=400, detail="Print with this ID already exists")
    # 生成unique content
    print_id = generate_content_id(print_data.title, print_data.author_id)
    print_data.content_id = print_id
    fake_prints_db[print_id] = print_data
    return print_data

# 更新付费内容
@router.put("/update/{content_id}", response_model=Print)
async def update_print(content_id: str, print_data: Print):
    if content_id not in fake_prints_db:
        raise HTTPException(status_code=404, detail="Print not found")
    
    fake_prints_db[content_id] = print_data
    return print_data

# 删除付费内容
@router.delete("/delete/{content_id}", response_model=Dict[str, str])
async def delete_print(content_id: str):
    if content_id not in fake_prints_db:
        raise HTTPException(status_code=404, detail="Print not found")
    
    del fake_prints_db[content_id]
    return {"message": "Print deleted successfully"}