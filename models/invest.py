from pydantic import BaseModel
from datetime import datetime

class Investment(BaseModel):
    invest_id: str
    user_id: str
    print_id: str
    invest_type: str  # "Content Promotion", "Content Maintenance", "Ad Placement", "Angel Investment"
    invest_amount: float
    invest_time: datetime
    profit: float  # 预期或实际收益