import sentry_sdk
from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware
from api.main import apiRouter
from core.config import settings
from middlewares.exception import ExceptionHandlerMiddleware
from middlewares.reqResLog import RouterLoggingMiddleware
from logs.oneLog import oneLogger


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


# initialize logger
if settings.SENTRY_DSN and settings.ENVIRONMENT != "local":
    sentry_sdk.init(dsn=str(settings.SENTRY_DSN), enable_tracing=True)

# Set FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url=f"{settings.API_V1_STR}/docs",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.add_middleware(ExceptionHandlerMiddleware)
app.add_middleware(RouterLoggingMiddleware)


# Set Router
# fmt: off
app.include_router(apiRouter, prefix=settings.API_V1_STR, include_in_schema=False)


# initial tables
# createDatabase()

oneLogger.info("App Has Started")
