from bson import ObjectId
from pydantic import BaseModel
from typing import Optional

from pyobjectid import PyObjectId


class UserDetailsModel(BaseModel):
    id: Optional[PyObjectId] = None
    user_id: PyObjectId
    name: str
    age: int
    height: float  # in cm
    weight: float  # in kg
    activity_level: str  # e.g., sedentary, active
    goal_calories: int
    goal_macros: dict  # Example: {"carbs": 50, "protein": 30, "fats": 20}
    created_at: Optional[str] = None

    class Config:
        json_encoders = {ObjectId: str}
        orm_mode = True
