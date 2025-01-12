from fastapi import APIRouter, HTTPException, Path
from typing import List, Dict
from loguru import logger

from models.print import Print
from wrench.misc import generate_print_id

from fake_dbs.fake_prints import fake_prints_db

router = APIRouter(prefix="/print", tags=["prints"])

# 获取所有付费内容: 应该返回简洁内容，而非完整内容，后续修改
@router.get("/all", response_model=List[Print])
async def get_all_prints():
    return list(fake_prints_db.values())

# 获取单个付费内容
@router.get("/{print_id}", response_model=Print)
async def get_by_id(user_id: str, print_id: str = Path(..., description="The ID of the print to retrieve")):
    if print_id not in fake_prints_db:
        raise HTTPException(status_code=404, detail="Print not found")
    # 校验用户是否购买该内容
    
    return fake_prints_db[print_id]

# 创建付费内容
@router.post("/create", response_model=Print)
async def create_print(print_data: Print):
    if print_data.print_id in fake_prints_db:
        raise HTTPException(status_code=400, detail="Print with this ID already exists")
    # 生成unique content
    print_id = generate_print_id(print_data.title, print_data.author_id)
    print_data.print_id = print_id
    print_data.status = "under_review"
    fake_prints_db[print_id] = print_data
    logger.info(f"Created print with ID: {print_id}")
    return print_data

# 更新付费内容
@router.put("/update/{print_id}", response_model=Print)
async def update_print(print_id: str, print_data: Print):
    if print_id not in fake_prints_db:
        raise HTTPException(status_code=404, detail="Print not found")
    
    fake_prints_db[print_id] = print_data
    return print_data

# 删除付费内容
@router.delete("/delete/{print_id}", response_model=Dict[str, str])
async def delete_print(print_id: str):
    if print_id not in fake_prints_db:
        raise HTTPException(status_code=404, detail="Print not found")
    
    del fake_prints_db[print_id]
    return {"message": "Print deleted successfully"}

# 购买print
@router.post("/buy/{print_id}", response_model=Dict[str, str])
async def buy_print(print_id: str, user_id: str):
    if print_id not in fake_prints_db:
        raise HTTPException(status_code=404, detail="Print not found")

    # 模拟购买操作
    # 这里可以根据实际需求进行购买逻辑的实现，比如扣款、记录购买记录等
    return {"message": "Print purchased successfully"}
