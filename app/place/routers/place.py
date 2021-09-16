from typing import Any, List

from app.place.exceptions import PlacesNotFound
from app.place.models.place import Place
from app.place.views import place_view

async def setup(router):
  @router.get(
    "/", response_model=List[Place],
    groups=['users', 'admins'], # OR
    roles=['basic'],  # OR
    actions=['users:create']
  )
  async def list_places(
    skip: int = 0,
    limit: int = 100
  ) -> Any:
    """
    Retrieve places from bigquery.
    """
    places = await place_view.get_places(limit, skip)

    if not places:
      raise PlacesNotFound


    return places
