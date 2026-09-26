from fastapi import FastAPI

from app.database import Base, engine
import app.models
from app.routers import student, subject , user




app = FastAPI()

app.include_router(student.router)
app.include_router(subject.router)
app.include_router(user.router)
