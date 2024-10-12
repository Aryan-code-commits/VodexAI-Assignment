from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure

# Use the local MongoDB connection string
MONGO_DETAILS = "mongodb://localhost:27017"  # Local connection string

client = AsyncIOMotorClient(MONGO_DETAILS)

# Define your database name
DATABASE_NAME = "fastapi_db"

# Initialize the database
database = client[DATABASE_NAME]

async def initialize_database():
    try:
        # Try to connect to the MongoDB server
        await client.admin.command('ping')  # Ping the server to check if it is running
        print("Connected to MongoDB!")

        # Check if collections exist; if not, create them
        existing_collections = await database.list_collection_names()

        if "items" not in existing_collections:
            await database.create_collection("items")
            print("Collection 'items' created.")

        if "clock_in_records" not in existing_collections:
            await database.create_collection("clock_in_records")
            print("Collection 'clock_in_records' created.")

    except ConnectionFailure:
        print("Failed to connect to MongoDB. Please make sure the server is running.")

# Define the collections
items_collection = database.get_collection("items")
clock_in_collection = database.get_collection("clock_in_records")
