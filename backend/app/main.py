from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
import app.models
from app.models.base import Base

from app.routers.auth import router as auth_router
from app.routers.upload import router as upload_router
from app.routers.bills import router as bills_router
from app.routers.chat import router as chat_router

app = FastAPI(title="Hospital Billing Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(upload_router)
app.include_router(bills_router)
app.include_router(chat_router)


@app.get("/")
async def root():
    return {"status": "running"}