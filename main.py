
"""from fastapi import FastAPI
from app.api.v1.hello import router as hello_router

app = FastAPI(
    title="Secure FastAPI Example",
    version="1.0.0"
)

app.include_router(hello_router, prefix="/api/v1")
"""


from fastapi import FastAPI
from app.api.v1.hello import router as hello_router
from app.api.v1.auth import router as auth_router
from app.core.audit import AuditMiddleware

app = FastAPI(title="Secure FastAPI API")

app.add_middleware(AuditMiddleware)

app.include_router(auth_router, prefix="/api/v1/auth")
app.include_router(hello_router, prefix="/api/v1")