from fastapi import APIRouter
from app.core.jwt_manager import create_access_token

router = APIRouter()

@router.post("/login")
def login(username: str, password: str):
    # Demo: usuario fijo
    if username == "admin" and password == "1234":
        token = create_access_token({"sub": username, "role": "admin"})
        return {"access_token": token, "token_type": "bearer"}

    return {"error": "Credenciales inválidas"}

