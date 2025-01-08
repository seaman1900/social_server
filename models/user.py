from pydantic import BaseModel
from typing import List
from datetime import datetime

class Metadata(BaseModel):
    followers: int
    likes: int
    dislikes: int

class Profile(BaseModel):
    bio: str
    location: str
    website: str

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
    profile: Profile
    shop_list: List[dict]
    mark_list: List[dict]
    payment_methods: List[str]
    investments: List[dict]
    orders: List[dict]
    metadata: Metadata

# 注册请求模型
class RegisterRequest(BaseModel):
    username: str
    email: str
    avatar_url: str
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