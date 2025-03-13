# Import Libraries
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from app.server.config.config import Settings

settings = Settings()

# Database Configuration
client = AsyncIOMotorClient(settings.MONGODB_URL, serverSelectionTimeoutMS=5000)
client.get_io_loop = asyncio.get_event_loop

try:
 db_connection = client.server_info()
 print("Connection to Mongo DB Server Successfull")
except Exception as e:
 print("Connection Unsuccessfull")
 print(str(e))

database = client.frogsss_api
frogs = database.get_collection("frogss_collection")