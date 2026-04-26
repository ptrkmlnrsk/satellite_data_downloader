from dataclasses import dataclass
from typing import List, Literal
from pydantic import BaseModel


Coordinate = tuple[float, float]


@dataclass
class PolygonModel(BaseModel):
    coordinates: List[List[Coordinate]]
    type: Literal["Polygon"] = "Polygon"
