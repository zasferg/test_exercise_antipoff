from pydantic import BaseModel
from datetime import datetime

class DataModel(BaseModel):
    id:int
    cadastral_number: str
    latitude: float
    longitude: float
    result: bool
    query_time: datetime
