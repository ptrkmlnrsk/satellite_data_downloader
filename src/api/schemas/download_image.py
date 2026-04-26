from pydantic import BaseModel

# from pydantic_geojson import PolygonModel
from src.domain.polygon import PolygonModel


class GEEImageDownload(BaseModel):
    """Pydantic model for the request body"""

    image_id: str
    roi: PolygonModel
    bands: list[str]
