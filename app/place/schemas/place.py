from pydantic import BaseModel, Json


# Shared properties
class PlaceBase(BaseModel):
    id: int
    place_id: str
    place_type: str
    name: str
    full_name: str
    country_code: str
    country: str
    bounding_box: str


# Additional properties to return via API
class Place(PlaceBase):
    pass
