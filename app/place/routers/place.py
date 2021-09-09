from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.place import schemas, views
from app.user import models
from app.api import deps

router = APIRouter(
  prefix="/places"
)


@router.get("/", response_model=List[schemas.Place])
def read_users(
  db: Session = Depends(deps.get_db),
  skip: int = 0,
  limit: int = 100,
  current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
  """
  Retrieve places from bigquery.
  """
  places = views.get_places()
  return places
