import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("DB_URI"))


def get_db():
    return client.get_database("arogyadb")
