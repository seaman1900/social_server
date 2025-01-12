from fastapi import APIRouter
from fastapi import HTTPException
from datetime import datetime
import hashlib

from models.user import User, RegisterRequest, LoginRequest, Metadata
from wrench.misc import generate_user_id
from fake_dbs.fake_users import fake_users_db
# logger
from loguru import logger

router = APIRouter(prefix="/user", tags=["users"])


# 密码哈希函数
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# 注册API
@router.post("/register")
async def register(user: RegisterRequest):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_password = hash_password(user.password)
    user_id = generate_user_id(user.username)
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
        role=[],
        avatar_url=user.avatar_url,
        mark_list=[],
        wish_list=[],
        metadata=Metadata(**meta_data)
    )
    
    fake_users_db[user_id] = new_user
    logger.info(f"User {user.username} registered at {new_user.registration_date}")
    return {"message": "User registered successfully", "user_info": new_user}

# 登录API
@router.post("/login")
async def login(login_data: LoginRequest):
    user = fake_users_db.get(login_data.username)
    if not user or user.password_hash != hash_password(login_data.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    user.last_login = datetime.now()
    logger.info(f"User {user.username} logged in at {user.last_login}")
    return {"message": "Login successful", "user_info": user}

# 更新用户信息
@router.put("/{user_id}")
async def update_user(user_id: str, user_data: User):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")

    user = fake_users_db[user_id]
    if user_data.username:
        user.username = user_data.username
    if user_data.email:
        user.email = user_data.email
    return {"message": "User updated successfully", "user_info": user}

# 获取用户基本信息
@router.get("/{user_id}")
async def get_user(user_id: str):
    user = fake_users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user