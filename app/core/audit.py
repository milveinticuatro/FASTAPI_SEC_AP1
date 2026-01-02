from starlette.middleware.base import BaseHTTPMiddleware
import time

class AuditMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = round(time.time() - start, 4)

        print({
            "path": request.url.path,
            "method": request.method,
            "duration": duration,
            "status": response.status_code
        })

        return response

