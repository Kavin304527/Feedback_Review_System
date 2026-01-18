from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine
from routers import feedback, admin


models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Feedback System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(feedback.router)
app.include_router(admin.router)

