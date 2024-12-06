from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel
from typing import Dict, Optional, List

from pyobjectid import PyObjectId


class MealModel(BaseModel):
    id: Optional[PyObjectId] = None
    user_id: PyObjectId
    meal_time: datetime
    meal_name: str  # e.g., breakfast, lunch, dinner
    total_calories: float
    total_macros: Dict[
        str, float
    ]  # Example: {"carbs": 150.0, "protein": 90.0, "fats": 60.0}
    meal_item_ids: List[PyObjectId]  # List of references to MealItems
    created_at: Optional[datetime] = datetime.now(datetime.timezone.utc)

    class Config:
        json_encoders = {ObjectId: str}
        orm_mode = True
