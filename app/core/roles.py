from fastapi import HTTPException, status

def check_role(user: dict, required_role: str):
    user_role = user.get("role")
    if user_role != required_role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Se requiere rol '{required_role}'"
        )

