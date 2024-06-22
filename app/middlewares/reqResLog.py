import os
import time
import uuid
import json
import logging
import logging.config
from typing import Callable, Optional
from fastapi import FastAPI, Request, Response
from fastapi.concurrency import iterate_in_threadpool
from starlette.middleware.base import BaseHTTPMiddleware


class RouterLoggingMiddleware(BaseHTTPMiddleware):

    def __init__(
        self, app: FastAPI, *, logger: Optional[logging.Logger] = None
    ) -> None:
        self._logger = logger if logger else logging.getLogger(__name__)
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: Callable) -> Response:

        requestBody = None
        body = await request.body()
        if body:
            requestBody = json.loads(body.decode("utf-8"))

        startTime = time.time()
        response: Response = await call_next(request)
        processTime = (time.time() - startTime) * 1000
        processTimeFormated = "{0:.2f}".format(processTime)
        response.headers["X-Process-Time"] = str(processTime)
        response.headers["X-Process-Time-Formated"] = str(processTimeFormated)

        responseContentStream = [section async for section in response.body_iterator]
        response.body_iterator = iterate_in_threadpool(iter(responseContentStream))
        responseBody = responseContentStream[0].decode()

        await self.logDataFormatter(
            request, response, startTime, processTime, requestBody, responseBody
        )
        return response

    async def logDataFormatter(
        self,
        request: Request,
        response: Response,
        startTime: float,
        processTime: float,
        requestBody: any,
        responseBody: any,
    ) -> None:
        logDataDict = dict()
        logDataDict["transactionId"] = str(uuid.uuid4())
        logDataDict["ip"] = request.client.host
        logDataDict["startTime"] = startTime
        logDataDict["processTime"] = processTime  # f"{processTime:0.4f}s"
        logDataDict["method"] = request.method
        logDataDict["requestUrl"] = request.url.hostname
        logDataDict["path"] = (
            f"{request.url.path}?{request.query_params}"
            if request.query_params
            else request.url.path
        )
        logDataDict["statusCode"] = response.status_code
        logDataDict["requestBody"] = requestBody
        logDataDict["responseBody"] = responseBody
        logDataDict["env"] = os.environ.get("ENV")
        logDataDict["region"] = os.environ.get("REGION")
        logDataDict["name"] = os.environ.get("NAME")
        self._logger.info(logDataDict)
