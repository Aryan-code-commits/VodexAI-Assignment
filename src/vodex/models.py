from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import pytz

# Function to get the current datetime in IST
def current_ist_time():
    return datetime.now(pytz.timezone('Asia/Kolkata'))

# Model for Items
class Item(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: datetime
    insert_date: Optional[datetime] = Field(default_factory=current_ist_time)

# Model for User Clock-In Records
class ClockInRecord(BaseModel):
    email: str
    location: str
    insert_datetime: Optional[datetime] = Field(default_factory=current_ist_time)

# Model for updating records (optional fields)
class UpdateItem(BaseModel):
    name: Optional[str]
    email: Optional[str]
    item_name: Optional[str]
    quantity: Optional[int]
    expiry_date: Optional[datetime]

class UpdateClockIn(BaseModel):
    email: Optional[str]
    location: Optional[str]
