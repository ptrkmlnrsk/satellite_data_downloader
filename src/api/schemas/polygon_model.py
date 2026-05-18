from dataclasses import dataclass

from src.domain.image_request import GEEImageRequest


Coordinate = tuple[float, float]


@dataclass
class Polygon:
    coordinates: list[list[Coordinate]]


class GEEPolygon:
    """Creates GEE Polygon object from polygon coordinates
    provided in GEEImageRequest object in specific format."""

    @classmethod
    def from_request(cls, request: GEEImageRequest):
        from ee import Geometry

        polygon_roi = Polygon(request.roi)

        return Geometry({"type": "Polygon", "coordinates": polygon_roi.coordinates})
