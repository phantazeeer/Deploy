from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import user_router


# TODO: настроить нормально CORS
def create_app() -> FastAPI:
    app = FastAPI()
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(user_router)
    return app
