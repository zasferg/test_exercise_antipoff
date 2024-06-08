from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict

class DataModel(BaseModel):
    id:int
    cadastral_number: str
    latitude: float
    longitude: float
    result: bool
    query_time: datetime

    class Config:
        from_attributes = True


class QueryHistory(BaseModel):
    cadastral_number: str
    query_date: datetime
    query_data: Optional[str]
    response_status: Optional[bool]
    response_data: Optional[str]

    class Config:
        from_attributes = True
