from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas
import crud
from database import get_db

router = APIRouter(prefix="/feedbacks", tags=["admin"])

@router.put("/{feedback_id}/status")
def update_feedback_status(
    feedback_id: int, 
    status: schemas.FeedbackUpdate, 
    db: Session = Depends(get_db)
):
    """Update feedback status (Admin only)"""
    feedback = crud.update_feedback_status(db, feedback_id, status.status)
    if feedback is None:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return feedback
