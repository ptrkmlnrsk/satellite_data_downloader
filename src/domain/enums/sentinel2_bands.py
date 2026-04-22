from enum import Enum


class Sentinel2Bands(Enum):
    """Enum object for Sentinel 2 bands.
    10 m resolution bands:
    B2, B3, B4, B8"""

    BLUE = {"code": "B2", "resolution": 10, "description": "Blue band"}
    GREEN = "B3"
    RED = "B4"
    RED_EDGE_1 = "B5"
    RED_EDGE_2 = "B6"
    RED_EDGE_3 = "B7"
    NIR = "B8"
    RED_EDGE_4 = "B8A"
    WATER_VAPOUR = "B9"
    CIRRUS = "B10"
    SWIR_1 = "B11"
    SWIR_2 = "B12"
