from fastapi import FastAPI, HTTPException, File, UploadFile

from app.parking import process_entry, process_exit

app = FastAPI()


@app.post("/entry")
async def entry(plate: str, parkingLot: int):
    ticket_id, entry_time = await process_entry(plate, parkingLot)
    return {"ticketId": ticket_id, "entryTime": entry_time}


@app.post("/exit")
async def exit(plate: str):
    result = await process_exit(plate)
    if not result:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return result
