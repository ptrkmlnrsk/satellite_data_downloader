from pydantic import BaseModel

from src.domain.enums.sentinel2_bands import Sentinel2Band


class GEEImageRequest(BaseModel):
    """An object to represent an Earth Engine image request.
    Roi parameter has to be Polygon object with at least 3 vertices."""

    image_id: str
    bands: list[str]
    roi: list[list[tuple[float, float]]] | tuple[float, float]

    @classmethod
    def validate_bands(cls, bands: list[str]):
        return [Sentinel2Band.from_any(b) for b in bands]
