from app.utils import calculate_fee
from app.db import entries_collection
from datetime import datetime
import uuid


async def process_entry(plate: str, parking_lot: int) -> str:
    ticket_id = str(uuid.uuid4())
    entry_time = datetime.utcnow()
    entries_collection.insert_one({
        "ticket_id": ticket_id,
        "plate": plate,
        "parking_lot": parking_lot,
        "entry_time": entry_time
    })
    return ticket_id, entry_time


async def process_exit(plate: str):
    record = await entries_collection.find_one_and_delete({"plate": plate})
    if not record:
        return None
    exit_time = datetime.utcnow()
    duration, fee = calculate_fee(record["entry_time"], exit_time)
    return {
        "plate": record["plate"],
        "parkingLot": record["parking_lot"],
        "duration": str(duration),
        "fee": round(fee, 2)
    }
