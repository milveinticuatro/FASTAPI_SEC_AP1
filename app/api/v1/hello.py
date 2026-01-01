from fastapi import APIRouter, Depends
from app.core.security import verify_api_key

router = APIRouter()

@router.get("/hello")
def hello_world(user=Depends(verify_api_key)):
    return {"message": "Hola mundo seguro", "user": user}