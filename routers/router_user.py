from fastapi import APIRouter
from fastapi import HTTPException
from datetime import datetime
import hashlib

from models.user import User, RegisterRequest, LoginRequest, PurchaseRequest, RechargeRequest, Profile, Metadata
from tools.misc import generate_user_id


router = APIRouter(prefix="/user", tags=["users"])

# 模拟数据库
fake_db = {
    "test_user_id_1": User(
        user_id="test_user_id_1",
        username="test_user_1",
        email="test_user@example.com",
        password_hash="a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3", # 123的hash
        registration_date=datetime.now(),
        last_login=datetime.now(),
        is_admin=False,
        roles=["user"],
        permissions=["user"],
        avatar_url="https://cdn.img2ipfs.com/ipfs/QmQKq7c7jmmZpPjof7gmUQhjBoScYmD3KUW73Wj7eJtcEY?filename=myxj.jpg",
        balance=100.0,
        profile=Profile(bio="This is a test user", location="Test City", website="https://github.com/seaman1900"),
        shop_list=[],
        mark_list=[],
        payment_methods=[],
        investments=[],
        orders=[],
        metadata=Metadata(followers=0, likes=0, dislikes=0)
    ),
    "test_user_id_2": User(
        user_id="test_user_id_2",
        username="test_user_2",
        email="test_user@example.com",
        password_hash="a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3",
        registration_date=datetime.now(),
        last_login=datetime.now(),
        is_admin=False,
        roles=["user"],
        permissions=["admin"],
        avatar_url="https://cdn.img2ipfs.com/ipfs/QmQKq7c7jmmZpPjof7gmUQhjBoScYmD3KUW73Wj7eJtcEY?filename=myxj.jpg",
        balance=1000.0,
        profile=Profile(bio="This is a test user", location="Test City", website="https://github.com/seaman1900"),
        shop_list=[],
        mark_list=[],
        payment_methods=[],
        investments=[],
        orders=[],
        metadata=Metadata(followers=0, likes=0, dislikes=0)
    )
}

# 密码哈希函数
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# 注册API
@router.post("/register")
async def register(user: RegisterRequest):
    if user.username in fake_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_password = hash_password(user.password)
    user_id = generate_user_id(user.username)
    profile = {
        'bio': '',
        'location': '',
        'website': '',
    }
    meta_data = {
        'followers': 0,
        'likes': 0,
        'dislikes': 0
    }
    new_user = User(
        user_id=user_id,
        username=user.username,
        email=user.email,
        password_hash=hashed_password,
        registration_date=datetime.now(),
        last_login=datetime.now(),
        is_admin=False,
        roles=[],
        permissions=[],
        avatar_url=user.avatar_url,
        balance=0.0,
        profile=Profile(**profile),
        shop_list=[],
        mark_list=[],
        payment_methods=[],
        investments=[],
        orders=[],
        metadata=Metadata(**meta_data)
    )
    
    fake_db[user_id] = new_user
    return {"message": "User registered successfully", "user_info": new_user}

# 登录API
@router.post("/login")
async def login(login_data: LoginRequest):
    user = fake_db.get(login_data.username)
    if not user or user.password_hash != hash_password(login_data.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    user.last_login = datetime.now()
    return {"message": "Login successful", "user_info": user}

# 购买付费内容API
@router.post("/purchase")
async def purchase(purchase_data: PurchaseRequest):
    user = fake_db.get(purchase_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.balance < purchase_data.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    
    user.balance -= purchase_data.amount
    user.shop_list.append({"content_id": purchase_data.content_id, "added_time": datetime.now()})
    
    return {"message": "Purchase successful", "remaining_balance": user.balance}

# 充值API
@router.post("/recharge")
async def recharge(recharge_data: RechargeRequest):
    user = fake_db.get(recharge_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.balance += recharge_data.amount
    user.orders.append({
        "order_id": hashlib.sha256(str(datetime.now()).encode()).hexdigest(),
        "order_amount": recharge_data.amount,
        "order_time": datetime.now(),
        "order_status": "paid",
        "payment_method": recharge_data.payment_method
    })
    
    return {"message": "Recharge successful", "new_balance": user.balance}

