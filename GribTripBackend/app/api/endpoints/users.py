from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi.params import Header
from fastapi.security import OAuth2PasswordRequestForm

from app.api.schemas import UserCreateParameters
from app.api.schemas import UserCreateResponse
from app.api.schemas import UserGetMeResponse
from app.api.schemas import UserLogInParameters
from app.api.schemas import UserLogInResponse
from app.services import UserService
from app.utils import get_jwt_payload
from app.utils import IUnitOfWork
from app.utils import UnitOfWork

router = APIRouter(tags=["work with users"], prefix="/auth")


async def get_user_service(uow: IUnitOfWork = Depends(UnitOfWork)) -> UserService:  # noqa
    return UserService(uow)


@router.post("/register")
async def register(
    user: UserCreateParameters, user_service: UserService = Depends(get_user_service), # noqa
) -> UserCreateResponse:  # noqa
    """Регистрация пользователя"""
    access_token, refresh_token = await user_service.register(
        username=user.name,
        password=user.password,
        email=user.email,
        role=user.role,
    )
    response = UserCreateResponse(refresh_token=refresh_token, access_token=access_token, token_type="bearer")
    return response


@router.post("/login")
async def login(
    user: UserLogInParameters, user_service: UserService = Depends(get_user_service), # noqa
) -> UserLogInResponse:  # noqa
    access_token, refresh_token = await user_service.login(email=user.email, password=user.password)
    response = UserLogInResponse(access_token=access_token, refresh_token=refresh_token, token_type="bearer")
    return response


@router.post("/docs/login")
async def docs_login(
    user: Annotated[OAuth2PasswordRequestForm, Depends()], user_service: UserService = Depends(get_user_service) # noqa
) -> UserLogInResponse:  # noqa
    access_token, refresh_token = await user_service.login(email=user.username, password=user.password)
    response = UserLogInResponse(access_token=access_token, refresh_token=refresh_token, token_type="bearer")
    return response


@router.get("/me")
async def me(
    jwt_access: Annotated[str, Depends(get_jwt_payload)], user_service: UserService = Depends(get_user_service), # noqa
) -> UserGetMeResponse:
    resp = await user_service.get_me(token=jwt_access)
    return resp


@router.get("/refresh")
async def refresh(
    jwt_refresh: Annotated[str, Header()], user_service: UserService = Depends(get_user_service), # noqa
) -> UserLogInResponse:
    resp = await user_service.refresh(get_jwt_payload(jwt_refresh))
    return UserLogInResponse(access_token=resp, refresh_token=jwt_refresh, token_type="bearer")
