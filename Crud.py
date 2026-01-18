from sqlalchemy.orm import Session
from models import Feedback
from schemas import FeedbackCreate, FeedbackUpdate

def create_feedback(db: Session, feedback: FeedbackCreate):
    db_feedback = Feedback(**feedback.dict())
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

def get_feedbacks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Feedback).offset(skip).limit(limit).all()

def update_feedback_status(db: Session, feedback_id: int, status: str):
    feedback = db.query(Feedback).filter(Feedback.id == feedback_id).first()
    if feedback:
        feedback.status = status
        db.commit()
        db.refresh(feedback)
    return feedback
