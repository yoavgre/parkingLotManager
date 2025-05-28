from fastapi import FastAPI, HTTPException, File, UploadFile

from app.parking import process_entry, process_exit
from app.plate_reader import extract_plate_from_image

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


@app.post("/entry-image")
async def entry_image(parking_lot: int, file: UploadFile = File(...)):
    contents = await file.read()
    plate = extract_plate_from_image(contents)
    ticket_id, entry_time = await process_entry(plate, parking_lot)
    return {"ticketId": ticket_id, "plate": plate, "entryTime": entry_time}


@app.post("/exit-image")
async def exit_image(file: UploadFile = File(...)):
    contents = await file.read()
    plate = extract_plate_from_image(contents)
    result = await process_exit(plate)
    if not result:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return result
