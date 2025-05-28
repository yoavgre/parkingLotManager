from pydantic import BaseModel
from datetime import datetime


class EntryRecord(BaseModel):
    ticket_id: str
    plate: str
    parking_lot: int
    entry_time: datetime
