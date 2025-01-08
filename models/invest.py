from pydantic import BaseModel
from datetime import datetime

class Investment(BaseModel):
    invest_id: str
    user_id: str
    content_id: str
    invest_amount: float
    invest_time: datetime
    invest_type: str  # "Content Promotion", "Content Maintenance", "Ad Placement", "Angel Investment"
    profit: float  # 预期或实际收益