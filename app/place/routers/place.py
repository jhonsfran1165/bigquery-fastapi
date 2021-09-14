from typing import Any, List

from fastapi import APIRouter, Depends

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.place.models.place import Place
from app.place.views import place
from app.user.models.user import User
from app.api import deps

router = APIRouter(
  prefix="/places"
)

@router.get("/users", response_model=List[User])
async def get_songs(db: AsyncSession = Depends(deps.get_db)):
    result = await db.exec(select(User))
    songs = result.all()
    return songs


@router.get("/", response_model=List[Place])
async def read_users(
  db: AsyncSession = Depends(deps.get_db),
  skip: int = 0,
  limit: int = 100,
) -> Any:
  """
  Retrieve places from bigquery.
  """
  places = await place.get_places(limit=limit, skip=skip)
  return places
