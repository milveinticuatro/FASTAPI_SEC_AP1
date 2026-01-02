# V1 Despligue inicial a GitHub 
"""from fastapi import Header, HTTPException, status

API_KEY = "supersecreto"  # En producción: cargar desde entorno

def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
    return "authorized-user"
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.core.jwt_manager import SECRET_KEY, ALGORITHM
from app.core.roles import check_role

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )

def require_role(role: str):
    def wrapper(user=Depends(get_current_user)):
        check_role(user, role)
        return user
    return wrapper