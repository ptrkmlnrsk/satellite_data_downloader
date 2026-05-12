from dataclasses import dataclass
from src.api.schemas.polygon_model import Coordinate


@dataclass
class Polygon:
    coordinates: list[list[Coordinate]]
