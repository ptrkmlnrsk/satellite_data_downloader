from enum import Enum


class Bands(Enum):
    """Enum object for Sentinel 2 bands"""

    BLUE = "B2"
    GREEN = "B3"
    RED = "B4"
    NIR = "B8"
