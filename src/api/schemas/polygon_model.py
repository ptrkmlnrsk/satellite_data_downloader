# from typing import Literal
from dataclasses import dataclass

from pydantic import BaseModel

# from src.domain.polygon import Polygon
from src.domain.image_request import GEEImageRequest

Coordinate = tuple[float, float]


@dataclass
class Polygon:
    coordinates: list[list[Coordinate]]


class GEEPolygon(BaseModel):
    @classmethod
    def from_request(cls, request: GEEImageRequest):
        from ee import Geometry

        polygon_roi = Polygon(request.roi)

        return Geometry({"type": "Polygon", "coordinates": polygon_roi.coordinates})


# class PolygonModel(BaseModel):
#     """Pydantic model for polygon"""
#
#     coordinates: list[list[Coordinate]]
#     #type: Literal["Polygon"] = "Polygon" # w literalu Polygon to musi byc Polygon
#
#     @field_validator("coordinates")
#     def validate_coordinates(cls, coordinates):
#         if len(coordinates) < 5:
#             raise ValueError("Polygon must have at least 5 vertices")
#         return coordinates
