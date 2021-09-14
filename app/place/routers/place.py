from typing import Any, List

from fastapi import APIRouter, Depends

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi_permissions import Authenticated, Allow


from app.place.models.place import Place
from app.place.views import place
from app.user.models.user import User
from app.api import deps

router = APIRouter(
  prefix="/places"
)

acl_places = [
  (Allow, "admin", "*"),
  (Allow, "owner", "*"),
  (Allow, Authenticated, "view")
]

# TODO: https://github.com/holgi/fastapi-permissions/issues/3
@router.get("/", response_model=List[Place])
async def read_users(
  db: AsyncSession = Depends(deps.get_db),
  skip: int = 0,
  limit: int = 100,
  acls: list = deps.Permission("view", acl_places)
) -> Any:
  """
  Retrieve places from bigquery.
  """
  places = await place.get_places(limit=limit, skip=skip)
  return places
