from fastapi import APIRouter
from fastapi import HTTPException
from datetime import datetime
import hashlib

from models.transaction import Transaction, TransactionRequest
from fake_dbs.fake_transactions import fake_transactions_db

router = APIRouter(prefix="/transaction", tags=["transactions"])

@router.post("/create")
async def create_transaction(transactionRequest: TransactionRequest):
  transaction_id = hashlib.sha256(str(transactionRequest).encode('utf-8')).hexdigest()
  transaction = Transaction(
    transaction_id=transaction_id,
    trans_type=transactionRequest.trans_type,
    user_id=transactionRequest.user_id,
    print_id=transactionRequest.print_id,
    amount=transactionRequest.amount,
    created_at=datetime.now(),
    status="pending",
    updated_at=datetime.now()
  )
  fake_transactions_db[transaction_id] = transaction
  return transaction

# 检查是否已经购买过
@router.get("/check/{user_id}/{print_id}")
async def check_transaction(user_id: str, print_id: str):
  # 遍历 fake_transactions_db，检查是否有相同的 user_id 和 print_id
  for transaction_id, transaction in fake_transactions_db.items():
    if transaction.user_id == user_id and transaction.print_id == print_id:
      return {"message": "yes"}
  return {"message": "no"}
@router.get("/get/{transaction_id}")
async def get_transaction(transaction_id: str):
  # TODO: Implement get transaction by id
  return {"message": "Not implemented yet"}