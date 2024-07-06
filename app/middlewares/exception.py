import uuid
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

# Configure the logger
# logging.basicConfig(filename='error.log', level=logging.ERROR)
# logger = logging.getLogger(__name__)


class CustomException(Exception):
    def __init__(self, message, errorCode):
        super().__init__(message)
        self.statusCode = 400
        self.errorCode = errorCode
        self.message = message
        self.errorId = str(uuid.uuid4())


class ValidationException(CustomException): ...


class AuthException(CustomException): ...


class BusinessException(CustomException): ...


class IntegrationException(CustomException): ...


class SdkException(CustomException): ...


class ExceptionHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except HTTPException as http_exception:
            return JSONResponse(
                status_code=http_exception.status_code,
                content={
                    "error": "Client Error",
                    "message": str(http_exception.detail),
                },
            )
        except Exception as e:
            # logging.error('An error occurred: %s', str(e))
            # logger.exception(msg=e.__class__.__name__, args=e.args)
            exceptionClassName = e.__class__.__name__
            if (
                exceptionClassName == "AuthException"
                or exceptionClassName == "ValidationException"
                or exceptionClassName == "BusinessException"
                or exceptionClassName == "IntegrationException"
                or exceptionClassName == "SdkException"
            ):
                return JSONResponse(
                    status_code=e.statusCode,
                    content={
                        "errorId": e.errorId,
                        "errorCode": e.errorCode,
                        "type": e.__class__.__name__,
                        "message": e.message,
                    },
                )

            return JSONResponse(
                status_code=500,
                content={
                    "type": e.__class__.__name__,
                    "message": e.args,
                },
            )
