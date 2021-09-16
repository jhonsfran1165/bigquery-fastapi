from fastapi import FastAPI
from loguru import logger
from starlette.middleware.cors import CORSMiddleware
from easyauth.client import EasyAuthClient


from app.core.config import settings
from app.api.api_v1.api import api_router_setup


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_PREFIX}/openapi.json",
        debug=settings.DEBUG,
        version=settings.VERSION
    )

    # Set all CORS enabled origins
    if settings.BACKEND_CORS_ORIGINS:
        application.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )

    return application


app = get_application()


@app.on_event("shutdown")
async def on_shutdown():
    logger.info("Shotdown api")


@app.on_event('startup')
async def startup():
    logger.info("Starting api")

    app.auth = await EasyAuthClient.create(
        app,
        token_server=settings.TOKEN_SERVER,
        token_server_port=settings.TOKEN_SERVER_PORT,
        logger = logger,
        auth_secret = settings.SECRET_KEY
    )

    await api_router_setup(app)
