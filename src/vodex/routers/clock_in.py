from fastapi import APIRouter, HTTPException
from vodex.models import ClockInRecord, UpdateClockIn
from vodex.database import clock_in_collection
from bson import ObjectId
from typing import List
from pymongo import ReturnDocument
from datetime import datetime

router = APIRouter()

# POST /clock-in
@router.post("/clock-in", response_model=ClockInRecord)
async def create_clock_in(record: ClockInRecord):
    record_data = record.dict()
    result = await clock_in_collection.insert_one(record_data)
    record_data["_id"] = str(result.inserted_id)
    return record_data

# GET /clock-in/{id}
@router.get("/clock-in/{id}", response_model=ClockInRecord)
async def get_clock_in(id: str):
    record = await clock_in_collection.find_one({"_id": ObjectId(id)})
    if not record:
        raise HTTPException(status_code=404, detail="Clock-In record not found")
    return record

# GET /clock-in/filter
@router.get("/clock-in/filter", response_model=List[ClockInRecord])
async def filter_clock_in(email: str = None, location: str = None, insert_datetime: datetime = None):
    query = {}
    if email:
        query["email"] = email
    if location:
        query["location"] = location
    if insert_datetime:
        query["insert_datetime"] = {"$gte": insert_datetime}
    
    records = await clock_in_collection.find(query).to_list(100)
    return records

# DELETE /clock-in/{id}
@router.delete("/clock-in/{id}")
async def delete_clock_in(id: str):
    result = await clock_in_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Clock-In record not found")
    return {"message": "Clock-In record deleted successfully"}

# PUT /clock-in/{id}
@router.put("/clock-in/{id}", response_model=ClockInRecord)
async def update_clock_in(id: str, record: UpdateClockIn):
    updated_record = await clock_in_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": record.dict(exclude_unset=True)},
        return_document=ReturnDocument.AFTER
    )
    if not updated_record:
        raise HTTPException(status_code=404, detail="Clock-In record not found")
    return updated_record
