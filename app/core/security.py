from fastapi import Header, HTTPException, status

API_KEY = "supersecreto"  # En producción: cargar desde entorno

def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
    return "authorized-user"