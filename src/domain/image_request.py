# from src.domain.polygon import Polygon

# from dataclasses import dataclass
from pydantic import BaseModel
from src.domain.enums.sentinel2_bands import Sentinel2Band


class GEEImageRequest(BaseModel):
    """An object to represent an Earth Engine image request.
    Roi parameter has to be Polygon object with at least 3 vertices."""

    image_id: str
    bands: list[Sentinel2Band]
    roi: list[list[tuple[float, float]]] | tuple[float, float]
