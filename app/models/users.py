from bson import ObjectId
from pydantic import BaseModel, EmailStr
from typing import Optional

from pyobjectid import PyObjectId


class UserModel(BaseModel):
    id: Optional[PyObjectId] = None
    email: EmailStr
    password_hash: str

    class Config:
        json_encoders = {ObjectId: str}
        orm_mode = True
