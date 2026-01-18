from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
import schemas
import crud
from database import get_db

router = APIRouter(prefix="/feedbacks", tags=["feedback"])

@router.post("/", response_model=schemas.Feedback)
def create_feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    """Create new feedback"""
    return crud.create_feedback(db=db, feedback=feedback)

@router.get("/", response_model=List[schemas.Feedback])
def read_feedbacks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all feedbacks"""
    feedbacks = crud.get_feedbacks(db, skip=skip, limit=limit)
    return feedbacks
