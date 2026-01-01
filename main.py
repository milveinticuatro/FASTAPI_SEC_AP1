from fastapi import FastAPI
from app.api.v1.hello import router as hello_router

app = FastAPI(
    title="Secure FastAPI Example",
    version="1.0.0"
)

app.include_router(hello_router, prefix="/api/v1")