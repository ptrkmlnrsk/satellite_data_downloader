from pydantic import BaseModel

# from pydantic_geojson import PolygonModel
# from src.api.schemas.polygon_model import PolygonModel


class GEEImageDownload(BaseModel):
    """Pydantic model for the request body"""

    image_id: str
    # roi: PolygonModel
    roi: list[list[tuple[float, float]]]
    bands: list[str]
