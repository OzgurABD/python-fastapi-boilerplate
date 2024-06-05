import logging
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

# Configure the logger
# logging.basicConfig(filename='error.log', level=logging.ERROR)
logger = logging.getLogger(__name__)


class ValidationException(Exception):
    pass


class BusinessException(Exception):
    pass


class IntegrationException(Exception):
    pass


class SdkException(Exception):
    pass


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
            logger.exception(msg=e.__class__.__name__, args=e.args)
            return JSONResponse(
                status_code=500,
                content={
                    "error": "Internal Server Error",
                    "message": "An unexpected error occurred.",
                },
            )
