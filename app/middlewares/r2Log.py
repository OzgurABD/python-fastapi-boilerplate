import time
import json
import logging
import logging.config
from typing import Callable, Optional
from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


class RouterLoggingMiddleware(BaseHTTPMiddleware):

    def __init__(
        self, app: FastAPI, *, logger: Optional[logging.Logger] = None
    ) -> None:
        self._logger = logger if logger else logging.getLogger(__name__)
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        startTime = time.time()
        response = await call_next(request)
        processTime = time.time() - startTime
        response.headers["X-Process-Time"] = str(processTime)
        return response
