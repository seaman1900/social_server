import hashlib
from datetime import datetime

def generate_user_id(username: str) -> str:
    # 基于用户名和时间戳生成用户ID
    unique_string = f"{username}_{datetime.now().isoformat()}"
    return hashlib.sha256(unique_string.encode()).hexdigest()[:8]  # 取前8位作为ID

def generate_content_id(title: str, author_id: str) -> str:
    # 基于标题、作者ID和时间戳生成哈希值
    unique_string = f"{title}_{author_id}_{datetime.now().isoformat()}"
    return hashlib.sha256(unique_string.encode()).hexdigest()[:8]  # 取前8位作为ID

def generate_investment_id(user_id: str, content_id: str, invest_time: datetime, invest_amount: float) -> str:
    # 将用户ID、内容ID、投资时间和投资金额组合成一个唯一字符串
    unique_string = f"{user_id}_{content_id}_{invest_time.isoformat()}_{invest_amount}"
    # 使用SHA-256生成哈希值，并取前8位作为ID
    return hashlib.sha256(unique_string.encode()).hexdigest()[:8]