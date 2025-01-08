from pydantic import BaseModel
from typing import List
from datetime import datetime

# 用户模型
class User(BaseModel):
    user_id: str
    username: str
    email: str
    password_hash: str
    registration_date: datetime
    last_login: datetime
    is_admin: bool
    roles: List[str]
    permissions: List[str]
    avatar_url: str
    balance: float
    profile: dict
    shop_list: List[dict]
    mark_list: List[dict]
    payment_methods: List[str]
    investments: List[dict]
    orders: List[dict]
    metadata: dict

# 注册请求模型
class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

# 登录请求模型
class LoginRequest(BaseModel):
    username: str
    password: str

# 购买请求模型
class PurchaseRequest(BaseModel):
    user_id: str
    content_id: str
    amount: float

# 充值请求模型
class RechargeRequest(BaseModel):
    user_id: str
    amount: float
    payment_method: str