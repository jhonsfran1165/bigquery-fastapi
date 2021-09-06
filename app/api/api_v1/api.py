from fastapi import APIRouter
from app.user.router import user, login
from app.place.router import place

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(user.router, tags=["users"])
api_router.include_router(place.router, tags=["places"])
