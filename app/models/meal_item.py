from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel
from typing import Dict, Optional

from pyobjectid import PyObjectId


class MealItemModel(BaseModel):
    id: Optional[PyObjectId] = None
    meal_id: PyObjectId
    user_id: PyObjectId  # Optional for user-based queries
    food_name: str
    quantity: float  # in grams or units
    calories: float
    macros: Dict[str, float]  # Example: {"carbs": 50.0, "protein": 30.0, "fats": 20.0}
    created_at: Optional[datetime] = datetime.now(datetime.timezone.utc)

    class Config:
        json_encoders = {ObjectId: str}
        orm_mode = True
