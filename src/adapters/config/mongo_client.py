from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def get_mongo_client():
    return MongoClient(getenv("MONGODB_URI"))

def get_db():
    client = get_mongo_client()
    return client[getenv("MONGODB_DB")]
