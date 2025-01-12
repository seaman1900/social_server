from datetime import datetime
from models.balance import Balance
from fastapi import APIRouter
from fake_dbs.fake_balance import fake_balances
from loguru import logger

router = APIRouter(prefix="/balance", tags=["balance"])

# Get a balance by id
@router.get("/{user_id}")
def get_balances(user_id: str):
    return fake_balances[user_id].balance

# update balance
@router.put("/{user_id}")
def update_balance(user_id: str, balance: Balance):
    fake_balances[user_id].balance += balance.balance
    fake_balances[user_id].frozen_amount += balance.frozen_amount
    fake_balances[user_id].last_update_time = datetime.now()
    logger.info(f"User {user_id} balance updated to {fake_balances[user_id].balance}")
    return fake_balances[user_id].balance