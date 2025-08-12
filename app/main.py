from fastapi import FastAPI
from app.controller import face

app = FastAPI(title="Fayda Face Recognition API")

app.include_router(face.router, prefix="/api/face", tags=["Face Recognition"])
