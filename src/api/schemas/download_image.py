from pydantic import BaseModel
from pydantic_geojson import PolygonModel


class GEEImageDownload(BaseModel):
    image_id: str
    roi: PolygonModel
    bands: list[str]
