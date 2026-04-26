from src.domain.polygon import PolygonModel

from dataclasses import dataclass
from ee import Geometry


class ImageRequest:
    image_id: str


@dataclass
class GEEImageRequest(ImageRequest):
    """An object to represent an Earth Engine image request"""

    image_id: str
    roi: PolygonModel
    bands: list[str]

    def convert_to_gee_roi(self):
        return Geometry(self.roi.model_dump())
