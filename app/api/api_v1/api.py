from fastapi import APIRouter
from app.user.routers import user, auth
from app.place.routers import place

api_router = APIRouter()
api_router.include_router(auth.router, tags=["auth"])
api_router.include_router(user.router, tags=["users"])
api_router.include_router(place.router, tags=["places"])
