from pydantic import BaseModel, field_validator
from src.domain.enums.sentinel2_bands import Sentinel2Band


# from pydantic_geojson import PolygonModel
# from src.api.schemas.polygon_model import PolygonModel


class GEEImageDownload(BaseModel):
    """Pydantic model for the request body"""

    image_id: str
    # roi: PolygonModel
    roi: list[list[tuple[float, float]]]
    bands: list[str]

    @field_validator("bands")
    @classmethod
    def validate_bands(cls, bands: list[str]):
        parsed = [
            Sentinel2Band.from_any(b) for b in bands
        ]  # tu sie zamieniają stringi na enumy

        return [
            band.code for band in parsed
        ]  # zaamiana spowrotem enumow na kody bandow
