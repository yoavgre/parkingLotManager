from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")

if not MONGO_URL:
    raise ValueError("MONGO_URL not found in environment variables")

client = AsyncIOMotorClient(MONGO_URL)
db = client["parking_db"]
entries_collection: Collection = db["entries"]
