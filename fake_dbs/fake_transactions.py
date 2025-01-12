from datetime import datetime
from typing import Dict

from models.transaction import Transaction

# 假交易数据
fake_transactions_db: Dict[str, Transaction] = {
    "a1b2c3d4-e89b-12d3-a456-426614174000": Transaction(
        transaction_id="a1b2c3d4-e89b-12d3-a456-426614174000",
        trans_type="recharge",
        user_id="user123",
        print_id="",
        amount=10000,  # 单位为分（假设金额以分为单位）
        created_at=datetime(2023, 10, 1, 12, 34, 56),
        status="completed",
        updated_at=datetime(2023, 10, 1, 12, 34, 56)
    ),
    "b2c3d4e5-f89b-12d3-a456-426614174001": Transaction(
        transaction_id="b2c3d4e5-f89b-12d3-a456-426614174001",
        trans_type="purchase",
        user_id="user123",
        print_id="123e4567-e89b-12d3-a456-426614174000",
        amount=5000,
        created_at=datetime(2023, 10, 2, 14, 20, 10),
        status="completed",
        updated_at=datetime(2023, 10, 2, 14, 20, 10)
    ),
    "c3d4e5f6-g89b-12d3-a456-426614174002": Transaction(
        transaction_id="c3d4e5f6-g89b-12d3-a456-426614174002",
        trans_type="recharge",
        user_id="user456",
        print_id="",
        amount=20000,
        created_at=datetime(2023, 10, 3, 9, 15, 30),
        status="completed",
        updated_at=datetime(2023, 10, 3, 9, 15, 30)
    ),
    "d4e5f6g7-h89b-12d3-a456-426614174003": Transaction(
        transaction_id="d4e5f6g7-h89b-12d3-a456-426614174003",
        trans_type="purchase",
        user_id="user456",
        print_id="223e4567-e89b-12d3-a456-426614174001",
        amount=7500,
        created_at=datetime(2023, 10, 4, 16, 45, 22),
        status="failed",
        updated_at=datetime(2023, 10, 4, 16, 45, 22)
    ),
    "e5f6g7h8-i89b-12d3-a456-426614174004": Transaction(
        transaction_id="e5f6g7h8-i89b-12d3-a456-426614174004",
        trans_type="recharge",
        user_id="user789",
        print_id="",
        amount=15000,
        created_at=datetime(2023, 10, 5, 11, 10, 45),
        status="completed",
        updated_at=datetime(2023, 10, 5, 11, 10, 45)
    ),
    "f6g7h8i9-j89b-12d3-a456-426614174005": Transaction(
        transaction_id="f6g7h8i9-j89b-12d3-a456-426614174005",
        trans_type="purchase",
        user_id="user789",
        print_id="323e4567-e89b-12d3-a456-426614174002",
        amount=3000,
        created_at=datetime(2023, 10, 6, 18, 30, 15),
        status="completed",
        updated_at=datetime(2023, 10, 6, 18, 30, 15)
    ),
    "g7h8i9j0-k89b-12d3-a456-426614174006": Transaction(
        transaction_id="g7h8i9j0-k89b-12d3-a456-426614174006",
        trans_type="recharge",
        user_id="user101",
        print_id="",
        amount=30000,
        created_at=datetime(2023, 10, 7, 8, 5, 50),
        status="completed",
        updated_at=datetime(2023, 10, 7, 8, 5, 50)
    ),
    "h8i9j0k1-l89b-12d3-a456-426614174007": Transaction(
        transaction_id="h8i9j0k1-l89b-12d3-a456-426614174007",
        trans_type="purchase",
        user_id="user101",
        print_id="423e4567-e89b-12d3-a456-426614174003",
        amount=10000,
        created_at=datetime(2023, 10, 8, 20, 25, 40),
        status="completed",
        updated_at=datetime(2023, 10, 8, 20, 25, 40)
    ),
    "i9j0k1l2-m89b-12d3-a456-426614174008": Transaction(
        transaction_id="i9j0k1l2-m89b-12d3-a456-426614174008",
        trans_type="recharge",
        user_id="user202",
        print_id="",
        amount=5000,
        created_at=datetime(2023, 10, 9, 13, 55, 33),
        status="failed",
        updated_at=datetime(2023, 10, 9, 13, 55, 33)
    ),
    "j0k1l2m3-n89b-12d3-a456-426614174009": Transaction(
        transaction_id="j0k1l2m3-n89b-12d3-a456-426614174009",
        trans_type="purchase",
        user_id="user202",
        print_id="523e4567-e89b-12d3-a456-426614174004",
        amount=2500,
        created_at=datetime(2023, 10, 10, 17, 40, 12),
        status="completed",
        updated_at=datetime(2023, 10, 10, 17, 40, 12)
    )
}