from datetime import datetime
from typing import Dict
from models.balance import Balance

# 假余额数据
fake_balances: Dict[str, Balance] = {
    "user123": Balance(
        user_id="user123",
        balance=1000.50,
        frozen_amount=200.00,
        last_update_time=datetime(2023, 10, 1, 12, 34, 56)
    ),
    "user456": Balance(
        user_id="user456",
        balance=500.75,
        frozen_amount=100.25,
        last_update_time=datetime(2023, 10, 2, 14, 20, 10)
    ),
    "user789": Balance(
        user_id="user789",
        balance=1500.00,
        frozen_amount=300.50,
        last_update_time=datetime(2023, 10, 3, 9, 15, 30)
    ),
    "user101": Balance(
        user_id="user101",
        balance=2000.25,
        frozen_amount=400.75,
        last_update_time=datetime(2023, 10, 4, 16, 45, 22)
    ),
    "user202": Balance(
        user_id="user202",
        balance=750.00,
        frozen_amount=150.00,
        last_update_time=datetime(2023, 10, 5, 11, 10, 45)
    )
}