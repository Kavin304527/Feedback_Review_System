from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FeedbackBase(BaseModel):
    user_name: str
    message: str
    rating: int

class FeedbackCreate(FeedbackBase):
    pass

class Feedback(FeedbackBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

class FeedbackUpdate(BaseModel):
    status: str
