from typing import List, Dict
from fastapi import APIRouter
from fastapi import HTTPException, Path

from models.invest import Investment
from tools.misc import generate_investment_id

router = APIRouter(prefix="/invest", tags=["users"])

# 模拟数据库
fake_investments_db: Dict[str, Investment] = {}

# 创建投资
@router.post("/", response_model=Investment)
async def create_investment(investment: Investment):
    if investment.invest_id in fake_investments_db:
        raise HTTPException(status_code=400, detail="Investment with this ID already exists")
    invest_id = generate_investment_id(investment.user_id, investment.content_id, investment.invest_time, investment.invest_amount)
    investment.invest_id = invest_id
    fake_investments_db[investment.invest_id] = investment
    return investment

# 获取用户的所有投资
@router.get("/user/{user_id}", response_model=List[Investment])
async def get_user_investments(user_id: str):
    user_investments = [inv for inv in fake_investments_db.values() if inv.user_id == user_id]
    if not user_investments:
        raise HTTPException(status_code=404, detail="No investments found for this user")
    return user_investments

# 获取单个投资的详细信息
@router.get("/{invest_id}", response_model=Investment)
async def get_investment(invest_id: str = Path(..., description="The ID of the investment to retrieve")):
    if invest_id not in fake_investments_db:
        raise HTTPException(status_code=404, detail="Investment not found")
    return fake_investments_db[invest_id]