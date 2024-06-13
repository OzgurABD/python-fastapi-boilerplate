import time
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
        response: Response = await call_next(request)
        processTime = time.time() - startTime
        response.headers["X-Process-Time"] = str(processTime)
        self.logDataFormatter(request, response, startTime, processTime)
        return response

    async def logDataFormatter(
        self, request: Request, response: Response, startTime: float, processTime: float
    ) -> None:
        logDataDict = dict()
        logDataDict["ip"] = request.client.host
        logDataDict["startTime"] = startTime
        logDataDict["processTime"] = processTime  # f"{processTime:0.4f}s"
        logDataDict["request"] = await self.reqLogFormat(request)
        logDataDict["response"] = await self.resLogFormat(response)
        self._logger.info(logDataDict)

    async def reqLogFormat(self, request: Request) -> str:
        _path = (
            f"{request.url.path}?{request.query_params}"
            if request.query_params
            else request.url.path
        )

        data = {
            "path": _path,
            "method": request.method,
        }

        try:
            data["body"] = await request.json()
        except:
            data["body"] = None

        return data

    async def resLogFormat(self, response: Response) -> str:

        data = {
            "statusCode": response.status_code,
        }

        print(response)

        return ""
