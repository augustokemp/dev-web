from fastapi import APIRouter

from app.api.api_v1.endpoints import (
    login, users, tools)


api_router = APIRouter()

api_router.include_router(
    login.router, prefix="/login", tags=["login"])
api_router.include_router(
    users.router, prefix="/users", tags=["users"])
api_router.include_router(
    tools.router, prefix="/tools", tags=["tools"])
