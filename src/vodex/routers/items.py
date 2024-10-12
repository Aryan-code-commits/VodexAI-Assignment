from fastapi import APIRouter, HTTPException
from vodex.models import Item, UpdateItem
from vodex.database import items_collection
from bson import ObjectId
from typing import List
from pymongo import ReturnDocument
from datetime import datetime

router = APIRouter()

# POST /items
@router.post("/items", response_model=Item)
async def create_item(item: Item):
    item_data = item.dict()
    result = await items_collection.insert_one(item_data)
    item_data["_id"] = str(result.inserted_id)
    return item_data

# GET /items/{id}
@router.get("/items/{id}", response_model=Item)
async def get_item(id: str):
    item = await items_collection.find_one({"_id": ObjectId(id)})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# GET /items/filter
@router.get("/items/filter", response_model=List[Item])
async def filter_items(email: str = None, expiry_date: datetime = None, insert_date: datetime = None, quantity: int = None):
    query = {}
    if email:
        query["email"] = email
    if expiry_date:
        query["expiry_date"] = {"$gte": expiry_date}
    if insert_date:
        query["insert_date"] = {"$gte": insert_date}
    if quantity:
        query["quantity"] = {"$gte": quantity}
    
    items = await items_collection.find(query).to_list(100)
    return items

# Aggregation: Count items by email
@router.get("/items/aggregate/count-by-email")
async def count_items_by_email():
    pipeline = [
        {"$group": {"_id": "$email", "count": {"$sum": 1}}}
    ]
    result = await items_collection.aggregate(pipeline).to_list(100)
    return result

# DELETE /items/{id}
@router.delete("/items/{id}")
async def delete_item(id: str):
    result = await items_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}

# PUT /items/{id}
@router.put("/items/{id}", response_model=Item)
async def update_item(id: str, item: UpdateItem):
    updated_item = await items_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": item.dict(exclude_unset=True)},
        return_document=ReturnDocument.AFTER
    )
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item
