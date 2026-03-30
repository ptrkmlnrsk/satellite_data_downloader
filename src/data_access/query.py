from dataclasses import dataclass
from ee import Geometry


@dataclass
class QueryParameters:
    """This dataclass contains all the parameters needed for the query to fetch satellite image"""

    roi: Geometry
    coordinates: list[float]
    date_range: tuple[str, str]
    cloud_cover: float
    bands: str
    sensor: str
    product_level: str
