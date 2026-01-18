from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True)
    message = Column(String)
    rating = Column(Integer)
    status = Column(String, default="New")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
