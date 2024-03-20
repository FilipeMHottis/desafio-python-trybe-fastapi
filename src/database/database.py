from pymongo import MongoClient
from app.settings import get_settings

settings = get_settings()

db_client = MongoClient(settings.mongo_url)
db = db_client[settings.db_name]
