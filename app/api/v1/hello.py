"""from fastapi import APIRouter, Depends
from app.core.security import verify_api_key

router = APIRouter()

@router.get("/hello")
def hello_world(user=Depends(verify_api_key)):
    return {"message": "Hola mundo seguro", "user": user}
"""

from fastapi import APIRouter, Depends
from app.core.security import require_role

router = APIRouter()

@router.get("/hello")
def hello_world(user=Depends(require_role("admin"))):
    return {"message": "Hola mundo seguro", "user": user["sub"]}

