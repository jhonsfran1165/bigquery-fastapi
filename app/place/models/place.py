from sqlmodel import SQLModel


# Shared properties
class PlaceBase(SQLModel):
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
