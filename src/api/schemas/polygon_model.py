from typing import Literal
from pydantic import BaseModel, field_validator


Coordinate = tuple[float, float]


class PolygonModel(BaseModel):
    """Pydantic model for polygon"""

    coordinates: list[list[Coordinate]]
    type: Literal["Polygon"] = "Polygon"

    @field_validator("coordinates")
    def validate_coordinates(cls, coordinates):
        if len(coordinates) < 5:
            raise ValueError("Polygon must have at least 5 vertices")
        return coordinates
