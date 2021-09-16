from fastapi import HTTPException

class PlacesNotFound(HTTPException):
    def __init__(self):
        super().__init__(
            status_code = 404,
            detail = f"There is no Places"
        )